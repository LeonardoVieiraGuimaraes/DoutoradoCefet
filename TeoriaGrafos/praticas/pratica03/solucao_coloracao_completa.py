"""
SOLUÇÃO COMPLETA: PROBLEMA DE COLORAÇÃO DE VÉRTICES EM GRAFOS
==============================================================
Implementação de Força Bruta (Parte 1) e Heurística (Parte 2)

Objetivo:
---------
Encontrar o número cromático χ(G) de um grafo, ou seja, o número mínimo de cores
necessárias para colorir os vértices de modo que vértices adjacentes tenham cores diferentes.

Estrutura:
----------
PARTE 1 - Força Bruta:
  1. Algoritmo de força bruta para encontrar χ(G)
  2. Geração automática de instâncias aleatórias (tamanho 2 a n)
  3. Medição de tempo de execução

PARTE 2 - Heurística:
  1. Implementação de heurística (Welsh-Powell)
  2. Leitura de instâncias DIMACS (5 instâncias do Moodle)
  3. Cálculo de número de cores e tempo de execução

Saída:
------
Estrutura de diretórios:
  resultados/
  ├── parte1/
  │   ├── csv/
  │   │   ├── parametros_grafos.csv
  │   │   └── resultados_forca_bruta.csv
  │   ├── grafos/
  │   │   └── grafo_n*.png
  │   └── graficos/
  │       └── *.png
  └── parte2/
      ├── csv/
      │   └── resultados_heuristica.csv
      ├── grafos/
      │   └── *.png
      └── graficos/
          └── *.png

Autor: Gerado automaticamente
Data: 2025
"""

# ============================================================================
# IMPORTS E CONFIGURAÇÃO
# ============================================================================

import os
import csv
import time
import json
import random
from pathlib import Path
from itertools import product
from typing import Dict, Tuple, List, Set
import networkx as nx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Configurar estilo dos gráficos
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 10

# ============================================================================
# CONFIGURAÇÃO DE DIRETÓRIOS
# ============================================================================

class ConfiguradorDiretorios:
    """Classe auxiliar para criar e gerenciar estrutura de diretórios."""
    
    ESTRUTURA_DIRETORIOS = {
        'resultados/parte1/csv': [],
        'resultados/parte1/grafos': [],
        'resultados/parte1/graficos': [],
        'resultados/parte2/csv': [],
        'resultados/parte2/grafos': [],
        'resultados/parte2/graficos': [],
    }
    
    @staticmethod
    def criar_estrutura():
        """Cria a estrutura de diretórios completa."""
        for diretorio in ConfiguradorDiretorios.ESTRUTURA_DIRETORIOS.keys():
            Path(diretorio).mkdir(parents=True, exist_ok=True)
        print(f"✓ Estrutura de diretórios criada com sucesso")
    
    @staticmethod
    def obter_caminho_arquivo(tipo_parte: str, tipo_saida: str, nome_arquivo: str) -> str:
        """
        Retorna caminho completo para arquivo baseado em tipo.
        
        Args:
            tipo_parte: 'parte1' ou 'parte2'
            tipo_saida: 'csv', 'grafos' ou 'graficos'
            nome_arquivo: nome do arquivo
        
        Returns:
            Caminho completo do arquivo
        """
        return f"resultados/{tipo_parte}/{tipo_saida}/{nome_arquivo}"


# ============================================================================
# FUNÇÕES COMUNS / AUXILIARES GERAIS (usadas em Parte 1 e Parte 2)
# ============================================================================

def extrair_parametros_grafo(grafo: nx.Graph) -> Dict:
    """
    Extrai parâmetros estatísticos de um grafo.
    
    Função auxiliar comum usada em ambas as partes para extrair informações
    de um grafo (densidade, grau médio, conectividade, etc.).
    
    Args:
        grafo: Grafo NetworkX
        
    Returns:
        Dicionário com parâmetros do grafo
    """
    return {
        'num_vertices': grafo.number_of_nodes(),
        'num_arestas': grafo.number_of_edges(),
        'densidade': nx.density(grafo),
        'grau_medio': sum(dict(grafo.degree()).values()) / grafo.number_of_nodes(),
        'grau_minimo': min(dict(grafo.degree()).values()),
        'grau_maximo': max(dict(grafo.degree()).values()),
        'eh_conexo': nx.is_connected(grafo),
        'num_componentes': nx.number_connected_components(grafo),
    }


