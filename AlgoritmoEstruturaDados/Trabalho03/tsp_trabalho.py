#!/usr/bin/env python
# coding: utf-8

# # Trabalho Prático
# 
# Este notebook implementa e analisa algoritmos para o problema do Caixeiro Viajante (TSP), incluindo força bruta e heurística, conforme especificado no enunciado do trabalho.

# Nesta seção, importamos as bibliotecas essenciais para manipulação de dados, geração de instâncias, implementação dos algoritmos e visualização dos resultados.

# In[64]:


import numpy as np
import itertools
import time
import matplotlib.pyplot as plt
import random
import os


# ## Parte 01

# ### 1. Implementação do Algoritmo de Força Bruta
# 
# Implementar o método de força bruta para solucionar o problema, ou seja, um algoritmo que determina todas as possíveis rotas e escolhe a melhor, ou seja, a menor;

# In[65]:


def tsp_forca_bruta(matriz):
    n = len(matriz)
    cidades = list(range(n))
    menor_distancia = float('inf')
    melhor_rota = None
    for perm in itertools.permutations(cidades[1:]):
        rota = [0] + list(perm) + [0]
        distancia = sum(matriz[rota[i], rota[i+1]] for i in range(n))
        if distancia < menor_distancia:
            menor_distancia = distancia
            melhor_rota = rota
    return melhor_rota, menor_distancia


# ### 2. Gerar instâncias de tamanho 2 até n e aplicar o método de força bruta
# 
# Gerar instâncias de tamanho 2 à n e aplicar o método implementado no item 1;

# In[66]:


def gerar_matriz_tsp(n_cidades, peso_min=1, peso_max=100):
    matriz = np.random.randint(peso_min, peso_max+1, size=(n_cidades, n_cidades))
    np.fill_diagonal(matriz, 0)
    # Simetrizar para garantir grafo não-direcionado
    matriz = np.triu(matriz) + np.triu(matriz, 1).T
    return matriz

# Exemplo de geração de uma matriz para 5 cidades
n = 5
matriz_exemplo = gerar_matriz_tsp(n)
print(matriz_exemplo)
# Exemplo de uso:
rota, dist = tsp_forca_bruta(matriz_exemplo)
print('Melhor rota:', rota)
print('Distância:', dist)


# In[67]:


import networkx as nx
import matplotlib.pyplot as plt
import os

def plotar_grafo_tsp(matriz, rota=None, title="Grafo TSP", nome_arquivo=None):
    import networkx as nx
    import matplotlib.pyplot as plt
    import os

    n = len(matriz)
    G = nx.Graph()
    for i in range(n):
        G.add_node(i)
    for i in range(n):
        for j in range(i+1, n):
            if matriz[i, j] > 0:
                G.add_edge(i, j, weight=matriz[i, j])

    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(7, 7))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    # Destacar a melhor rota em vermelho
    if rota is not None and len(rota) > 1:
        edges_rota = [(rota[i], rota[i+1]) for i in range(len(rota)-1)]
        nx.draw_networkx_edges(G, pos, edgelist=edges_rota, edge_color='red', width=3)

    plt.title(title)
    if nome_arquivo is not None:
        if not os.path.exists('graficos'):
            os.makedirs('graficos')
        plt.savefig(f'graficos/{nome_arquivo}', bbox_inches='tight')
    plt.show()
# Exemplo de uso:
# Exemplo de uso:
plotar_grafo_tsp(matriz_exemplo, rota=rota, title="Grafo TSP - Melhor Rota", nome_arquivo="grafo_melhor_rota.png")


# ### 3. Computar o tempo de execução durante a aplicação da força bruta
# 
# Computar o tempo de execução durante a aplicação da força-bruta em cada uma das instâncias geradas. A aplicação do método deve ser realizada em quantas instâncias forem possíveis (possivelmente o tamanho máximo vai girar em torno de 10 a 14 cidades);
# 
# Obs.: as instâncias devem ser geradas de forma automática onde os pesos possuem valores aleatórios. Pode-se utilizar qualquer tipo de representação de grafos que se desejar.

# In[68]:


tempos = []
distancias = []
ns = list(range(2, 14)) 
for n in ns:
    matriz = gerar_matriz_tsp(n)
    inicio = time.time()
    rota, dist = tsp_forca_bruta(matriz)
    fim = time.time()
    tempos.append(fim - inicio)
    distancias.append(dist)
    #printar Matriz de adjacencia
    print(f'Matriz para {n} cidades:')
    print(gerar_matriz_tsp(n))
    # printar tempo e distância
    print(f'{n} cidades: tempo = {tempos[-1]:.4f}s, distância = {dist}, rota = {rota}')
    plotar_grafo_tsp(matriz, rota=rota, title=f"Grafo TSP - {n} Cidades", nome_arquivo=f"grafo_{n}_cidades.png")





