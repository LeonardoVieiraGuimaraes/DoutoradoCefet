# Buscas em Grafos

Este módulo reúne algoritmos de exploração em grafos, começando pela Busca em Largura (BFS).

## Conteúdo
- 01_busca_em_largura_bfs.ipynb — Definição, propriedades, implementação com fila, prova de correção (intuitiva), reconstrução de caminhos e análise de complexidade O(|V|+|E|). Inclui exemplos com grafos não dirigidos e dirigidos, visualizações e um experimento simples de contagem de operações.
- 02_exercicios_bfs.ipynb — Soluções dos exercícios: camadas (níveis) por listas, floresta BFS (grafos desconexos), teste de bipartição (2-coloração), alcançáveis em digrafo e comparação de distâncias com NetworkX.

## Pré-requisitos
- Python 3.10+ com ambiente gerenciado via `uv` (conforme raiz do projeto)
- Pacotes: `networkx`, `matplotlib`, `numpy`, `jupyter`

## Como usar
1. Abra o notebook no VS Code ou Jupyter e execute as células sequencialmente.
2. Ajuste a semente ou o grafo de exemplo para testar outros cenários.

## Exercícios sugeridos
- Estenda a BFS para grafos desconexos (floresta BFS).
- Verifique bipartição com BFS (2-coloração) e destaque os conjuntos.
- Compare seus resultados com `nx.shortest_path_length` e discuta diferenças.

## Referências
- Cormen, Leiserson, Rivest, Stein — Introduction to Algorithms (Cap. 22)
- Bondy & Murty — Graph Theory
- Sedgewick & Wayne — Algorithms
