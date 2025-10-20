# Representações de Grafos — Matrizes e Listas

Este repositório contém implementações didáticas de representações de grafos em Python:

- `representacoes_grafos.py` — implementação de:
  - `Aresta` (dataclass)
  - `GrafoMatriz` (matriz de adjacência)
  - `GrafoLista` (lista de adjacência)
  - utilitários de conversão e visualização (`matriz_para_lista`, `lista_para_matriz`, `desenha_grafo_de_lista`)

- `representacoes_grafos.ipynb` — notebook com explicações, exemplos e visualizações.
- `test_grafos.py` e `test_grafos_extra.py` — testes pytest.

Como usar (Windows / PowerShell)

1. Criar e ativar um ambiente virtual (recomendado):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Instalar dependências:

```powershell
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install networkx matplotlib pytest
```

3. Rodar os testes:

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

4. Abrir e executar o notebook `representacoes_grafos.ipynb` no VS Code ou Jupyter.

Notas

- As implementações são direcionadas (cada aresta é armazenada como v1 -> v2). Se precisar de versão não direcionada, me avise que eu adapto.
- A visualização com `networkx` e `matplotlib` é opcional; instale as bibliotecas acima para usar as funções de plot.

Contato

Se quiser que eu crie um PR com essas mudanças, ou adicione suporte a grafos não direcionados, me diga e eu faço os commits e abro uma branch.