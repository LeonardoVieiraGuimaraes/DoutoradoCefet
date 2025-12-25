# Estudo Dirigido 2: Planejamento e Análise de Experimentos

Este projeto está dividido em **dois notebooks Jupyter principais**:

## 📊 Estrutura dos Notebooks

### 1️⃣ **Parte 1: Implementação dos Experimentos**
Arquivo: `estudos_dirigidos_2_parte1_implementacao.ipynb`

**Objetivo**: Implementar 4 estudos estatísticos de planejamento e análise de experimentos

**Experimentos implementados**:

1. **TCL (Teorema Central do Limite)**
   - Valida o TCL usando população assimétrica (exponencial)
   - Gera 10.000 simulações com diferentes tamanhos de amostra (n=5, n=50)
   - **Outputs**:
     - CSVs: `parametros_tcl.csv`, `analise_tcl_resultados.csv`
     - Gráficos: 3 histogramas (população, n=5, n=50) com labels de assimetria

2. **One-Way ANOVA**
   - Compara 3 revestimentos (A, B, C) com teste post-hoc de Tukey
   - Análise de 30 observações (3 grupos × 10 repetições)
   - **Outputs**:
     - CSVs: `parametros_oneway.csv`, `analise_oneway_resultados.csv`
     - Gráficos: 1 boxplot com grupos de revestimento

3. **RCBD (Randomized Complete Block Design)**
   - Controla variabilidade entre blocos (gaiolas) com 3 blocos e 4 tratamentos
   - Análise de 12 observações com efeito de bloco
   - **Outputs**:
     - CSVs: `parametros_rcbd.csv`, `analise_rcbd_resultados.csv`
     - Gráficos: 1 boxplot com colora ção de blocos

4. **ANOVA Fatorial**
   - Analisa interação entre Temperatura (2 níveis) × Pressão (3 níveis)
   - 30 observações (2×3×5 repetições)
   - **Outputs**:
     - CSVs: `parametros_fatorial.csv`, `analise_fatorial_resultados.csv`
     - Gráficos: Interaction plot + boxplot

**Como executar**:
```bash
cd estudo_dirigido_2
.venv\Scripts\python executar_parte1.py
```

---

### 2️⃣ **Parte 2: Geração de Tabelas LaTeX**
Arquivo: `estudos_dirigidos_2_parte2_latex.ipynb`

**Objetivo**: Gerar tabelas LaTeX profissionais a partir dos CSV gerados na Parte 1

**Estrutura de saída**:
```
relatorio/resultados/analises/
├── tcl/
│   ├── parametros_tcl.tex
│   └── resultados_tcl.tex
├── oneway/
│   ├── parametros_oneway.tex
│   └── resultados_oneway.tex
├── rcbd/
│   ├── parametros_rcbd.tex
│   └── resultados_rcbd.tex
└── fatorial/
    ├── parametros_fatorial.tex
    └── resultados_fatorial.tex
```

**Como executar**:
```bash
cd estudo_dirigido_2
.venv\Scripts\python executar_parte2.py
```

---

## 📁 Estrutura de Arquivos

```
estudo_dirigido_2/
├── estudos_dirigidos_2_parte1_implementacao.ipynb    # Notebook Part 1
├── estudos_dirigidos_2_parte2_latex.ipynb            # Notebook Part 2
├── executar_parte1.py                                 # Script para executar Part 1
├── executar_parte2.py                                 # Script para executar Part 2
├── relatorio/
│   └── resultados/
│       ├── parte_1_tcl/                              # CSVs do TCL
│       ├── parte_2_oneway/                           # CSVs do One-Way
│       ├── parte_2_rcbd/                             # CSVs do RCBD
│       ├── parte_2_fatorial/                         # CSVs do Fatorial
│       └── analises/                                 # LaTeX tables (Part 2)
│           ├── tcl/
│           ├── oneway/
│           ├── rcbd/
│           └── fatorial/
└── .venv/                                             # Ambiente virtual Python
```

---

## 🛠️ Ambiente Virtual

O projeto utiliza um ambiente virtual Python com as seguintes dependências:

```
scipy
numpy
pandas
matplotlib
seaborn
statsmodels
nbconvert
jupyter
```

**Ativar ambiente**:
```bash
.venv\Scripts\activate
```

---

## 📝 Fluxo de Trabalho Recomendado

1. **Executar Parte 1**:
   ```bash
   python executar_parte1.py
   ```
   Isso gera 8 arquivos CSV com parâmetros e resultados de todos os 4 experimentos.

2. **Executar Parte 2**:
   ```bash
   python executar_parte2.py
   ```
   Isso lê os 8 CSVs e gera 8 tabelas LaTeX.

3. **Integrar LaTeX no Relatório**:
   - Usar `\input{relatorio/resultados/analises/<experimento>/<parametros|resultados>_<nome>.tex}`
   - Exemplo: `\input{relatorio/resultados/analises/tcl/parametros_tcl.tex}`

---

## 📊 Outputs Finais

### Parte 1: CSVs + Gráficos
- **8 arquivos CSV** com parâmetros e resultados
- **Gráficos em PNG**: histogramas, boxplots, interaction plots

### Parte 2: Tabelas LaTeX
- **8 arquivos .tex** com tabelas formatadas
- Cada arquivo contém uma tabela LaTeX completa e pronta para usar

---

## ✅ Status de Conclusão

- [x] TCL: Implementação + CSVs + Histogramas
- [x] One-Way ANOVA: Implementação + CSVs + Boxplot
- [x] RCBD: Implementação + CSVs + Boxplot
- [x] ANOVA Fatorial: Implementação + CSVs + Gráficos
- [x] Geração de 8 tabelas LaTeX
- [x] Estrutura de diretórios criada

---

**Última atualização**: 25 de dezembro de 2025
