# Prática 01 — SSSP (Dijkstra vs Heurística Gulosa)

Este diretório contém:
- `graph_io.py` — utilitários para ler grafos de arquivos e gerar grafos completos.
- `dijkstra_impl.py` — implementação de Dijkstra com contagem de comparações de relaxamento.
- `greedy_impl.py` — heurística gulosa baseada na menor aresta saindo do conjunto alcançado (para comparação).
- `run_experiments.py` — script para rodar benchmarks e aplicar nas instâncias fornecidas.

## Requisitos
- Python 3.10+
- Pacotes: `matplotlib` (apenas para os gráficos). Se não quiser plotar, você pode usar apenas o subcomando `instance`.

## Como usar

1) Rodar em grafos completos pequenos (cuidado: O(n^2) memória):

pwsh
python praticas/pratica01/run_experiments.py bench --nmax 200 --step 10

Irá exibir e plotar as comparações de Dijkstra vs Greedy conforme n.

2) Rodar em uma instância de arquivo (ex.: `10000.txt`):

pwsh
python praticas/pratica01/run_experiments.py instance praticas/pratica01/10000.txt --origin 0

Saída esperada: número de comparações para Dijkstra e para a heurística.

Observações:
- As instâncias fornecidas no Moodle usam o formato:
  - 1a linha: n (vértices)
  - 2a linha: m (arestas)
  - linhas seguintes: `u v w` (índices inteiros base-0 e peso real positivo)
- `10000.txt` já contém arestas em ambos os sentidos; ao ler usamos `directed=True` para não duplicar.
- Para a instância com ~1 milhão de vértices, a leitura é factível em máquina com memória suficiente; o script imprime apenas as contagens.
