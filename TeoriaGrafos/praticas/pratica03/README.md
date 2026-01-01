# Prática 03 - Teoria dos Grafos: Coloração de Vértices

Este projeto aborda algoritmos de coloração de vértices em grafos, comparando métodos exatos (força bruta) e heurísticos (Greedy e DSATUR) em instâncias sintéticas e reais.

## Estrutura do Projeto

- `coloracao_vertices.ipynb`: Notebook principal com toda a análise, execução dos algoritmos, geração de gráficos e exportação de resultados.
- `instancias/`: Instâncias reais de grafos para teste.
- `resultados/`: Saída dos experimentos (imagens, CSVs, gráficos).
  - `parte_1_forca_bruta/`: Resultados e gráficos da abordagem exata.
  - `parte_2_heuristica/`: Resultados e gráficos das heurísticas.
  - `grafos_individuais/`: Visualização dos grafos completos coloridos.
- `requirements.txt`: Dependências Python do projeto.
- `RESUMO_TRABALHO_REALIZADO.md`: Resumo das etapas e decisões do trabalho.
- `relatorio/`: Relatório em LaTeX e referências (opcional).

## Como Executar

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
2. Abra o notebook `coloracao_vertices.ipynb` no VS Code ou Jupyter.
3. Execute todas as células para gerar os resultados, gráficos e arquivos CSV.

## Principais Funcionalidades

- Geração de grafos aleatórios e leitura de instâncias reais.
- Execução dos algoritmos de coloração:
  - Força Bruta (exato)
  - Greedy (Welsh-Powell)
  - DSATUR
- Comparação de desempenho (tempo e eficiência).
- Visualização dos grafos coloridos e gráficos comparativos.
- Exportação de todos os resultados em CSV e PNG.

## Observações

- Todos os resultados são salvos na pasta `resultados/`.
- Os gráficos de comparação são apresentados em subplots para facilitar a análise visual.
- As arestas dos grafos completos são desenhadas em tom claro para melhor visualização das cores dos vértices.

---

Desenvolvido para a disciplina de Teoria dos Grafos - Doutorado CEFET.