# In[69]:


import os 
# Criando o diretório para salvar os gráficos, se não existir
if not os.path.exists('graficos'):
    os.makedirs('graficos')

plt.figure(figsize=(8,5))
plt.plot(ns, tempos, marker='o')
plt.yscale('log')
plt.xlabel('Número de cidades')
plt.ylabel('Tempo de execução (s) [escala log]')
plt.title('Crescimento do tempo de execução (força bruta)')
plt.grid(True)
plt.savefig('graficos/grafico_tempo_forca_bruta.png')
plt.show()


# ## Parte 2: Heurística 

# ### 1. Implementação de uma Heurística para o TSP
# 
# Aqui, implementamos uma heurística (vizinho mais próximo) para encontrar soluções aproximadas para o TSP.

# In[79]:


def tsp_vizinho_mais_proximo(matriz, inicio=0):
    n = len(matriz)
    visitado = [False]*n
    rota = [inicio]
    visitado[inicio] = True
    atual = inicio
    for _ in range(n-1):
        proximos = [(i, matriz[atual][i]) for i in range(n) if not visitado[i]]
        prox, _ = min(proximos, key=lambda x: x[1])
        rota.append(prox)
        visitado[prox] = True
        atual = prox
    rota.append(inicio)
    distancia = sum(matriz[rota[i], rota[i+1]] for i in range(n))
    return rota, distancia

# Exemplo de uso:
rota_h, dist_h = tsp_vizinho_mais_proximo(matriz_exemplo)
print('Rota heurística:', rota_h)
print('Distância heurística:', dist_h)


# In[80]:


tempos_heuristica = []
distancias_heuristica = []
ns = list(range(2, 14))
for n in ns:
    matriz = gerar_matriz_tsp(n)
    inicio = time.time()
    rota_h, dist_h = tsp_vizinho_mais_proximo(matriz)
    fim = time.time()
    tempos_heuristica.append(fim - inicio)
    distancias_heuristica.append(dist_h)
    print(f'Matriz para {n} cidades:')
    print(matriz)
    print(f'{n} cidades (heurística): tempo = {tempos_heuristica[-1]:.4f}s, distância = {dist_h}, rota = {rota_h}')
    plotar_grafo_tsp(matriz, rota=rota_h, title=f"Grafo TSP Heurística - {n} Cidades", nome_arquivo=f"grafo_heuristica_{n}_cidades.png")


# In[81]:


import os
# Criando o diretório para salvar os gráficos, se não existir
if not os.path.exists('graficos'):
    os.makedirs('graficos')

plt.figure(figsize=(8,5))
plt.plot(ns, tempos_heuristica, marker='o', color='orange')
plt.yscale('log')
plt.xlabel('Número de cidades')
plt.ylabel('Tempo de execução (s) [escala log]')
plt.title('Crescimento do tempo de execução (heurística vizinho mais próximo)')
plt.grid(True)
plt.savefig('graficos/grafico_tempo_heuristica.png')
plt.show()


# ### 2. Aplicar a Heuristica 
# 
# Nesta etapa, vamos ler os arquivos .tsp fornecidos (matriz de adjacência superior/inferior) e convertê-los para matriz de adjacência completa.

# #### 2.1 si535.tsp
# 
# Descrição: Instância do TSP com 535 cidades.
# Formato: Matriz de adjacência, apenas a diagonal superior (EDGE_WEIGHT_FORMAT: UPPER_DIAG_ROW).
# Como funciona:
# Os pesos das arestas estão dispostos apenas na parte superior da matriz (incluindo a diagonal principal).
# Para reconstruir a matriz completa, basta preencher a parte inferior com os mesmos valores da superior, pois o grafo é simétrico.
# Uso: Para ler corretamente, utilize um método que leia a diagonal superior e replique os valores para a parte inferior.

# In[82]:


def ler_tsp_diagonal_superior(path):
    import numpy as np
    n = None
    with open(path, 'r') as f:
        for linha in f:
            if linha.startswith("DIMENSION"):
                n = int(linha.split(":")[1].strip())
            if linha.strip() == "EDGE_WEIGHT_SECTION":
                break
        # Lê todos os números da seção, independentemente das quebras de linha
        numeros = []
        for linha in f:
            linha = linha.strip()
            if not linha or not (linha[0].isdigit() or linha[0] == '0'):
                continue
            numeros += list(map(int, linha.split()))
            if len(numeros) >= (n * (n + 1)) // 2:
                break
    if n is None:
        raise ValueError("DIMENSION não encontrada no arquivo.")
    matriz = np.zeros((n, n), dtype=int)
    idx = 0
    for i in range(n):
        for j in range(i, n):
            matriz[i, j] = numeros[idx]
            matriz[j, i] = numeros[idx]
            idx += 1
    return matriz

