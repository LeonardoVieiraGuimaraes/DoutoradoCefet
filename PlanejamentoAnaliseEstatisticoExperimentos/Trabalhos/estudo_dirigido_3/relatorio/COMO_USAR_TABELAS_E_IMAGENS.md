# 📚 Como Usar Tabelas LaTeX e Imagens no Relatório

Guia rápido para incorporar as tabelas e imagens geradas automaticamente ao seu arquivo `relatorio.tex`.

---

## 📁 Estrutura de Arquivos

```
relatorio/
├── relatorio.tex              ← Arquivo principal do relatório
├── tabelas_latex/             ← 9 tabelas em formato LaTeX
│   ├── tab_01_01_Parametros_Metodologia.tex
│   ├── tab_02_02_Estatisticas_Descritivas.tex
│   ├── tab_03_02_Estatisticas_por_mes.tex
│   ├── tab_04_03_TCL_validacao.tex
│   ├── tab_05_04_IC_por_ano.tex
│   ├── tab_06_04_IC_por_mes.tex
│   ├── tab_07_05_ANOVA_fatorial_efeitos.tex
│   ├── tab_08_06_Arquivos_Gerados.tex
│   └── tab_09_06_Resumo_Executivo.tex
├── img/                       ← 5 imagens organizadas por tema
│   ├── 02_Estatisticas_Descritivas/
│   │   └── 02_Distribuicao_Original.png
│   ├── 03_Teorema_Central_Limite/
│   │   └── 03_TCL_distribuicao_original.png
│   ├── 04_Intervalos_Confianca/
│   │   ├── 04_IC_por_ano_grafico.png
│   │   └── 04_IC_por_mes_grafico.png
│   └── 05_ANOVA_Fatorial/
│       └── 05_Boxplot_quantidade_por_mes.png
└── INDICE_TABELAS_E_IMAGENS.txt  ← Referência de comandos
```

---

## 🔹 Como Incluir as Tabelas

### Opção 1: Incluir tabela específica

No seu arquivo `relatorio.tex`, onde deseja inserir uma tabela, use:

```latex
\input{relatorio/tabelas_latex/tab_01_01_Parametros_Metodologia.tex}
```

### Opção 2: Incluir todas as tabelas

Crie uma seção no seu relatório:

```latex
\section{Tabelas de Resultados}

% Tabela 1: Parâmetros e Metodologia
\input{relatorio/tabelas_latex/tab_01_01_Parametros_Metodologia.tex}

% Tabela 2: Estatísticas Descritivas
\input{relatorio/tabelas_latex/tab_02_02_Estatisticas_Descritivas.tex}

% Tabela 3: Estatísticas por Mês
\input{relatorio/tabelas_latex/tab_03_02_Estatisticas_por_mes.tex}

% Tabela 4: Validação TCL
\input{relatorio/tabelas_latex/tab_04_03_TCL_validacao.tex}

% Tabela 5: IC por Ano
\input{relatorio/tabelas_latex/tab_05_04_IC_por_ano.tex}

% Tabela 6: IC por Mês
\input{relatorio/tabelas_latex/tab_06_04_IC_por_mes.tex}

% Tabela 7: ANOVA Fatorial Efeitos
\input{relatorio/tabelas_latex/tab_07_05_ANOVA_fatorial_efeitos.tex}

% Tabela 8: Arquivos Gerados
\input{relatorio/tabelas_latex/tab_08_06_Arquivos_Gerados.tex}

% Tabela 9: Resumo Executivo
\input{relatorio/tabelas_latex/tab_09_06_Resumo_Executivo.tex}
```

---

## 🔹 Como Incluir as Imagens

### Opção 1: Incluir imagem específica

```latex
\begin{figure}[H]
    \centering
    \includegraphics[width=0.9\textwidth]{relatorio/img/02_Estatisticas_Descritivas/02_Distribuicao_Original.png}
    \caption{Distribuição Original dos Bovinos por GTA}
    \label{fig:distribuicao_original}
\end{figure}
```

### Opção 2: Incluir todas as imagens

