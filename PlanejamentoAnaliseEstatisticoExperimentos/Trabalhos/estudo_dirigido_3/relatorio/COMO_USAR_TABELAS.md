# Guia de Uso das Tabelas LaTeX

## 📋 Tabelas Geradas Automaticamente

Todas as tabelas foram geradas automaticamente a partir dos arquivos CSV da análise e estão localizadas em:
```
relatorio/tabelas_latex/
```

## 📊 Lista de Tabelas

### Análise Principal (TCL, IC, ANOVA)

| # | Arquivo | Descrição | Comando |
|---|---------|-----------|---------|
| 1 | `tab_01_Parametros_Analise.tex` | Parâmetros utilizados na análise | `\input{relatorio/tabelas_latex/tab_01_Parametros_Analise.tex}` |
| 2 | `tab_02_Estatisticas_Descritivas_Gerais.tex` | Estatísticas descritivas dos dados | `\input{relatorio/tabelas_latex/tab_02_Estatisticas_Descritivas_Gerais.tex}` |
| 3 | `tab_03_TCL_Resumo_Comparativo.tex` | Resumo comparativo do TCL | `\input{relatorio/tabelas_latex/tab_03_TCL_Resumo_Comparativo.tex}` |
| 4 | `tab_04_TCL_Validacao_10mil_simulacoes.tex` | Validação do TCL com 10k simulações | `\input{relatorio/tabelas_latex/tab_04_TCL_Validacao_10mil_simulacoes.tex}` |
| 5 | `tab_05_IC_95_Por_Ano_Detalhado.tex` | Intervalos de confiança por ano | `\input{relatorio/tabelas_latex/tab_05_IC_95_Por_Ano_Detalhado.tex}` |
| 6 | `tab_06_IC_95_Por_Mes_Detalhado.tex` | Intervalos de confiança por mês | `\input{relatorio/tabelas_latex/tab_06_IC_95_Por_Mes_Detalhado.tex}` |
| 7 | `tab_07_ANOVA_Efeitos_Principais_Interacao.tex` | Efeitos principais da ANOVA | `\input{relatorio/tabelas_latex/tab_07_ANOVA_Efeitos_Principais_Interacao.tex}` |
| 8 | `tab_08_ANOVA_Qualidade_Modelo.tex` | Qualidade do modelo ANOVA | `\input{relatorio/tabelas_latex/tab_08_ANOVA_Qualidade_Modelo.tex}` |
| 9 | `tab_09_Conclusoes_Finais_Interpretacao.tex` | Conclusões finais | `\input{relatorio/tabelas_latex/tab_09_Conclusoes_Finais_Interpretacao.tex}` |

### Dados Complementares

| # | Arquivo | Descrição |
|---|---------|-----------|
| 10 | `tab_10_bd_gta_dentro_mg202505091607_analise.tex` | Análise de dados GTA MG |
| 11 | `tab_11_bd_gta_dentro_mg_faixa_etaria202505091602_analise.tex` | Análise por faixa etária |
| 12 | `tab_12_bd_gta_oe202505091618_analise.tex` | Análise de dados OE |
| 13 | `tab_13_bd_gta_oe_faixa_etaria202505091630_analise.tex` | Análise OE por faixa etária |
| 14 | `tab_14_gtas_com_distancias_analise.tex` | Análise com distâncias |
| 15 | `tab_15_matriz_distancias_analise.tex` | Matriz de distâncias |
| 16 | `tab_16_possiveis_fraudes_analise.tex` | Análise de fraudes |

## 🔧 Como Usar no Seu Documento LaTeX

### Opção 1: Incluir Tabelas Individuais

No seu arquivo `.tex` principal, insira as tabelas conforme desejar:

```latex
\section{Análise Descritiva}
\input{relatorio/tabelas_latex/tab_02_Estatisticas_Descritivas_Gerais.tex}

\section{Teorema Central do Limite}
\input{relatorio/tabelas_latex/tab_03_TCL_Resumo_Comparativo.tex}
\input{relatorio/tabelas_latex/tab_04_TCL_Validacao_10mil_simulacoes.tex}

\section{Intervalos de Confiança}
\input{relatorio/tabelas_latex/tab_05_IC_95_Por_Ano_Detalhado.tex}
\input{relatorio/tabelas_latex/tab_06_IC_95_Por_Mes_Detalhado.tex}

\section{Análise de Variância}
\input{relatorio/tabelas_latex/tab_07_ANOVA_Efeitos_Principais_Interacao.tex}
\input{relatorio/tabelas_latex/tab_08_ANOVA_Qualidade_Modelo.tex}
```

### Opção 2: Usar o Arquivo de Índice

Se desejar uma abordagem mais centralizada, descomente as linhas no arquivo `INDICE_TABELAS.txt`.

## 📝 Notas Importantes

1. **Formato**: As tabelas utilizam o ambiente `table[H]` do pacote `float`
   - Certifique-se que seu preâmbulo LaTeX contém:
   ```latex
   \usepackage{float}
   \usepackage{geometry} % para melhor controle de layout
   ```

2. **Referências**: Cada tabela possui um label único `tab:XX_*` 
   - Use `\ref{tab:01_01_Parametros_Metodologia}` para referenciá-las

3. **Fonte dos dados**: Cada tabela indica a pasta e arquivo CSV de origem

4. **Regenerar tabelas**: Para atualizar as tabelas, execute novamente o notebook `gerar_tabelas_latex.ipynb`

## 📍 Estrutura de Diretórios

```
estudo_dirigido_3/
├── resultados/
│   ├── 01_Parametros_Metodologia/
│   ├── 02_Estatisticas_Descritivas/
│   ├── 03_Teorema_Central_Limite/
│   ├── 04_Intervalos_Confianca/
│   ├── 05_ANOVA_Fatorial/
│   ├── 06_Conclusoes_Relatorio/
│   └── informacoes_dados/
├── relatorio/
│   ├── relatorio.tex (seu arquivo principal)
│   └── tabelas_latex/ (🔴 Tabelas estão aqui!)
└── gerar_tabelas_latex.ipynb
```

## ✅ Próximos Passos

1. Copie e cole os comandos `\input{}` no seu documento LaTeX
2. Compile com `pdflatex` ou seu editor favorito
3. As tabelas serão incorporadas automaticamente

---

**Gerado em**: {{ data_geracao }}
**Notebook**: `gerar_tabelas_latex.ipynb`