# Exemplo de uso:
matriz_si535 = ler_tsp_diagonal_superior('data/si535.tsp')
print(matriz_si535.shape)


# #### 2.2 pa561.tsp
# 
# Descrição: Instância do TSP com 561 cidades.
# Formato: Matriz de adjacência, apenas a diagonal inferior (EDGE_WEIGHT_FORMAT: LOWER_DIAG_ROW).
# Como funciona:
# Os pesos das arestas estão dispostos apenas na parte inferior da matriz (incluindo a diagonal principal).
# Para reconstruir a matriz completa, basta preencher a parte superior com os mesmos valores da inferior, pois o grafo é simétrico.
# Uso: Para ler corretamente, utilize um método que leia a diagonal inferior e replique os valores para a parte superior.

# In[83]:


def ler_tsp_diagonal_inferior(path):
    import numpy as np
    n = None
    with open(path, 'r') as f:
        for linha in f:
            if linha.startswith("DIMENSION"):
                n = int(linha.split(":")[1].strip())
            if linha.strip() == "EDGE_WEIGHT_SECTION":
                break
        # Lê todos os números da seção, independentemente das quebras de linha
        numeros = []
        for linha in f:
            linha = linha.strip()
            if not linha or not (linha[0].isdigit() or linha[0] == '0'):
                continue
            numeros += list(map(int, linha.split()))
            if len(numeros) >= (n * (n + 1)) // 2:
                break
    if n is None:
        raise ValueError("DIMENSION não encontrada no arquivo.")
    matriz = np.zeros((n, n), dtype=int)
    idx = 0
    for i in range(n):
        for j in range(i + 1):
            matriz[i, j] = numeros[idx]
            matriz[j, i] = numeros[idx]
            idx += 1
    return matriz

# Exemplo de uso:
matriz_pa561 = ler_tsp_diagonal_inferior('data/pa561.tsp')
print(matriz_pa561.shape)


# #### 2.3 si1032.tsp
# 
# Descrição: Instância do TSP com 1032 cidades.
# Formato: Matriz de adjacência, apenas a diagonal superior (EDGE_WEIGHT_FORMAT: UPPER_DIAG_ROW).
# Como funciona:
# Igual ao arquivo si535.tsp, os pesos estão apenas na parte superior da matriz.
# Para reconstruir a matriz completa, replique os valores para a parte inferior.
# Uso: Use o mesmo método de leitura da diagonal superior.
# 

# In[73]:


def ler_tsp_diagonal_superior(path):
    import numpy as np
    n = None
    with open(path, 'r') as f:
        for linha in f:
            if linha.startswith("DIMENSION"):
                n = int(linha.split(":")[1].strip())
            if linha.strip() == "EDGE_WEIGHT_SECTION":
                break
        # Lê todos os números da seção, independentemente das quebras de linha
        numeros = []
        for linha in f:
            linha = linha.strip()
            if not linha or not (linha[0].isdigit() or linha[0] == '0'):
                continue
            numeros += list(map(int, linha.split()))
            if len(numeros) >= (n * (n + 1)) // 2:
                break
    if n is None:
        raise ValueError("DIMENSION não encontrada no arquivo.")
    matriz = np.zeros((n, n), dtype=int)
    idx = 0
    for i in range(n):
        for j in range(i, n):
            matriz[i, j] = numeros[idx]
            matriz[j, i] = numeros[idx]
            idx += 1
    return matriz

# Exemplo de uso:
matriz_si1032 = ler_tsp_diagonal_superior('data/si1032.tsp')
print(matriz_si1032.shape)  # Deve mostrar (1032, 1032)


# #### 3. Aplicação da Heurística nas Instâncias
# 
# Aplicamos a heurística implementada nas três instâncias reais e calculamos as rotas.

# In[74]:


matriz_si535 = ler_tsp_diagonal_superior('data/si535.tsp')
matriz_pa561 = ler_tsp_diagonal_inferior('data/pa561.tsp')
matriz_si1032 = ler_tsp_diagonal_superior('data/si1032.tsp')

# Calculando as rotas e distâncias
resultados = {}
resultados['si535'] = tsp_vizinho_mais_proximo(matriz_si535)
resultados['pa561'] = tsp_vizinho_mais_proximo(matriz_pa561)
resultados['si1032'] = tsp_vizinho_mais_proximo(matriz_si1032)

# Agora você pode exibir os resultados
for nome, (rota, dist) in resultados.items():
    print(f'Instância {nome}: distância encontrada pela heurística = {dist}')