def visualizar_e_salvar_grafo(grafo: nx.Graph, coloracao: Dict, caminho_saida: str):
    """
    Visualiza grafo com coloração e salva como PNG.
    
    Função auxiliar comum que cria visualização dos grafos coloridos em ambas
    as partes da solução. Adapta a visualização conforme o tamanho do grafo.
    Implementa visualização adaptativa com estatísticas visuais.
    
    Args:
        grafo: Grafo NetworkX
        coloracao: Dicionário {vertice: cor}
        caminho_saida: Caminho para salvar arquivo PNG
    """
    num_vertices = grafo.number_of_nodes()
    num_arestas = grafo.number_of_edges()
    cores_set = set(coloracao.values())
    num_cores = max(cores_set) + 1
    cores_lista = [coloracao[node] for node in grafo.nodes()]
    densidade = nx.density(grafo)
    
    # Calcular distribuição de cores
    distribuicao_cores = {}
    for cor in cores_set:
        distribuicao_cores[cor] = sum(1 for v in coloracao.values() if v == cor)
    
    # Criar figura com subplot para grafos grandes (inclui estatísticas)
    if num_vertices <= 100:
        # ======= GRAFOS MUITO PEQUENOS (≤100): Visualização Completa com Labels =======
        fig = plt.figure(figsize=(12, 8))
        
        # Subplot principal: grafo
        ax_grafo = plt.subplot(1, 2, 1)
        pos = nx.spring_layout(grafo, seed=42, iterations=50)
        
        nx.draw_networkx_edges(grafo, pos, alpha=0.3, width=0.8, ax=ax_grafo)
        nx.draw_networkx_nodes(grafo, pos, node_color=cores_lista, 
                              node_size=500, cmap='Set3', vmin=0, 
                              vmax=max(cores_set), ax=ax_grafo)
        nx.draw_networkx_labels(grafo, pos, font_size=7, ax=ax_grafo)
        
        ax_grafo.set_title(f'Coloração de Vértices\n{num_vertices} vértices, {num_arestas} arestas',
                          fontsize=12, fontweight='bold')
        ax_grafo.axis('off')
        
        # Subplot de estatísticas: distribuição de cores
        ax_stats = plt.subplot(1, 2, 2)
        cores_ids = sorted(distribuicao_cores.keys())
        contagens = [distribuicao_cores[c] for c in cores_ids]
        colors_bar = plt.cm.Set3(np.linspace(0, 1, num_cores))
        
        bars = ax_stats.bar(cores_ids, contagens, color=colors_bar[:len(cores_ids)], 
                            edgecolor='black', linewidth=1.5)
        ax_stats.set_xlabel('Cor', fontsize=11, fontweight='bold')
        ax_stats.set_ylabel('Número de Vértices', fontsize=11, fontweight='bold')
        ax_stats.set_title('Distribuição de Cores', fontsize=12, fontweight='bold')
        ax_stats.grid(True, alpha=0.3, axis='y')
        
        # Adicionar valores nas barras
        for bar, count in zip(bars, contagens):
            height = bar.get_height()
            ax_stats.text(bar.get_x() + bar.get_width()/2., height,
                         f'{int(count)}', ha='center', va='bottom', fontweight='bold')
        
        # Adicionar informações estatísticas
        info_text = f"χ(G) = {num_cores} cores\nDensidade: {densidade:.4f}\nGrau médio: {2*num_arestas/num_vertices:.2f}"
        ax_stats.text(0.02, 0.98, info_text, transform=ax_stats.transAxes,
                     fontsize=10, verticalalignment='top',
                     bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
        
        dpi = 150
        
    elif num_vertices <= 1000:
        # ======= GRAFOS MÉDIOS (501-1000): Layout Otimizado + Stats =======
        fig = plt.figure(figsize=(14, 6))
        
        # Subplot principal: grafo
        ax_grafo = plt.subplot(1, 3, (1, 2))
        try:
            pos = nx.kamada_kawai_layout(grafo)
        except:
            pos = nx.spring_layout(grafo, seed=42, iterations=30, k=0.15)
        
        nx.draw_networkx_edges(grafo, pos, alpha=0.15, width=0.3, ax=ax_grafo)
        nx.draw_networkx_nodes(grafo, pos, node_color=cores_lista,
                              node_size=150, cmap='Set3', vmin=0,
                              vmax=max(cores_set), ax=ax_grafo, edgecolors='black', linewidths=0.5)
        
        ax_grafo.set_title(f'Coloração de Vértices - {num_vertices} vértices\nχ(G) = {num_cores} cores',
                          fontsize=12, fontweight='bold')
        ax_grafo.axis('off')
        
        # Subplot de estatísticas
        ax_stats = plt.subplot(1, 3, 3)
        cores_ids = sorted(distribuicao_cores.keys())
        contagens = [distribuicao_cores[c] for c in cores_ids]
        colors_bar = plt.cm.Set3(np.linspace(0, 1, num_cores))
        
        ax_stats.barh(cores_ids, contagens, color=colors_bar[:len(cores_ids)],
                     edgecolor='black', linewidth=1)
        ax_stats.set_ylabel('Cor', fontsize=10, fontweight='bold')
        ax_stats.set_xlabel('Vértices', fontsize=10, fontweight='bold')
        ax_stats.set_title('Distribuição', fontsize=11, fontweight='bold')
        ax_stats.grid(True, alpha=0.3, axis='x')
        ax_stats.invert_yaxis()
        
        info_text = f"Vértices: {num_vertices}\nArestas: {num_arestas}\nχ(G): {num_cores}\nDensidade: {densidade:.5f}\nGrau médio: {2*num_arestas/num_vertices:.2f}"
        ax_stats.text(0.02, 0.02, info_text, transform=ax_stats.transAxes,
                     fontsize=9, verticalalignment='bottom',
                     bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))
        
        dpi = 120
        
    else:
        # ======= GRAFOS GRANDES (>1000): Layout Consistente com Médios =======
        fig = plt.figure(figsize=(14, 6))
        
        # Subplot principal: grafo
        ax_grafo = plt.subplot(1, 3, (1, 2))
        try:
            # Para grafos muito grandes, usar layout mais rápido
            pos = nx.spring_layout(grafo, seed=42, iterations=15, k=0.2)
        except:
            pos = nx.random_layout(grafo, seed=42)
        
        nx.draw_networkx_edges(grafo, pos, alpha=0.08, width=0.2, ax=ax_grafo)
        nx.draw_networkx_nodes(grafo, pos, node_color=cores_lista,
                              node_size=50, cmap='Set3', vmin=0,
                              vmax=max(cores_set), ax=ax_grafo, linewidths=0)
        
        ax_grafo.set_title(f'Coloração de Vértices - {num_vertices} vértices\nχ(G) = {num_cores} cores',
                          fontsize=12, fontweight='bold')
        ax_grafo.axis('off')
        
        # Subplot de estatísticas: distribuição de cores (barras horizontais)
        ax_stats = plt.subplot(1, 3, 3)
        cores_ids = sorted(distribuicao_cores.keys())
        contagens = [distribuicao_cores[c] for c in cores_ids]
        colors_bar = plt.cm.Set3(np.linspace(0, 1, num_cores))
        
        ax_stats.barh(cores_ids, contagens, color=colors_bar[:len(cores_ids)],
                     edgecolor='black', linewidth=1)
        ax_stats.set_ylabel('Cor', fontsize=10, fontweight='bold')
        ax_stats.set_xlabel('Vértices', fontsize=10, fontweight='bold')
        ax_stats.set_title('Distribuição', fontsize=11, fontweight='bold')
        ax_stats.grid(True, alpha=0.3, axis='x')
        ax_stats.invert_yaxis()
        
        info_text = f"Vértices: {num_vertices}\nArestas: {num_arestas}\nχ(G): {num_cores}\nDensidade: {densidade:.5f}\nGrau médio: {2*num_arestas/num_vertices:.2f}"
        ax_stats.text(0.02, 0.02, info_text, transform=ax_stats.transAxes,
                     fontsize=9, verticalalignment='bottom',
                     bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))
        
        dpi = 120
    
    plt.tight_layout()
    plt.savefig(caminho_saida, dpi=dpi, bbox_inches='tight')
    plt.close()