```latex
\section{Figuras e Gráficos}

% Gráfico 1: Distribuição Original
\begin{figure}[H]
    \centering
    \includegraphics[width=0.9\textwidth]{relatorio/img/02_Estatisticas_Descritivas/02_Distribuicao_Original.png}
    \caption{Distribuição Original - Histograma, Q-Q Plot e Boxplot}
    \label{fig:distribuicao_original}
\end{figure}

% Gráfico 2: Teorema Central do Limite
\begin{figure}[H]
    \centering
    \includegraphics[width=0.9\textwidth]{relatorio/img/03_Teorema_Central_Limite/03_TCL_distribuicao_original.png}
    \caption{Teorema Central do Limite - Distribuição das Médias Amostrais}
    \label{fig:tcl_distribuicao}
\end{figure}

% Gráfico 3: IC por Ano
\begin{figure}[H]
    \centering
    \includegraphics[width=0.9\textwidth]{relatorio/img/04_Intervalos_Confianca/04_IC_por_ano_grafico.png}
    \caption{Intervalos de Confiança 95\% - Por Ano}
    \label{fig:ic_ano}
\end{figure}

% Gráfico 4: IC por Mês
\begin{figure}[H]
    \centering
    \includegraphics[width=0.9\textwidth]{relatorio/img/04_Intervalos_Confianca/04_IC_por_mes_grafico.png}
    \caption{Intervalos de Confiança 95\% - Por Mês}
    \label{fig:ic_mes}
\end{figure}

% Gráfico 5: ANOVA - Boxplot
\begin{figure}[H]
    \centering
    \includegraphics[width=0.9\textwidth]{relatorio/img/05_ANOVA_Fatorial/05_Boxplot_quantidade_por_mes.png}
    \caption{Distribuição por Mês - ANOVA Fatorial}
    \label{fig:boxplot_mes}
\end{figure}
```

---

## ⚙️ Requisitos do Pacote LaTeX

Para que as tabelas e imagens sejam renderizadas corretamente, certifique-se de que seu arquivo `relatorio.tex` contém os seguintes pacotes no preâmbulo:

```latex
\documentclass[12pt]{report}

% ... outros pacotes ...

% Pacotes necessários para tabelas e imagens
\usepackage[utf-8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[portuguese]{babel}
\usepackage{graphicx}                    % Para incluir imagens
\usepackage{float}                       % Para figura/tabela em [H]
\usepackage{booktabs}                    % Melhor formatação de tabelas
\usepackage{array}                       % Tratamento avançado de tabelas
\usepackage{xcolor}                      % Cores nas tabelas

\begin{document}
% ... seu conteúdo ...
\end{document}
```

---

## 🔧 Compilação

### Via Terminal

**Opção 1: pdflatex (uma única passagem)**
```bash
pdflatex relatorio.tex
```

**Opção 2: latexmk (compilação automática com múltiplas passagens)**
```bash
latexmk -pdf relatorio.tex
```

**Opção 3: pdflatex com múltiplas passagens**
```bash
pdflatex relatorio.tex
pdflatex relatorio.tex
pdflatex relatorio.tex
```

### Via VS Code

1. Abra `relatorio.tex` no VS Code
2. Use a extensão "LaTeX Workshop"
3. Clique em "Build LaTeX project" ou pressione `Ctrl+Alt+B`

---

## 💡 Dicas Importantes

### ✅ Referências Cruzadas

Use as labels automáticas para referenciar tabelas e figuras:

```latex
% Referência a tabela
Ver \ref{tab:01_01_Parametros_Metodologia} na página \pageref{tab:01_01_Parametros_Metodologia}.

% Referência a figura
A \autoref{fig:distribuicao_original} mostra...
```

### ✅ Escala e Posicionamento

Ajuste a largura das imagens conforme necessário:

```latex
% Imagem em 100% da largura do texto
\includegraphics[width=\textwidth]{...}

% Imagem em 80% da largura
\includegraphics[width=0.8\textwidth]{...}

% Imagem com altura específica
\includegraphics[height=6cm]{...}
```

### ✅ Subcaptions

Para agrupar múltiplas imagens, use subcaptions:

```latex
\usepackage{subcaption}

\begin{figure}[H]
    \centering
    \begin{subfigure}{0.45\textwidth}
        \centering
        \includegraphics[width=\textwidth]{relatorio/img/02_Estatisticas_Descritivas/02_Distribuicao_Original.png}
        \caption{Distribuição Original}
    \end{subfigure}
    \hfill
    \begin{subfigure}{0.45\textwidth}
        \centering
        \includegraphics[width=\textwidth]{relatorio/img/03_Teorema_Central_Limite/03_TCL_distribuicao_original.png}
        \caption{TCL}
    \end{subfigure}
    \caption{Análises Estatísticas}
    \label{fig:analises}
\end{figure}
```

---

## 📖 Arquivo de Índice

Um arquivo `INDICE_TABELAS_E_IMAGENS.txt` foi criado com todos os comandos prontos para copiar e colar. Consulte este arquivo como referência rápida.

---

## ✅ Checklist Final

- [ ] Arquivo `relatorio.tex` contém os pacotes necessários
- [ ] Caminhos para imagens estão corretos (relativos à pasta do .tex)
- [ ] Usou `\input{}` para tabelas
- [ ] Usou `\includegraphics{}` para imagens
- [ ] Compilou com sucesso (sem erros)
- [ ] Verificou que todas as tabelas e imagens aparecem no PDF final

---

**Gerado automaticamente em:** 31 de dezembro de 2025

Para regenerar as tabelas e imagens, execute: `jupyter notebook gerar_tabelas_latex_e_copiar_imagens.ipynb`
