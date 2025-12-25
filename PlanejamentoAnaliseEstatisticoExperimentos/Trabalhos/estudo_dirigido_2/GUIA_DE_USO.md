# 🎯 GUIA DE USO - ESTUDO DIRIGIDO 2

## Visão Geral

Este projeto contém toda a implementação do **Estudo Dirigido 2** sobre **Planejamento e Análise de Experimentos**. Está dividido em **2 Notebooks Jupyter** que trabalham em sinergia:

- **Parte 1**: Implementação e execução dos 4 experimentos
- **Parte 2**: Geração de tabelas LaTeX a partir dos resultados

---

## 🚀 Início Rápido (3 passos)

### Passo 1: Executar Parte 1
```bash
cd d:\GitHub\DoutoradoCefet\...\estudo_dirigido_2
.venv\Scripts\python executar_parte1.py
```

**Resultado**: 8 arquivos CSV + gráficos PNG

### Passo 2: Executar Parte 2
```bash
.venv\Scripts\python executar_parte2.py
```

**Resultado**: 8 tabelas LaTeX formatadas

### Passo 3: Usar no Relatório
```latex
% No seu .tex principal:
\input{relatorio/resultados/analises/tcl/parametros_tcl.tex}
\input{relatorio/resultados/analises/tcl/resultados_tcl.tex}
% ... repita para os outros experimentos
```

---

## 📋 Experimentos Implementados

### 1. TCL (Teorema Central do Limite)
**Arquivo**: `Parte 1 > Seção 1`

**O que faz**:
- Simula 10.000 amostras de uma distribuição exponencial
- Calcula médias para tamanhos amostrais n=5 e n=50
- Valida o teorema de convergência para a distribuição normal

**Outputs**:
```
relatorio/resultados/parte_1_tcl/
├── parametros_tcl.csv (parâmetros da simulação)
├── analise_tcl_resultados.csv (resultados + cobertura IC)
├── tcl_histograma_populacao.png
├── tcl_histograma_n5.png
└── tcl_histograma_n50.png
```

**Como usar no LaTeX**:
```latex
\section{Teorema Central do Limite}
\input{relatorio/resultados/analises/tcl/parametros_tcl.tex}
\input{relatorio/resultados/analises/tcl/resultados_tcl.tex}
\includegraphics{relatorio/resultados/parte_1_tcl/tcl_histograma_n50.png}
```

---

### 2. One-Way ANOVA
**Arquivo**: `Parte 1 > Seção 2`

**O que faz**:
- Compara 3 tipos de revestimento (A, B, C)
- Realiza análise de variância (ANOVA)
- Executa teste post-hoc de Tukey para comparações pairwise

**Outputs**:
```
relatorio/resultados/parte_2_oneway/
├── parametros_oneway.csv (design da experiência)
├── analise_oneway_resultados.csv (ANOVA + Tukey)
└── oneway_boxplot.png
```

**Como usar no LaTeX**:
```latex
\section{One-Way ANOVA}
\input{relatorio/resultados/analises/oneway/parametros_oneway.tex}
\input{relatorio/resultados/analises/oneway/resultados_oneway.tex}
\includegraphics{relatorio/resultados/parte_2_oneway/oneway_boxplot.png}
```

---

### 3. RCBD (Randomized Complete Block Design)
**Arquivo**: `Parte 1 > Seção 3`

**O que faz**:
- Delineia experimento com blocos (gaiolas como fonte de variação)
- Implementa ANOVA com 3 blocos e 4 tratamentos
- Controla a variabilidade entre blocos

**Outputs**:
```
relatorio/resultados/parte_2_rcbd/
├── parametros_rcbd.csv (design com blocos)
├── analise_rcbd_resultados.csv (ANOVA + efeitos)
└── rcbd_boxplot.png
```

**Como usar no LaTeX**:
```latex
\section{RCBD - Delineamento em Blocos Completos Casualizados}
\input{relatorio/resultados/analises/rcbd/parametros_rcbd.tex}
\input{relatorio/resultados/analises/rcbd/resultados_rcbd.tex}
\includegraphics{relatorio/resultados/parte_2_rcbd/rcbd_boxplot.png}
```

---

### 4. ANOVA Fatorial 2×3
**Arquivo**: `Parte 1 > Seção 4`

**O que faz**:
- Analisa dois fatores: Temperatura (2) e Pressão (3)
- Detecta efeitos principais e de interação
- Gera interaction plot para visualizar relações

