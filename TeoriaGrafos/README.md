# 📚 Teoria dos Grafos - Material Didático

Este repositório contém material completo de **Teoria dos Grafos** com:
- ✅ **6 Jupyter Notebooks** organizados por temas
- ✅ Exemplos práticos usando **NetworkX**
- ✅ Visualizações interativas com **Matplotlib**
- ✅ Exercícios e problemas clássicos
- ✅ Configurado com **uv** para gerenciamento rápido de dependências

---

## 📖 Conteúdo

### Notebooks (pasta `terminologia/`)

1. **[Introdução e Motivação](terminologia/01_introducao_motivacao.ipynb)** - O que são grafos e por que estudá-los
2. **[Terminologia Básica](terminologia/02_terminologia.ipynb)** - Adjacência, incidência, laços, subgrafos
3. **[Tipos de Grafos](terminologia/03_tipos_grafos.ipynb)** - Simples, direcionados, completos, ciclo, roda
4. **[Grafos Especiais](terminologia/04_grafos_especiais.ipynb)** - Bipartidos, ponderados, planares, multigrafos
5. **[Grau e Teoremas](terminologia/05_grau_teoremas.ipynb)** - Teorema do Aperto de Mãos, grafos regulares
6. **[Problema de Königsberg](terminologia/06_konigsberg.ipynb)** 🌉 - O problema clássico de Euler

📚 [**Ver índice completo dos notebooks →**](terminologia/README.md)

---

## 🧭 Outros módulos do repositório

- 📦 [Representações de Grafos](representacoes/README.md)
- 🌲 [Árvores](arvores/README.md)
- 🔎 [Buscas (BFS)](buscas/README.md)
- 🌉 [Árvore Geradora e AGM](arvore_geradora/README.md)
- 🛣️ [Caminhos Mínimos (Bellman-Ford e Dijkstra)](caminhos_minimos/README.md)

Esses módulos seguem o mesmo padrão didático: teoria, implementação em Python/NetworkX, visualizações e exercícios.

---

## 🚀 Início Rápido

### 1️⃣ Instalação com uv (recomendado)

O [uv](https://docs.astral.sh/uv/) é um gerenciador ultra-rápido de Python e dependências:

```powershell
# Instalar uv (Windows/PowerShell)
irm https://astral.sh/uv/install.ps1 | iex

# Instalar todas as dependências
uv sync

# Iniciar Jupyter Notebook
uv run jupyter notebook
```

### 2️⃣ Alternativa: pip tradicional

```powershell
# Criar ambiente virtual
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Instalar dependências
pip install networkx matplotlib jupyter numpy

# Iniciar Jupyter
jupyter notebook
```

---

## 📦 Dependências

As seguintes bibliotecas são instaladas automaticamente:

- **NetworkX** 3.5 - Criação e análise de grafos
- **Matplotlib** 3.10.7 - Visualização
- **Jupyter** Lab 4.4.10 - Ambiente de notebooks
- **NumPy** 2.3.4 - Computação numérica

---

## 🎯 Ordem de Estudo Recomendada

```
1. Introdução → 2. Terminologia → 3. Tipos → 4. Especiais → 5. Teoremas → 6. Königsberg
```

Cada notebook é independente, mas segue uma progressão lógica de dificuldade.

---

## 💡 Como Usar os Notebooks

1. **Abra o Jupyter**:
   ```powershell
   uv run jupyter notebook
   ```

2. **Navegue até `terminologia/`**

3. **Comece pelo notebook 1** e execute todas as células (Shift+Enter)

4. **Modifique os exemplos** para experimentar!

---

## 🔧 Comandos Úteis com uv

```powershell
# Instalar nova dependência
uv add <pacote>

# Atualizar dependências
uv sync --upgrade

# Executar Python
uv run python script.py

# Executar Jupyter Lab (interface moderna)
uv run jupyter lab

# Ver versão do Python em uso
uv run python --version
```

---

## 📁 Estrutura do Projeto

```
TeoriaGrafos/
├── terminologia/
│   ├── README.md                      # 📚 Índice dos notebooks
│   ├── 01_introducao_motivacao.ipynb  # Introdução
│   ├── 02_terminologia.ipynb          # Terminologia básica
│   ├── 03_tipos_grafos.ipynb          # Tipos de grafos
│   ├── 04_grafos_especiais.ipynb      # Grafos especiais
│   ├── 05_grau_teoremas.ipynb         # Graus e teoremas
│   └── 06_konigsberg.ipynb            # Problema clássico 🌉
├── src/
│   └── teoriagrafos/                  # Pacote Python (opcional)
├── pyproject.toml                      # Configuração uv/pip
├── uv.lock                            # Lock file (gerado automaticamente)
└── README.md                          # Este arquivo
```

---

## 🎓 Tópicos Cobertos

### Conceitos Fundamentais
- ✅ Definição de grafos G = (V, E)
- ✅ Vértices e arestas
- ✅ Adjacência e incidência
- ✅ Laços e arestas paralelas
- ✅ Subgrafos

### Tipos de Grafos
- ✅ Grafos simples
- ✅ Grafos direcionados (digrafos)
- ✅ Grafos completos (Kₙ)
- ✅ Grafos ciclo (Cₙ)
- ✅ Grafos roda (Wₙ)

### Grafos Especiais
- ✅ Grafos bipartidos (K_{m,n})
- ✅ Multigrafos
- ✅ Grafos ponderados
- ✅ Grafos planares (K₅, K₃,₃)

### Teoremas e Problemas
- ✅ Grau de vértices
- ✅ Teorema do Aperto de Mãos (Handshaking Theorem)
- ✅ Grafos regulares
- ✅ **Problema das 7 Pontes de Königsberg** (Euler, 1736)
- ✅ Caminhos e ciclos Eulerianos

---

## 🌐 Recursos Adicionais

- 📖 [Documentação NetworkX](https://networkx.org/documentation/stable/)
- 📺 [3Blue1Brown - Discrete Math](https://www.youtube.com/c/3blue1brown)
- 📚 Livro: "Introduction to Graph Theory" - Douglas West
- 🎓 [Coursera: Graph Theory](https://www.coursera.org/learn/graphs)

---

## 🤝 Contribuições

Este material é educacional e está em constante evolução. Contribuições são bem-vindas:

- 🐛 Reporte bugs
- 💡 Sugira melhorias
- ✍️ Adicione exemplos
- 📝 Corrija erros

---

## 📄 Licença

MIT License - Livre para uso educacional

---

## 🎉 Pronto para Começar?

```powershell
uv run jupyter notebook
```

Abra `terminologia/01_introducao_motivacao.ipynb` e boa jornada! 🚀

---

## ⚙️ Detalhes Técnicos do uv

### Por que usar uv?

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