def ler_arquivo_dimacs(caminho_arquivo: str) -> nx.Graph:
    """
    Função auxiliar comum: Lê arquivo DIMACS e cria grafo NetworkX.
    
    Formato DIMACS:
    - Linhas começadas com 'c' são comentários
    - Linha 'p edge <n> <m>' define n vértices e m arestas
    - Linhas 'e <u> <v>' definem arestas
    
    Args:
        caminho_arquivo: Caminho do arquivo DIMACS
        
    Returns:
        Grafo NetworkX ou None se arquivo não existir
    """
    if not os.path.exists(caminho_arquivo):
        print(f"⚠ Arquivo não encontrado: {caminho_arquivo}")
        return None
    
    grafo = nx.Graph()
    
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8', errors='ignore') as f:
            for linha in f:
                linha = linha.strip()
                
                # Ignorar comentários
                if linha.startswith('c'):
                    continue
                
                # Linha de problema (define número de vértices)
                if linha.startswith('p edge'):
                    partes = linha.split()
                    num_vertices = int(partes[2])
                    num_arestas = int(partes[3])
                    grafo.add_nodes_from(range(1, num_vertices + 1))
                    continue
                
                # Linhas de aresta
                if linha.startswith('e'):
                    partes = linha.split()
                    u = int(partes[1])
                    v = int(partes[2])
                    grafo.add_edge(u, v)
        
        return grafo
    
    except Exception as e:
        print(f"⚠ Erro ao ler arquivo DIMACS: {str(e)}")
        return None


# ============================================================================
# PARTE 1: IMPLEMENTAÇÃO - FORÇA BRUTA
# ============================================================================

def gerar_instancia_grafo_aleatorio(num_vertices: int, probabilidade: float, 
                                   seed: int = None) -> nx.Graph:
    """
    REQUISITO 2 - PARTE 1: Gera instância aleatória de grafo.
    
    Cria um grafo aleatório usando modelo Erdős-Rényi:
    - Não direcionado
    - Não ponderado
    - Sem loops ou arestas paralelas (garantido pelo modelo)
    
    Args:
        num_vertices: Número de vértices (n)
        probabilidade: Probabilidade de aresta entre dois vértices (0 a 1)
        seed: Seed para reprodutibilidade
    
    Returns:
        Grafo NetworkX não direcionado
    """
    if seed is not None:
        random.seed(seed)
        np.random.seed(seed)
    
    # Modelo Erdős-Rényi: grafo aleatório
    grafo = nx.erdos_renyi_graph(n=num_vertices, p=probabilidade)
    
    # Garantir que o grafo tem arestas (para grafos muito pequenos)
    while grafo.number_of_edges() == 0 and num_vertices > 1:
        grafo = nx.erdos_renyi_graph(n=num_vertices, p=probabilidade)
    
    return grafo


def algoritmo_forca_bruta_coloracao(grafo: nx.Graph) -> Tuple[int, Dict, float]:
    """
    REQUISITO 1 - PARTE 1: Implementa algoritmo de força bruta para coloração.
    
    ESTRATÉGIA:
    -----------
    Para cada número de cores k = 1, 2, 3, ...:
      1. Gera todas as combinações possíveis de cores para os vértices (k^n)
      2. Para cada combinação, verifica se é válida (vértices adjacentes diferem)
      3. Se válida, retorna k como número cromático
    
    Complexidade: O(k^n) - Exponencial, viável para n ≤ ~15-20 vértices
    
    Args:
        grafo: Grafo NetworkX
        
    Returns:
        Tupla: (número_cromático, coloração_dict, tempo_segundos)
    """
    inicio = time.time()
    
    vertices = list(grafo.nodes())
    n_vertices = len(vertices)
    
    # Tentar com 1, 2, 3, ... cores até encontrar coloração válida
    for num_cores in range(1, n_vertices + 1):
        # Gera todas as combinações de cores (k^n possibilidades)
        for cores_tuple in product(range(num_cores), repeat=n_vertices):
            # Cria dicionário de coloração
            coloracao = {vertices[i]: cores_tuple[i] for i in range(n_vertices)}
            
            # Verifica se coloração é válida (vértices adjacentes com cores diferentes)
            eh_valida = True
            for u, v in grafo.edges():
                if coloracao[u] == coloracao[v]:
                    eh_valida = False
                    break
            
            # Se válida, encontramos χ(G)
            if eh_valida:
                tempo = time.time() - inicio
                return num_cores, coloracao, tempo
    
    # Nunca deve chegar aqui (coloração sempre existe)
    tempo = time.time() - inicio
    return n_vertices, {v: i for i, v in enumerate(vertices)}, tempo