**Outputs**:
```
relatorio/resultados/parte_2_fatorial/
├── parametros_fatorial.csv (níveis dos fatores)
├── analise_fatorial_resultados.csv (ANOVA 2-way)
├── fatorial_interaction_plot.png
└── fatorial_boxplot.png
```

**Como usar no LaTeX**:
```latex
\section{ANOVA Fatorial 2×3}
\input{relatorio/resultados/analises/fatorial/parametros_fatorial.tex}
\input{relatorio/resultados/analises/fatorial/resultados_fatorial.tex}
\includegraphics{relatorio/resultados/parte_2_fatorial/fatorial_interaction_plot.png}
\includegraphics{relatorio/resultados/parte_2_fatorial/fatorial_boxplot.png}
```

---

## 📊 Estrutura dos Arquivos Gerados

### CSVs (Dados Brutos)
Todos os CSVs possuem duas colunas:
- **Métrica**: Nome da variável/estatística
- **Valor**: Valor numérico ou string

**Exemplo**:
```csv
Métrica,Valor
Distribuição,Exponencial
Média da População,5
Taxa de Cobertura,0.9315
```

### LaTeX (Tabelas Formatadas)
Cada arquivo .tex contém uma tabela LaTeX completa:
```latex
\begin{table}[H]
\centering
\caption{Parâmetros - TCL}
\label{tab:parametros_tcl}
\begin{tabular}{|l|r|}
\hline
\textbf{Métrica} & \textbf{Valor} \\
\hline
Distribuição & Exponencial \\
...
\hline
\end{tabular}
\end{table}
```

---

## 🔧 Ambiente Virtual

O projeto inclui um `.venv` com todas as dependências. Para ativar:

```bash
# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate
```

**Dependências principais**:
- `scipy` - Testes estatísticos
- `numpy` - Computação numérica
- `pandas` - Manipulação CSV
- `matplotlib` & `seaborn` - Visualização
- `statsmodels` - Modelos estatísticos
- `nbconvert` - Execução notebooks

---

## 📝 Customizações Possíveis

### Alterar Parâmetros da Simulação
Editar a Parte 1 notebook, por exemplo:
```python
# TCL:
SAMPLE_SIZES = [10, 100]  # Mudar de [5, 50]
NUM_SIMULATIONS = 5000    # Mudar de 10000

# One-Way:
N_REPLICATES = 20  # Mudar de 10
```

### Customizar Gráficos
```python
# No notebook, após os gráficos:
plt.figure(figsize=(12, 6))  # Aumentar tamanho
sns.set_style("darkgrid")    # Mudar estilo
```

### Customizar Tabelas LaTeX
Editar manualmente os `.tex` ou alterar o código de geração na Parte 2:
```python
latex_table = """
\\begin{table}[H]
\\centering
\\scriptsize  % Para reduzir tamanho de fonte
"""
```

---

## 🐛 Troubleshooting

### Problema: "ModuleNotFoundError: No module named 'scipy'"
**Solução**:
```bash
.venv\Scripts\pip install -r requirements.txt
```

### Problema: Notebook vazio após execução
**Solução**: Use o script executar_parte1.py que contém lógica robusta:
```bash
.venv\Scripts\python executar_parte1.py
```

### Problema: Gráficos não aparecem
**Solução**: Adicionar ao início do notebook:
```python
%matplotlib inline
import matplotlib.pyplot as plt
```

### Problema: LaTeX não compila
**Solução**: 
- Verificar se `relatorio/` tem estrutura correta
- Tentar comentar `\input` e compilar
- Verificar codificação (UTF-8) dos arquivos

---

## ✨ Boas Práticas

1. **Sempre executar em ordem**: Parte 1 antes de Parte 2
2. **Manter backups**: CSVs são gerados toda vez (sobrescrevem)
3. **Usar paths relativos**: Tudo funciona do diretório do projeto
4. **Validar CSVs**: Sempre checar se dados fazem sentido
5. **Documentar mudanças**: Manter histórico de modificações

---

## 📞 Support

Para dúvidas sobre:
- **Estatística**: Consulte comentários no código
- **Python**: Ver docstrings das funções
- **LaTeX**: Verificar documentação padrão
- **Notebook**: Ler comentários nas células

---

## 📚 Referências

- **TCL**: Teorema Central do Limite - Livros de Probabilidade
- **ANOVA**: Analysis of Variance - Estatística Experimental
- **RCBD**: Delineamento em Blocos - Planejamento de Experimentos
- **Fatorial**: 2k e 3k designs - Otimização de Processos

---

**Última atualização**: 25/12/2025
**Versão**: 1.0
**Status**: ✅ Completo e Testado
