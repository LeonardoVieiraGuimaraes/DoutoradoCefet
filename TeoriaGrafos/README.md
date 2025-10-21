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

## Usando uv (opção mais rápida para Python) 🐍⚡

O [uv](https://docs.astral.sh/uv/) é um gerenciador/instalador de Python e dependências muito rápido. Abaixo um fluxograma de uso no Windows (PowerShell):

1) Instalar o uv

```powershell
# Método recomendado
irm https://astral.sh/uv/install.ps1 | iex

# Alternativa com Invoke-WebRequest
Invoke-WebRequest https://astral.sh/uv/install.ps1 -UseBasicParsing | Invoke-Expression
```

Feche e reabra o PowerShell após instalar.

2) Instalar uma versão do Python (opcional, o uv pode usar a sua atual)

```powershell
uv python install 3.12
```

3) Criar/sincronizar o ambiente do projeto (este repositório já tem `pyproject.toml`)

```powershell
# Cria uma venv local .venv (opcional, mas recomendado)
uv venv .venv

# Instala as dependências do projeto declaradas no pyproject (e gera uv.lock)
uv sync
```

4) Executar o pacote

```powershell
# Executa o ponto de entrada do pacote (src/teoriagrafos/__main__.py)
uv run -m teoriagrafos
```

5) Adicionar dependências (ex.: networkx, matplotlib, pytest)

```powershell
uv add networkx matplotlib pytest

# Rodar testes com a ferramenta instalada via uvx
uvx pytest -q
```

Notas uv

- `uv sync` lê `pyproject.toml` e mantém o ambiente reproduzível via `uv.lock`.
- `uv run` executa comandos usando o ambiente resolvido/sincronizado (sem precisar ativar a venv manualmente).
- `uvx <tool>` executa CLIs temporários (ex.: `uvx ruff`, `uvx black`, `uvx pytest`).
- Para remover o ambiente local, apague a pasta `.venv/` e o arquivo `uv.lock` se desejar refazer o lock.