def processar_instancias_por_tamanho(tamanho_min: int = 5, tamanho_max: int = 13,
                                     probabilidade: float = 0.3,
                                     num_instancias_por_tamanho: int = 3) -> Tuple[List, List]:
    """
    REQUISITO 2 + 3 - PARTE 1: Processa múltiplas instâncias aleatórias.
    
    Gera instâncias de tamanho tamanho_min a tamanho_max e aplica força bruta em cada.
    Mede tempo de execução para cada instância.
    
    Args:
        tamanho_min: Tamanho mínimo (padrão 5 vértices)
        tamanho_max: Tamanho máximo (padrão 13 vértices)
        probabilidade: Probabilidade de aresta entre vértices
        num_instancias_por_tamanho: Número de instâncias por tamanho
        
    Returns:
        Tupla: (lista_parametros, lista_resultados)
    """
    lista_parametros = []
    lista_resultados = []
    
    print("\n" + "="*70)
    print("PARTE 1: PROCESSANDO INSTÂNCIAS ALEATÓRIAS COM FORÇA BRUTA")
    print("="*70)
    
    for tamanho in range(tamanho_min, tamanho_max + 1):
        print(f"\nTamanho: {tamanho} vértices", end="")
        
        for instancia_idx in range(num_instancias_por_tamanho):
            # Gerar instância
            seed = tamanho * 1000 + instancia_idx
            grafo = gerar_instancia_grafo_aleatorio(tamanho, probabilidade, seed=seed)
            
            # Extrair parâmetros
            parametros = extrair_parametros_grafo(grafo)
            parametros['tamanho'] = tamanho
            parametros['instancia'] = instancia_idx + 1
            parametros['id_grafo'] = f"n{tamanho:02d}_i{instancia_idx+1:02d}"
            
            # Aplicar força bruta
            try:
                num_cromatico, coloracao, tempo = algoritmo_forca_bruta_coloracao(grafo)
                
                resultado = {
                    'id_grafo': parametros['id_grafo'],
                    'tamanho': tamanho,
                    'instancia': instancia_idx + 1,
                    'numero_cromatico': num_cromatico,
                    'tempo_segundos': tempo,
                    'arestas': parametros['num_arestas'],
                }
                
                lista_parametros.append(parametros)
                lista_resultados.append(resultado)
                
                # Salvar visualização
                caminho_grafo = ConfiguradorDiretorios.obter_caminho_arquivo(
                    'parte1', 'grafos', f"grafo_{parametros['id_grafo']}.png"
                )
                visualizar_e_salvar_grafo(grafo, coloracao, caminho_grafo)
                
                print(".", end="", flush=True)
            
            except KeyboardInterrupt:
                print("\n⚠ Execução interrompida pelo usuário")
                break
            except Exception as e:
                print(f"\n⚠ Erro ao processar grafo {tamanho}_{instancia_idx}: {str(e)}")
                continue
        
        print(f" [{tamanho} vértices processado]")
    
    print("\n✓ Processamento de instâncias concluído")
    return lista_parametros, lista_resultados


# ============================================================================
# PARTE 2: IMPLEMENTAÇÃO - HEURÍSTICA WELSH-POWELL
# ============================================================================

def algoritmo_welsh_powell(grafo: nx.Graph) -> Tuple[int, Dict, float]:
    """
    REQUISITO 1 - PARTE 2: Implementa heurística Welsh-Powell para coloração.
    
    ESTRATÉGIA:
    -----------
    Algoritmo guloso que ordena vértices por grau decrescente:
    1. Ordena vértices por grau (maior primeiro)
    2. Para cada vértice em ordem:
       - Atribui a menor cor disponível (que não foi usada por vizinhos)
    
    Complexidade: O(n + m) - Linear em número de vértices e arestas
    Garantias: Encontra coloração válida (nem sempre ótima)
    Qualidade: Típicamente O(Δ + 1) cores, onde Δ é grau máximo
    
    Args:
        grafo: Grafo NetworkX
        
    Returns:
        Tupla: (número_cores_usado, coloracao_dict, tempo_segundos)
    """
    inicio = time.time()
    
    # Ordenar vértices por grau decrescente (heurística Welsh-Powell)
    graus = dict(grafo.degree())
    vertices_ordenados = sorted(graus.keys(), key=lambda v: graus[v], reverse=True)
    
    coloracao = {}
    
    # Para cada vértice em ordem de grau decrescente
    for vertice in vertices_ordenados:
        # Cores já usadas pelos vizinhos
        cores_vizinhos = set()
        for vizinho in grafo.neighbors(vertice):
            if vizinho in coloracao:
                cores_vizinhos.add(coloracao[vizinho])
        
        # Encontrar menor cor disponível
        cor = 0
        while cor in cores_vizinhos:
            cor += 1
        
        coloracao[vertice] = cor
    
    tempo = time.time() - inicio
    num_cores = max(coloracao.values()) + 1 if coloracao else 0
    
    return num_cores, coloracao, tempo


