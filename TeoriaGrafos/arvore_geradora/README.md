# Árvore Geradora e Árvore Geradora Mínima

Este módulo apresenta o conceito de Árvore Geradora (Spanning Tree) e, em seguida, a Árvore Geradora Mínima (AGM / MST) com algoritmos clássicos.

## Conteúdo
- 01_arvore_geradora_spanning_tree.ipynb — Definição, propriedades (|E|=|V|−1), obtenção via BFS/DFS e remoção de ciclos, exemplos e visualizações.
- 02_agm_mst.ipynb — Definições de peso, implementação de Kruskal (Union-Find) e Prim (heap), verificação com NetworkX, análise de complexidade e exercícios.
- 03_agm_algoritmos_teoria.ipynb — Aplicação, algoritmo genérico (guloso), cortes, arestas seguras (teorema da aresta leve), derivação de Prim e Kruskal, validações e exercícios.

## Pré-requisitos
- Python 3.10+ com ambiente via `uv`
- Pacotes: `networkx`, `matplotlib`, `jupyter`, `numpy`

## Como usar
1. Abra os notebooks acima e execute as células em ordem.
2. Edite os exemplos para explorar diferentes grafos e pesos.

## Referências
- Cormen, Leiserson, Rivest, Stein — Introduction to Algorithms (Cap. 23)
- Sedgewick & Wayne — Algorithms
- Bondy & Murty — Graph Theory
