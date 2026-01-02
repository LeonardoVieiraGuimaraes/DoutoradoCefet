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
    
    Args:
        grafo: Grafo NetworkX
        coloracao: Dicionário {vertice: cor}
        caminho_saida: Caminho para salvar arquivo PNG
    """
    num_vertices = grafo.number_of_nodes()
    cores_set = set(coloracao.values())
    cores_lista = [coloracao[node] for node in grafo.nodes()]
    
    # Adaptar visualização conforme tamanho do grafo
    if num_vertices <= 500:
        # Grafos pequenos: visualização completa com spring layout
        plt.figure(figsize=(10, 8))
        pos = nx.spring_layout(grafo, seed=42, iterations=50)
        node_size = 500
        font_size = 8
        dpi = 150
        
    else:
        # Grafos grandes: layout otimizado com figura menor
        plt.figure(figsize=(8, 6))
        # Usar layout kamada-kawai mais rápido para grafos grandes
        try:
            pos = nx.kamada_kawai_layout(grafo)
        except:
            # Se kamada-kawai falhar, usar spring com menos iterações
            pos = nx.spring_layout(grafo, seed=42, iterations=20, k=0.1)
        node_size = 100
        font_size = 0  # Sem labels para não poluir
        dpi = 100
    
    # Desenhar grafo
    nx.draw_networkx_edges(grafo, pos, alpha=0.2, width=0.5)
    nx.draw_networkx_nodes(grafo, pos, node_color=cores_lista, 
                          node_size=node_size, cmap='Set3', vmin=0, vmax=max(cores_set))
    
    if font_size > 0:
        nx.draw_networkx_labels(grafo, pos, font_size=font_size)
    
    plt.title(f"Coloração de Vértices ({num_vertices} vértices)\n(χ(G) = {max(cores_set) + 1})")
    plt.axis('off')
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


# ============================================================================
# GERAÇÃO DE GRÁFICOS
# ============================================================================

def gerar_graficos_parte1(resultados_list: List):
    """
    Gera gráficos de análise para Parte 1.
    
    Gera:
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
    
    # Gráfico 1: Escalabilidade (Tempo vs Tamanho)
    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 2, 1)
    tamanhos = df_agrupado['tamanho'].values
    tempos_media = df_agrupado[('tempo_segundos', 'mean')].values
    tempos_min = df_agrupado[('tempo_segundos', 'min')].values
    tempos_max = df_agrupado[('tempo_segundos', 'max')].values
    
    plt.semilogy(tamanhos, tempos_media, 'o-', label='Média', linewidth=2, markersize=8)
    plt.fill_between(tamanhos, tempos_min, tempos_max, alpha=0.2, label='Min-Max')
    
    plt.xlabel('Tamanho do Grafo (número de vértices)', fontsize=11, fontweight='bold')
    plt.ylabel('Tempo de Execução (segundos)', fontsize=11, fontweight='bold')
    plt.title('Escalabilidade: Crescimento Exponencial do Tempo', fontsize=12, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    # Gráfico 2: Número cromático vs Tamanho
    plt.subplot(1, 2, 2)
    cores_media = df_agrupado[('numero_cromatico', 'mean')].values
    
    plt.plot(tamanhos, cores_media, 's-', color='green', linewidth=2, markersize=8)
    plt.xlabel('Tamanho do Grafo (número de vértices)', fontsize=11, fontweight='bold')
    plt.ylabel('Número Cromático χ(G)', fontsize=11, fontweight='bold')
    plt.title('Número Cromático Encontrado', fontsize=12, fontweight='bold')
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    caminho = ConfiguradorDiretorios.obter_caminho_arquivo(
        'parte1', 'graficos', 'escalabilidade_forca_bruta.png'
    )
    plt.savefig(caminho, dpi=150, bbox_inches='tight')
    plt.close()
    
    print(f"✓ Gráficos Parte 1 salvos em: {caminho.split('/graficos/')[0]}/graficos/")


def gerar_graficos_parte2(resultados_list: List):
    """
    Gera gráficos de análise para Parte 2.
    
    Gera:
    1. Número de cores por instância
    2. Tempo de execução por instância
    3. Comparação densidade vs cores
    
    Args:
        resultados_list: Lista de resultados da heurística
    """
    if not resultados_list:
        print("⚠ Sem dados para gerar gráficos Parte 2")
        return
    
    df = pd.DataFrame(resultados_list)
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # Gráfico 1: Número de cores por instância
    ax1 = axes[0, 0]
    instancias = df['instancia_id'].values
    cores = df['cores_heuristica'].values
    cores_sorted_idx = np.argsort(cores)
    
    ax1.bar(instancias[cores_sorted_idx], cores[cores_sorted_idx], color='steelblue')
    ax1.set_xlabel('Instância DIMACS', fontsize=11, fontweight='bold')
    ax1.set_ylabel('Número de Cores (Heurística)', fontsize=11, fontweight='bold')
    ax1.set_title('Cores Encontradas por Instância', fontsize=12, fontweight='bold')
    ax1.grid(True, alpha=0.3, axis='y')
    
    # Gráfico 2: Tempo de execução por instância
    ax2 = axes[0, 1]
    tempos = df['tempo_segundos'].values
    tempos_sorted_idx = np.argsort(tempos)
    
    ax2.bar(instancias[tempos_sorted_idx], tempos[tempos_sorted_idx], color='coral')
    ax2.set_xlabel('Instância DIMACS', fontsize=11, fontweight='bold')
    ax2.set_ylabel('Tempo (segundos)', fontsize=11, fontweight='bold')
    ax2.set_title('Tempo de Execução por Instância', fontsize=12, fontweight='bold')
    ax2.grid(True, alpha=0.3, axis='y')
    
    # Gráfico 3: Número de vértices vs Cores
    ax3 = axes[1, 0]
    ax3.scatter(df['num_vertices'], df['cores_heuristica'], s=200, alpha=0.6, 
               c=df['num_vertices'], cmap='viridis')
    for i, txt in enumerate(df['instancia_id']):
        ax3.annotate(txt, (df['num_vertices'].iloc[i], df['cores_heuristica'].iloc[i]),
                    fontsize=10, fontweight='bold')
    
    ax3.set_xlabel('Número de Vértices', fontsize=11, fontweight='bold')
    ax3.set_ylabel('Número de Cores', fontsize=11, fontweight='bold')
    ax3.set_title('Vértices vs Cores (Tamanho = Cores)', fontsize=12, fontweight='bold')
    ax3.grid(True, alpha=0.3)
    
    # Gráfico 4: Densidade vs Cores
    ax4 = axes[1, 1]
    ax4.scatter(df['densidade'], df['cores_heuristica'], s=200, alpha=0.6,
               c=df['cores_heuristica'], cmap='Reds')
    for i, txt in enumerate(df['instancia_id']):
        ax4.annotate(txt, (df['densidade'].iloc[i], df['cores_heuristica'].iloc[i]),
                    fontsize=10, fontweight='bold')
    
    ax4.set_xlabel('Densidade do Grafo', fontsize=11, fontweight='bold')
    ax4.set_ylabel('Número de Cores', fontsize=11, fontweight='bold')
    ax4.set_title('Densidade vs Cores', fontsize=12, fontweight='bold')
    ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    caminho = ConfiguradorDiretorios.obter_caminho_arquivo(
        'parte2', 'graficos', 'analise_heuristica.png'
    )
    plt.savefig(caminho, dpi=150, bbox_inches='tight')
    plt.close()
    
    print(f"✓ Gráficos Parte 2 salvos em: {caminho.split('/graficos/')[0]}/graficos/")


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


# ============================================================================
# PONTO DE ENTRADA
# ============================================================================

if __name__ == "__main__":
    executar_solucao_completa()
