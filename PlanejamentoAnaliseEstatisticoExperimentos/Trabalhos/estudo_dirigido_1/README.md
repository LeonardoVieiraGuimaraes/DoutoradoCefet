# Estudo Dirigido 1: Teorema Central do Limite e Intervalos de Confiança

## Descrição Geral

Este projeto implementa uma análise numérica do **Teorema Central do Limite (TCL)** e valida a robustez dos **Intervalos de Confiança (IC)** em distribuições assimétricas. O estudo utiliza simulações de Monte Carlo com distribuição Exponencial para demonstrar convergência para a normalidade conforme o tamanho amostral aumenta.

## Estrutura do Projeto

```
estudo_dirigido_1/
├── estudo_dirigido_1.ipynb              # Notebook Jupyter com simulações
├── requirements.txt                     # Dependências Python
├── .gitignore                          # Arquivo para ignorar build LaTeX
├── README.md                           # Este arquivo
└── relatorio/
    └── estudo_dirigido_1/
        ├── relatorio.tex               # Documento LaTeX principal
        ├── referencias.bib             # Referências ABNT NBR 6023:2018
        ├── relatorio.pdf               # PDF compilado
        └── resultados/
            ├── tarefa_1_*.png          # Gráficos das simulações
            ├── tarefa_2_*.png          # Gráficos de cobertura do IC
            ├── analise_*.tex           # Tabelas de resultados (geradas automaticamente)
            ├── tarefa_1_resultados.csv # Dados de assimetria
            └── tarefa_2_resultados.csv # Dados de cobertura
```

## Arquitetura e Fluxo de Trabalho

### 1. **Geração de Dados (Notebook Jupyter)**
```
Setup → Tarefa 1 (TCL) → Salvar Resultados 1 → 
Tarefa 2 (IC) → Salvar Resultados 2 → Gerar Tabelas LaTeX
```

**Fluxo Detalhado:**
- **Setup Inicial**: Configuração centralizada de parâmetros
  - População: Exponencial (λ=0.2, n=100.000)
  - Simulações: 10.000 replicações
  - Amostras: n=5 (pequena) e n=50 (grande)

- **Tarefa 1**: Simulação do TCL
  - Gera distribuições das médias amostrais
  - Calcula coeficientes de assimetria
  - Cria 4 gráficos PNG (população, n=5, n=50, Q-Q plot)
  - Exporta CSV com estatísticas

- **Tarefa 2**: Validação de Cobertura do IC
  - Constrói 10.000 ICs de 95%
  - Verifica se contêm μ=5
  - Cria 2 gráficos (taxa de cobertura, sucesso/falha)
  - Exporta CSV com resultados

- **Geração de Tabelas LaTeX**:
  - Converte dados CSV em tabelas `.tex` formatadas
  - 3 tabelas: assimetria, efeito de n, validação de IC

### 2. **Compilação LaTeX**
```
relatorio.tex + referencias.bib + imagens + tabelas → pdflatex → relatorio.pdf
```

## Componentes Reutilizáveis

### A. **Padrão Jupyter: Setup + Tarefas**

Para projetos estatísticos similares, use esta estrutura:

```python
# Cell 1: Setup Inicial
import numpy as np
from scipy import stats
import pandas as pd

# Parâmetros centralizados
PARAM = {
    'dist': 'exponential',
    'lambda': 0.2,
    'population_size': 100000,
    'simulations': 10000,
    'sample_sizes': [5, 50],
    'confidence_level': 0.95
}

# Cell 2: Tarefa 1 - Análise Distribuição
# código de simulação

# Cell 3: Salvar Resultados 1
# export_to_csv() e export_to_png()

# Cell 4: Tarefa 2 - Validação
# código de validação

# Cell 5: Salvar Resultados 2
# export_to_csv() e export_to_png()

# Cell 6: Gerar Tabelas LaTeX
# converter CSV em LaTeX tables
```

### B. **Padrão LaTeX: ABNT + Modular**

Estrutura reutilizável para relatórios académicos:

**Preamble (Configuração ABNT):**
```latex
\documentclass[12pt,a4paper]{article}
\usepackage[portuguese]{babel}
\usepackage[top=3cm,left=3cm,right=2cm,bottom=2cm]{geometry}
\usepackage{graphicx, amsmath, booktabs, ragged2e}
\usepackage{times, indentfirst}

% Configuração ABNT NBR 14724
\linespread{1.5}           % Espaçamento 1.5
\setlength{\parindent}{1.25cm}  % Parágrafo recuado
\justifying                % Texto justificado
```

**Estrutura de Conteúdo:**
```latex
% Capa
\begin{center}
  % Elementos obrigatórios
  \textbf{INSTITUIÇÃO}
  \textbf{TÍTULO}
  \normalsize Autor
  \textbf{Belo Horizonte - MG \\ 2025}
\end{center}

% Sumário
\tableofcontents

% Seções principais
\section{Introdução}
\section{Fundamentação Teórica}
\section{Metodologia}
\section{Resultados e Discussão}
\section{Conclusão}

% Referências
\bibliographystyle{abntex2-alf}
\bibliography{referencias}
```

### C. **Padrão de Referências: ABNT NBR 6023:2018**

