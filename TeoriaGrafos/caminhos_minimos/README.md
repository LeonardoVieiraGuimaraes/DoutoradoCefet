# Caminhos Mínimos — Bellman-Ford

Este módulo cobre caminhos mínimos de origem única em digrafos ponderados com arestas negativas, via o algoritmo de Bellman-Ford.

## Conteúdo
- 01_bellman_ford.ipynb — Definições, sub-estrutura ótima, relaxamento, inicialização, detecção de ciclo negativo, reconstrução de caminhos, exemplos, visualização e complexidade O(|V||E|).
- 02_exercicios_bellman_ford.ipynb — Práticas com parada antecipada, geração de instâncias, validação com NetworkX e detecção de ciclo negativo.
- 03_dijkstra.ipynb — Teoria e prática do algoritmo de Dijkstra (pesos não negativos), heap (fila de prioridade), árvore de caminhos mínimos e complexidade O(|E| log |V|).
- 04_exercicios_dijkstra.ipynb — Exercícios: comparação com Bellman-Ford (em grafos sem negativos), contagem de operações no heap, casos inalcançáveis e reconstrução de caminhos.

## Pré-requisitos
- Python 3.10+ com `uv`
- Pacotes: `networkx`, `matplotlib`, `numpy`, `jupyter`

## Como usar
1. Abra os notebooks e execute as células em ordem.
2. Ajuste grafos e pesos para explorar mais casos (com e sem ciclos negativos).

## Referências
- Cormen, Leiserson, Rivest, Stein — Introduction to Algorithms (Cap. 24)
- Sedgewick & Wayne — Algorithms
- Bondy & Murty — Graph Theory