def processar_instancias_dimacs() -> List:
    """
    REQUISITO 2 + 3 - PARTE 2: Processa instâncias DIMACS com heurística.
    
    Nota: Este é um template. Você deve colocar os arquivos DIMACS em
    'instancias/' e atualizar os caminhos abaixo.
    
    Instâncias esperadas (do Moodle):
      a. 450 vértices, 8260 arestas
      b. 864 vértices, 18707 arestas
      c. 1000 vértices, 14378 arestas
      d. 1916 vértices, 12506 arestas
      e. 4730 vértices, 286722 arestas
    
    Returns:
        Lista de resultados para cada instância
    """
    lista_resultados = []
    
    # Definir instâncias esperadas (atualizar conforme necessário)
    instancias = [
        {
            'id': 'a',
            'caminho': 'instancias/a - le450_25a.col.txt',
            'vertices_esperados': 450,
            'arestas_esperadas': 8260,
        },
        {
            'id': 'b',
            'caminho': 'instancias/b - inithx.i.1.col.txt',
            'vertices_esperados': 864,
            'arestas_esperadas': 18707,
        },
        {
            'id': 'c',
            'caminho': 'instancias/c - r1000.1.col.txt',
            'vertices_esperados': 1000,
            'arestas_esperadas': 14378,
        },
        {
            'id': 'd',
            'caminho': 'instancias/d - ash958GPIA.col.txt',
            'vertices_esperados': 1916,
            'arestas_esperadas': 12506,
        },
        {
            'id': 'e',
            'caminho': 'instancias/e - wap03a.col.txt',
            'vertices_esperados': 4730,
            'arestas_esperadas': 286722,
        },
    ]
    
    print("\n" + "="*70)
    print("PARTE 2: PROCESSANDO INSTÂNCIAS DIMACS COM HEURÍSTICA")
    print("="*70)
    
    for instancia in instancias:
        print(f"\nProcessando instância {instancia['id']}... ", end="", flush=True)
        
        grafo = ler_arquivo_dimacs(instancia['caminho'])
        
        if grafo is None:
            print(f"⚠ Não encontrado")
            continue
        
        # Verificar se grafo tem vértices
        if grafo.number_of_nodes() == 0:
            print(f"⚠ Grafo vazio")
            continue
        
        try:
            # Aplicar heurística Welsh-Powell
            num_cores, coloracao, tempo = algoritmo_welsh_powell(grafo)
            
            resultado = {
                'instancia_id': instancia['id'],
                'caminho': instancia['caminho'],
                'num_vertices': grafo.number_of_nodes(),
                'num_arestas': grafo.number_of_edges(),
                'cores_heuristica': num_cores,
                'tempo_segundos': tempo,
                'densidade': nx.density(grafo),
                'grau_medio': sum(dict(grafo.degree()).values()) / grafo.number_of_nodes(),
            }
            
            lista_resultados.append(resultado)
            print(f"✓ {num_cores} cores em {tempo:.4f}s")
            
            # Salvar visualização para todas as instâncias
            caminho_grafo = ConfiguradorDiretorios.obter_caminho_arquivo(
                'parte2', 'grafos', f"instancia_{instancia['id']}.png"
            )
            visualizar_e_salvar_grafo(grafo, coloracao, caminho_grafo)
        
        except Exception as e:
            print(f"⚠ Erro: {str(e)}")
            continue
    
    print("\n✓ Processamento de instâncias DIMACS concluído")
    return lista_resultados


# ============================================================================
# EXPORTAÇÃO DE DADOS
# ============================================================================

def salvar_resultados_csv_parte1(parametros_list: List, resultados_list: List):
    """
    Salva resultados da Parte 1 em CSV.
    
    Args:
        parametros_list: Lista de dicionários com parâmetros dos grafos
        resultados_list: Lista de dicionários com resultados da força bruta
    """
    # CSV de parâmetros
    if parametros_list:
        df_parametros = pd.DataFrame(parametros_list)
        caminho = ConfiguradorDiretorios.obter_caminho_arquivo(
            'parte1', 'csv', 'parametros_grafos.csv'
        )
        df_parametros.to_csv(caminho, index=False)
        print(f"✓ Parâmetros salvos em: {caminho}")
    
    # CSV de resultados
    if resultados_list:
        df_resultados = pd.DataFrame(resultados_list)
        caminho = ConfiguradorDiretorios.obter_caminho_arquivo(
            'parte1', 'csv', 'resultados_forca_bruta.csv'
        )
        df_resultados.to_csv(caminho, index=False)
        print(f"✓ Resultados salvos em: {caminho}")


def salvar_resultados_csv_parte2(resultados_list: List):
    """
    Salva resultados da Parte 2 em CSV.
    
    Args:
        resultados_list: Lista de dicionários com resultados da heurística
    """
    if resultados_list:
        df_resultados = pd.DataFrame(resultados_list)
        caminho = ConfiguradorDiretorios.obter_caminho_arquivo(
            'parte2', 'csv', 'resultados_heuristica.csv'
        )
        df_resultados.to_csv(caminho, index=False)
        print(f"✓ Resultados heurística salvos em: {caminho}")


def salvar_informacoes_instancias(resultados_list: List):
    """
    Salva informações estruturais das instâncias DIMACS em CSV.
    
    Gera um CSV com metadados de cada instância:
    - Nome da instância
    - Número de vértices
    - Número de arestas
    - Densidade do grafo
    - Grau médio
    - Número de cores encontradas
    - Tempo de execução
    
    Args:
        resultados_list: Lista de dicionários com resultados da heurística
    """
    if not resultados_list:
        print("⚠ Sem dados para gerar CSV de informações das instâncias")
        return
    
    # Extrair e calcular informações relevantes
    info_instancias = []
    for res in resultados_list:
        n = res['num_vertices']
        m = res['num_arestas']
        densidade = (2 * m) / (n * (n - 1)) if n > 1 else 0
        grau_medio = (2 * m) / n if n > 0 else 0
        
        info_instancias.append({
            'instancia': res['instancia_id'],
            'num_vertices': n,
            'num_arestas': m,
            'densidade': round(densidade, 4),
            'grau_medio': round(grau_medio, 2),
            'cores_encontradas': res['cores_heuristica'],
            'tempo_segundos': res['tempo_segundos']
        })
    
    df_info = pd.DataFrame(info_instancias)
    caminho = ConfiguradorDiretorios.obter_caminho_arquivo(
        'parte2', 'csv', 'informacoes_instancias.csv'
    )
    df_info.to_csv(caminho, index=False)
    print(f"✓ Informações das instâncias salvas em: informacoes_instancias.csv")


# ============================================================================
# GERAÇÃO DE GRÁFICOS
# ============================================================================