Formato dos arquivos `.bib`:

```bibtex
% Livro
@book{autor_ano,
  author    = {SOBRENOME, Nome and SOBRENOME, Nome},
  title     = {Título do livro},
  edition   = {nª},
  address   = {Cidade},
  publisher = {Editora},
  year      = {YYYY}
}

% Artigo de Periódico
@article{autor_ano,
  author  = {SOBRENOME, Nome},
  title   = {Título do artigo},
  journal = {Nome da Revista},
  volume  = {XX},
  number  = {X},
  pages   = {X--XX},
  year    = {YYYY}
}
```

**Citar no texto:**
```latex
\cite{chave1,chave2}  % (AUTOR ano; AUTOR ano)
```

### D. **Padrão de Métricas Estatísticas**

Para projetos com análises quantitativas:

```latex
\subsubsection{Métrica X}

A métrica X é calculada como:

\begin{equation}
\text{Métrica} = \frac{\text{parte 1}}{\text{parte 2}}
\end{equation}

Interpretações:
\begin{itemize}
  \item Valor > 0: significado
  \item Valor ≈ 0: significado
  \item Valor < 0: significado
\end{itemize}
```

## Métricas Implementadas

### 1. Coeficiente de Assimetria (Skewness)
```
γ = E[(X - μ)/σ]³

Interprets simetria da distribuição
- γ ≈ 0: simétrica
- γ > 0: cauda direita
- γ < 0: cauda esquerda
```

### 2. Taxa de Cobertura do IC
```
Cobertura = (ICs que contêm μ) / (Total de ICs)

Esperado para IC 95%: ~0.95
```

### 3. Redução Relativa de Assimetria
```
Redução(%) = [(γ_original - γ_n) / γ_original] × 100%

Mede velocidade de convergência do TCL
```

## Como Usar em Outros Projetos

### Caso 1: Simulações Estatísticas Similares

**Passos:**
1. Copie o padrão de `Setup → Tarefas → Exportação` do notebook
2. Adapte os parâmetros em `PARAM`
3. Modifique as distribuições (Normal, Uniforme, etc.)
4. Reutilize as funções de exportação (CSV, PNG, LaTeX)

**Exemplo:**
```python
# Para distribuição Normal em vez de Exponencial
PARAM['dist'] = 'normal'
PARAM['mean'] = 100
PARAM['std'] = 15
```

### Caso 2: Relatórios ABNT em LaTeX

**Passos:**
1. Copie `relatorio.tex` como template
2. Mantenha a preamble (ABNT)
3. Adapte seções conforme seu conteúdo
4. Use `\input{arquivo.tex}` para modularizar conteúdo
5. Mantenha arquivo `referencias.bib` em formato ABNT

**Comando de compilação:**
```bash
pdflatex -interaction=nonstopmode relatorio.tex
bibtex relatorio
pdflatex -interaction=nonstopmode relatorio.tex
pdflatex -interaction=nonstopmode relatorio.tex
```

### Caso 3: Integração Jupyter → LaTeX

**Fluxo a replicar:**
1. Gerar dados/gráficos no Jupyter (PNG/CSV)
2. Converter resultados em tabelas LaTeX com Python:
   ```python
   df.to_latex('tabela.tex', index=False, escape=False)
   ```
3. Importar no LaTeX: `\input{tabela.tex}`
4. Incluir imagens: `\includegraphics[width=0.7\textwidth]{imagem.png}`

## Configurações Importantes

### .gitignore
```
*.aux *.log *.bbl *.blg *.synctex.gz  # LaTeX build
*.pdf *.dvi                           # PDFs (opcional)
__pycache__/ *.pyc                    # Python cache
.venv/ venv/                          # Ambientes virtuais
```

### requirements.txt
```
numpy>=1.24.0
scipy>=1.10.0
pandas>=2.0.0
matplotlib>=3.7.0
seaborn>=0.12.0
jupyter>=1.0.0
```

## Boas Práticas Implementadas

✅ **Separação de Conceitos**: Setup centralizado vs. Tarefas específicas
✅ **Modularização**: Arquivos `.tex` separados para tabelas
✅ **Documentação**: Seção de métricas explica cálculos
✅ **ABNT Compliance**: Referências formatadas, margens corretas, espaçamento 1.5
✅ **Sem Overfull Hbox**: Texto justificado e bem quebrado
✅ **Rastreabilidade**: CSV exportados com todos os dados
✅ **Reprodutibilidade**: Parâmetros fixos permitem replicação

## Próximas Iterações / Melhorias Possíveis

- [ ] Adicionar análise de intervalo de confiança para mediana (bootstrap)
- [ ] Comparar múltiplas distribuições (Normal, Poisson, etc.)
- [ ] Gráficos interativos com Plotly
- [ ] Testes de hipótese estatísticos
- [ ] Análise de sensibilidade de parâmetros

## Autor

Leonardo Vieira Guimarães

## Data de Conclusão

16 de dezembro de 2025

## Licença

Documento académico - CEFET-MG

---

**Nota**: Este projeto pode servir como template para outras disciplinas do programa de Pós-Graduação em Educação Profissional e Tecnológica.