def gerar_graficos_parte1(resultados_list: List):
    """
    Gera gráficos de análise para Parte 1.
    
    Gera 2 gráficos separados:
    1. Gráfico de escalabilidade (tempo vs tamanho)
    2. Gráfico de número cromático (χ(G) vs tamanho)
    
    Args:
        resultados_list: Lista de resultados da força bruta
    """
    if not resultados_list:
        print("⚠ Sem dados para gerar gráficos Parte 1")
        return
    
    df = pd.DataFrame(resultados_list)
    
    # Agrupar por tamanho
    df_agrupado = df.groupby('tamanho').agg({
        'tempo_segundos': ['mean', 'min', 'max'],
        'numero_cromatico': 'mean'
    }).reset_index()
    
    tamanhos = df_agrupado['tamanho'].values
    tempos_media = df_agrupado[('tempo_segundos', 'mean')].values
    tempos_min = df_agrupado[('tempo_segundos', 'min')].values
    tempos_max = df_agrupado[('tempo_segundos', 'max')].values
    cores_media = df_agrupado[('numero_cromatico', 'mean')].values
    
    # Gráfico 1: Escalabilidade (Tempo vs Tamanho)
    plt.figure(figsize=(12, 7))
    
    plt.semilogy(tamanhos, tempos_media, 'o-', label='Média', linewidth=2.5, markersize=10, color='#2E86AB')
    plt.fill_between(tamanhos, tempos_min, tempos_max, alpha=0.25, label='Min-Max', color='#2E86AB')
    
    plt.xlabel('Tamanho do Grafo (número de vértices)', fontsize=13, fontweight='bold')
    plt.ylabel('Tempo de Execução (segundos)', fontsize=13, fontweight='bold')
    plt.title('Escalabilidade: Crescimento Exponencial do Tempo', fontsize=15, fontweight='bold')
    plt.grid(True, alpha=0.3, linestyle='--')
    plt.legend(fontsize=11)
    
    plt.tight_layout()
    caminho1 = ConfiguradorDiretorios.obter_caminho_arquivo(
        'parte1', 'graficos', 'grafico1_escalabilidade_tempo.png'
    )
    plt.savefig(caminho1, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  ✓ Gráfico 1 salvo: grafico1_escalabilidade_tempo.png")
    
    # Gráfico 2: Número cromático vs Tamanho
    plt.figure(figsize=(12, 7))
    
    plt.plot(tamanhos, cores_media, 's-', color='#06A77D', linewidth=2.5, markersize=10, markeredgecolor='black', markeredgewidth=1.5)
    
    # Adicionar valores nos pontos
    for i, (x, y) in enumerate(zip(tamanhos, cores_media)):
        plt.text(x, y + 0.15, f'{y:.1f}', ha='center', va='bottom', fontweight='bold', fontsize=10)
    
    plt.xlabel('Tamanho do Grafo (número de vértices)', fontsize=13, fontweight='bold')
    plt.ylabel('Número Cromático χ(G)', fontsize=13, fontweight='bold')
    plt.title('Número Cromático Encontrado', fontsize=15, fontweight='bold')
    plt.grid(True, alpha=0.3, linestyle='--')
    
    plt.tight_layout()
    caminho2 = ConfiguradorDiretorios.obter_caminho_arquivo(
        'parte1', 'graficos', 'grafico2_numero_cromatico.png'
    )
    plt.savefig(caminho2, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  ✓ Gráfico 2 salvo: grafico2_numero_cromatico.png")
    
    print(f"\n✓ Todos os gráficos Parte 1 salvos em: resultados/parte1/graficos/")


def gerar_graficos_parte2(resultados_list: List):
    """
    Gera gráficos de análise para Parte 2.
    
    Gera 4 gráficos separados:
    1. Número de cores por instância
    2. Tempo de execução por instância
    3. Número de vértices vs cores
    4. Densidade vs cores
    
    Args:
        resultados_list: Lista de resultados da heurística
    """
    if not resultados_list:
        print("⚠ Sem dados para gerar gráficos Parte 2")
        return
    
    df = pd.DataFrame(resultados_list)
    instancias = df['instancia_id'].values
    
    # Gráfico 1: Número de cores por instância
    plt.figure(figsize=(10, 6))
    cores = df['cores_heuristica'].values
    cores_sorted_idx = np.argsort(cores)
    
    plt.bar(instancias[cores_sorted_idx], cores[cores_sorted_idx], color='steelblue', edgecolor='black', linewidth=1.5)
    plt.xlabel('Instância DIMACS', fontsize=12, fontweight='bold')
    plt.ylabel('Número de Cores (Heurística)', fontsize=12, fontweight='bold')
    plt.title('Cores Encontradas por Instância', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3, axis='y')
    
    # Adicionar valores nas barras
    for idx in cores_sorted_idx:
        plt.text(instancias[idx], cores[idx] + 1, str(int(cores[idx])), 
                ha='center', va='bottom', fontweight='bold', fontsize=11)
    
    plt.tight_layout()
    caminho1 = ConfiguradorDiretorios.obter_caminho_arquivo(
        'parte2', 'graficos', 'grafico1_cores_por_instancia.png'
    )
    plt.savefig(caminho1, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  ✓ Gráfico 1 salvo: grafico1_cores_por_instancia.png")
    
    # Gráfico 2: Tempo de execução por instância
    plt.figure(figsize=(10, 6))
    tempos = df['tempo_segundos'].values
    tempos_sorted_idx = np.argsort(tempos)
    
    plt.bar(instancias[tempos_sorted_idx], tempos[tempos_sorted_idx], color='coral', edgecolor='black', linewidth=1.5)
    plt.xlabel('Instância DIMACS', fontsize=12, fontweight='bold')
    plt.ylabel('Tempo (segundos)', fontsize=12, fontweight='bold')
    plt.title('Tempo de Execução por Instância', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3, axis='y')
    
    # Adicionar valores nas barras
    for idx in tempos_sorted_idx:
        plt.text(instancias[idx], tempos[idx] + max(tempos)*0.02, f'{tempos[idx]:.4f}s', 
                ha='center', va='bottom', fontweight='bold', fontsize=10)
    
    plt.tight_layout()
    caminho2 = ConfiguradorDiretorios.obter_caminho_arquivo(
        'parte2', 'graficos', 'grafico2_tempo_execucao.png'
    )
    plt.savefig(caminho2, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  ✓ Gráfico 2 salvo: grafico2_tempo_execucao.png")
    
    # Gráfico 3: Número de vértices vs Cores
    plt.figure(figsize=(10, 7))
    scatter = plt.scatter(df['num_vertices'], df['cores_heuristica'], s=300, alpha=0.7, 
               c=df['num_vertices'], cmap='viridis', edgecolors='black', linewidth=2)
    
    for i, txt in enumerate(df['instancia_id']):
        plt.annotate(txt, (df['num_vertices'].iloc[i], df['cores_heuristica'].iloc[i]),
                    fontsize=12, fontweight='bold', ha='center', va='center')
    
    plt.xlabel('Número de Vértices', fontsize=12, fontweight='bold')
    plt.ylabel('Número de Cores', fontsize=12, fontweight='bold')
    plt.title('Vértices vs Cores', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.colorbar(scatter, label='Número de Vértices')
    
    plt.tight_layout()
    caminho3 = ConfiguradorDiretorios.obter_caminho_arquivo(
        'parte2', 'graficos', 'grafico3_vertices_vs_cores.png'
    )
    plt.savefig(caminho3, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  ✓ Gráfico 3 salvo: grafico3_vertices_vs_cores.png")
    
    # Gráfico 4: Densidade vs Cores
    plt.figure(figsize=(10, 7))
    scatter = plt.scatter(df['densidade'], df['cores_heuristica'], s=300, alpha=0.7,
               c=df['cores_heuristica'], cmap='Reds', edgecolors='black', linewidth=2)
    
    for i, txt in enumerate(df['instancia_id']):
        plt.annotate(txt, (df['densidade'].iloc[i], df['cores_heuristica'].iloc[i]),
                    fontsize=12, fontweight='bold', ha='center', va='center')
    
    plt.xlabel('Densidade do Grafo', fontsize=12, fontweight='bold')
    plt.ylabel('Número de Cores', fontsize=12, fontweight='bold')
    plt.title('Densidade vs Cores', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.colorbar(scatter, label='Número de Cores')
    
    plt.tight_layout()
    caminho4 = ConfiguradorDiretorios.obter_caminho_arquivo(
        'parte2', 'graficos', 'grafico4_densidade_vs_cores.png'
    )
    plt.savefig(caminho4, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  ✓ Gráfico 4 salvo: grafico4_densidade_vs_cores.png")
    
    print(f"\n✓ Todos os gráficos Parte 2 salvos em: resultados/parte2/graficos/")


# ============================================================================
# CONSOLIDAÇÃO E VERIFICAÇÃO DE CSVs
# ============================================================================

def consolidar_dados_csv():
    """
    Consolida e verifica todos os arquivos CSV gerados.
    
    Função modular que:
    1. Cria diretório de resultados
    2. Localiza todos os arquivos CSV gerados
    3. Exibe origem e conteúdo de cada CSV
    4. Confirma que os dados estão prontos para gerar tabelas LaTeX
    
    Returns:
        dict: Dicionário com informações sobre os CSVs encontrados
    """
    
    print("\n" + "="*70)
    print("CONSOLIDANDO E VERIFICANDO CSVs GERADOS")
    print("="*70)
    
    # Criar diretório se não existir
    Path('resultados').mkdir(exist_ok=True)
    
    print("\n📊 ORIGEM DOS DADOS (CSVs gerados automaticamente):\n")
    
    print("PARTE 1 - FORÇA BRUTA:")
    print("  1️⃣  parametros_grafos.csv")
    print("      Origem: processar_instancias_por_tamanho()")
    print("      Conteúdo: Parâmetros estruturais dos 27 grafos aleatórios")
    print("      (tamanho: 5-13 vértices, 3 instâncias cada)\n")
    
    print("  2️⃣  resultados_forca_bruta.csv")
    print("      Origem: algoritmo_forca_bruta_coloracao()")
    print("      Conteúdo: Número cromático encontrado e tempo para cada grafo\n")
    
    print("PARTE 2 - HEURÍSTICA WELSH-POWELL:")
    print("  3️⃣  resultados_heuristica.csv")
    print("      Origem: processar_instancias_dimacs() → algoritmo_welsh_powell()")
    print("      Conteúdo: Cores encontradas, tempo e parâmetros das 5 instâncias DIMACS\n")
    
    print("  4️⃣  informacoes_instancias.csv")
    print("      Origem: salvar_informacoes_instancias()")
    print("      Conteúdo: Informações consolidadas das instâncias DIMACS")
    print("      (densidade, grau médio, cores, tempo)\n")
    
    # Verificar quais arquivos CSV foram gerados
    csv_files = []
    csv_info = {}
    
    print("-" * 70)
    print("Verificando arquivos CSV gerados...\n")
    
    for root, dirs, files in os.walk('resultados'):
        for file in sorted(files):
            if file.endswith('.csv'):
                path = os.path.join(root, file)
                csv_files.append(path)
                
                try:
                    df = pd.read_csv(path)
                    csv_info[file] = {
                        'path': path,
                        'linhas': len(df),
                        'colunas': len(df.columns),
                        'colunas_nomes': list(df.columns),
                        'status': '✓'
                    }
                    
                    print(f"✓ {path}")
                    print(f"    Linhas: {len(df)} | Colunas: {len(df.columns)}")
                    print(f"    Campos: {', '.join(df.columns[:3])}...")
                    print()
                    
                except Exception as e:
                    csv_info[file] = {
                        'path': path,
                        'status': '⚠',
                        'erro': str(e)
                    }
                    print(f"⚠️  {path}")
                    print(f"    Erro: {e}\n")
    
    # Resumo final
    print("-" * 70)
    if csv_files:
        print(f"\n✅ Total de arquivos CSV gerados: {len(csv_files)}")
        print("\n📁 Arquivos prontos para gerar tabelas LaTeX:")
        for csv_path in sorted(csv_files):
            print(f"   - {csv_path}")
    else:
        print("\n⚠️  Nenhum CSV encontrado!")
        print("   Execute as células de solução primeiro para gerar os dados.")
    
    print("\n" + "="*70)
    print("PRÓXIMAS ETAPAS")
    print("="*70)
    print("""
1. Abra o notebook: gerar_tabelas_latex.ipynb
2. Execute as células para gerar as tabelas LaTeX
3. Os CSVs acima serão automaticamente lidos e convertidos em tabelas

Este fluxo garante que:
✓ Dados são calculados uma única vez (neste script)
✓ CSVs armazenam os resultados (fonte de verdade única)
✓ Tabelas LaTeX são geradas automaticamente (sempre sincronizadas)
✓ Relatório LaTeX usa as tabelas (dados sempre atualizados)
""")
    
    return csv_info


# ============================================================================
# FUNÇÃO PRINCIPAL - ORQUESTRA TODA A EXECUÇÃO
# ============================================================================

def executar_solucao_completa():
    """
    Executa a solução completa para o problema de coloração de vértices.
    
    Fluxo:
    1. Criar estrutura de diretórios
    2. PARTE 1: Gerar instâncias aleatórias e aplicar força bruta
    3. PARTE 2: Ler instâncias DIMACS e aplicar heurística
    4. Exportar resultados em CSV
    5. Gerar gráficos e visualizações
    6. Exibir resumo final
    """
    
    print("\n")
    print("╔" + "="*68 + "╗")
    print("║" + " "*15 + "SOLUÇÃO COMPLETA - COLORAÇÃO DE VÉRTICES" + " "*12 + "║")
    print("╚" + "="*68 + "╝")
    
    tempo_inicio = time.time()
    
    # ==================================================================
    # ETAPA 1: Criar Estrutura de Diretórios
    # ==================================================================
    print("\n[1/5] Criando estrutura de diretórios...")
    ConfiguradorDiretorios.criar_estrutura()
    
    # ==================================================================
    # ETAPA 2: PARTE 1 - Força Bruta com Instâncias Aleatórias
    # ==================================================================
    print("\n[2/5] Executando PARTE 1 - Força Bruta...")
    parametros_parte1, resultados_parte1 = processar_instancias_por_tamanho(
        tamanho_min=5,
        tamanho_max=13,
        probabilidade=0.3,
        num_instancias_por_tamanho=3
    )
    
    # ==================================================================
    # ETAPA 3: PARTE 2 - Heurística em Instâncias DIMACS
    # ==================================================================
    print("\n[3/5] Executando PARTE 2 - Heurística Welsh-Powell...")
    resultados_parte2 = processar_instancias_dimacs()
    
    # ==================================================================
    # ETAPA 4: Exportar Resultados em CSV
    # ==================================================================
    print("\n[4/5] Exportando resultados em CSV...")
    salvar_resultados_csv_parte1(parametros_parte1, resultados_parte1)
    salvar_resultados_csv_parte2(resultados_parte2)
    salvar_informacoes_instancias(resultados_parte2)
    
    # ==================================================================
    # ETAPA 5: Gerar Gráficos
    # ==================================================================
    print("\n[5/5] Gerando gráficos e visualizações...")
    gerar_graficos_parte1(resultados_parte1)
    gerar_graficos_parte2(resultados_parte2)
    
    # ==================================================================
    # RESUMO FINAL
    # ==================================================================
    tempo_total = time.time() - tempo_inicio
    
    print("\n" + "="*70)
    print("RESUMO FINAL DA EXECUÇÃO")
    print("="*70)
    
    print(f"\nPARTE 1 - FORÇA BRUTA:")
    print(f"  • Instâncias processadas: {len(resultados_parte1)}")
    if resultados_parte1:
        df_p1 = pd.DataFrame(resultados_parte1)
        print(f"  • Tamanhos testados: {df_p1['tamanho'].min()}-{df_p1['tamanho'].max()} vértices")
        print(f"  • Tempo máximo: {df_p1['tempo_segundos'].max():.4f}s")
        print(f"  • Tempo total Parte 1: {df_p1['tempo_segundos'].sum():.4f}s")
    
    print(f"\nPARTE 2 - HEURÍSTICA:")
    print(f"  • Instâncias DIMACS processadas: {len(resultados_parte2)}")
    if resultados_parte2:
        df_p2 = pd.DataFrame(resultados_parte2)
        print(f"  • Maiores instâncias: {df_p2['num_vertices'].max()} vértices, "
              f"{df_p2['num_arestas'].max()} arestas")
        print(f"  • Tempo máximo: {df_p2['tempo_segundos'].max():.4f}s")
    
    print(f"\nTEMPO TOTAL DE EXECUÇÃO: {tempo_total:.2f}s")
    
    print(f"\nARQUIVOS GERADOS:")
    print(f"  • resultados/parte1/csv/")
    print(f"  • resultados/parte1/grafos/")
    print(f"  • resultados/parte1/graficos/")
    print(f"  • resultados/parte2/csv/")
    print(f"  • resultados/parte2/grafos/")
    print(f"  • resultados/parte2/graficos/")
    
    print("\n" + "="*70)
    print("✓ EXECUÇÃO CONCLUÍDA COM SUCESSO")
    print("="*70 + "\n")
    
    # ==================================================================
    # ETAPA 6: Consolidar e Verificar CSVs para Tabelas LaTeX
    # ==================================================================
    print("\n[6/6] Consolidando dados em CSVs...")
    consolidar_dados_csv()


# ============================================================================
# PONTO DE ENTRADA
# ============================================================================

if __name__ == "__main__":
    executar_solucao_completa()
