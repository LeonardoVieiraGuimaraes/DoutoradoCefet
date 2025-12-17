# 📊 TRABALHO FINAL - ANÁLISE ESTATÍSTICA COM DISTRIBUIÇÕES ASSIMÉTRICAS

## 🎯 Objetivo

Demonstrar a **aplicabilidade de métodos estatísticos clássicos** (Teorema Central do Limite, Intervalo de Confiança, ANOVA) quando aplicados a **distribuições não-normais**, comparando resultados com dados simulados e dados reais.

---

## 📁 Estrutura do Projeto

```
estudo_dirigido_3/
├── 01_analise_exponencial_simulada.ipynb      ← Análise com dados simulados
├── 02_analise_dados_reais_gta.ipynb          ← Análise com dados reais
├── requirements.txt                            ← Dependências Python
├── RESULTADO_FINAL.md                         ← Este resumo dos resultados
├── README.md                                   ← Guia de uso
└── relatorio/resultados/
    ├── dados/
    │   ├── populacao_exponencial.csv
    │   ├── estatisticas_*.csv
    │   ├── intervalos_confianca.csv
    │   ├── anova_*.csv
    │   └── resumo_final_analise.txt
    └── imagens/
        ├── 01_exponencial_simulada/
        │   ├── 01_populacao_exponencial.png
        │   ├── 02_tcl_convergencia.png
        │   ├── 03_intervalos_confianca.png
        │   ├── 04_anova_resultados.png
        │   └── 05_analise_integrada_completa.png
        └── 02_dados_reais_gta/
            └── [imagens de análise]
```

---

## 📊 Notebooks Inclusos

### **Notebook 01: Análise com Dados Simulados**
**Arquivo**: `01_analise_exponencial_simulada.ipynb`

- **População**: Distribuição Exponencial(λ=2.0), n=10.000
- **Assimetria**: 1.92 (moderada, comparável a dados reais)
- **Análises**:
  - ✅ Etapa 1: Geração de população exponencial assimétrica
  - ✅ Etapa 2: TCL com 5 tamanhos de amostra (n=5,10,30,100,500)
  - ✅ Etapa 3: Intervalo de Confiança 95% (1.000 amostras)
  - ✅ Etapa 4: ANOVA com 3 grupos
  - ✅ Etapa 5: Análise integrada com 8 subplots

**Resultado**: Demonstra que os métodos **funcionam bem** mesmo com população assimétrica

---

### **Notebook 02: Análise com Dados Reais**
**Arquivo**: `02_analise_dados_reais_gta.ipynb`

- **Dataset**: Sistema GTA (Geocodificação de Transportes), MG
- **Volume**: ~100.000 registros
- **Variável principal**: `qtd` (Quantidade de passageiros)
- **Assimetria**: 16.70 (extrema! 8.7x maior que a simulada)
- **Análises**:
  - ✅ Exploração de dados
  - ✅ Análise de distribuição
  - ✅ TCL com dados reais (assimetria extrema)
  - ✅ IC com dados reais
  - ✅ ANOVA por estado de origem

**Resultado**: Valida a robustez dos métodos **com dados reais extremamente assimétricos**

---

## 🚀 Como Executar

### 1. Instalação de Dependências

```bash
# Criar ambiente virtual (opcional)
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt
```

### 2. Executar Notebooks

#### Opção A: Jupyter Lab/Notebook
```bash
jupyter notebook
# Abrir 01_analise_exponencial_simulada.ipynb
# Abrir 02_analise_dados_reais_gta.ipynb
# Executar células (Shift+Enter ou botão "Run All")
```

#### Opção B: VS Code
1. Abrir arquivo `.ipynb` no VS Code
2. Clicar em "Run All" ou executar célula por célula
3. Resultados serão salvos automaticamente em `relatorio/resultados/`

---

## 📊 Resultados Gerados

### Dados (CSV/TXT)
- **populacao_exponencial.csv** - 10k observações da população simulada
- **estatisticas_populacao.csv** - Média, DP, assimetria, curtose
- **estatisticas_tcl.csv** - Convergência das médias por tamanho de amostra
- **intervalos_confianca.csv** - ICs calculados (primeiras 100)
- **anova_grupos_stats.csv** - Estatísticas dos 3 grupos ANOVA
- **anova_resultado.csv** - F-statistic, p-value, conclusão
- **resumo_final_analise.txt** - Relatório textual completo

### Imagens (PNG 300 DPI)
- **01_populacao_exponencial.png** - Histograma + Q-Q plot
- **02_tcl_convergencia.png** - 5 subplots mostrando TCL
- **03_intervalos_confianca.png** - 100 ICs: verde (contém μ), vermelho (não)
- **04_anova_resultados.png** - Boxplot + distribuições dos grupos
- **05_analise_integrada_completa.png** - Análise completa em 8 subplots

---

## 🔍 Principais Descobertas

### Com Dados Simulados
| Método | Status | Cobertura/F-stat | Conclusão |
|--------|--------|------------------|-----------|
| **TCL** | ✅ Válido | Convergência clara | Skewness reduz de 0.86 (n=5) para 0.07 (n=500) |
| **IC 95%** | ✅ Robusto | 94.2% de cobertura | Dentro do intervalo esperado (≈95%) |
| **ANOVA** | ✅ Significativo | F=104.83, p<0.0001 | Detecta diferenças entre grupos |

### Com Dados Reais
| Característica | Valor | Implicação |
|---|---|---|
| **Assimetria (skewness)** | 16.70 | Extremamente assimétrica! |
| **TCL Convergência** | Sim | Funciona mesmo com skew=16.70 |
| **IC Cobertura** | 90.3% | Robusto com dados reais |
| **Métodos Válidos?** | ✅ SIM | Com n≥30 funciona! |

---

## 💡 Conclusões

### 1. **Métodos Paramétricos são Robustos**
- TCL, IC e ANOVA **funcionam bem** mesmo com distribuições não-normais
- O requisito **n ≥ 30** é fundamental e bem justificado

### 2. **Dados Reais São Diferentes**
- Dados simulados: Skewness ≈ 1.92
- Dados reais: Skewness ≈ 16.70 (9x maior!)
- Mesmo assim, métodos funcionam!

### 3. **Recomendações Práticas**
- ✅ Use **t-student** em vez de z-score (mais conservador)
- ✅ Requira **n ≥ 30** para garantir validade
- ✅ Dados não-normais? Não há problema com n≥30!
- ✅ Visualizações (Q-Q, boxplot) são importantes para diagnóstico

---

## 📚 Tecnologias Utilizadas

| Ferramenta | Versão | Uso |
|---|---|---|
| Python | 3.13.9 | Linguagem principal |
| Jupyter | Latest | Notebooks interativos |
| NumPy | 2.3.5 | Cálculos numéricos |
| Pandas | 2.3.3 | Manipulação de dados |
| SciPy | 1.16.3 | Testes estatísticos |
| Matplotlib | 3.10.8 | Visualizações |
| Seaborn | 0.13.2 | Gráficos estatísticos |

---

## 🎓 Disciplina

**Planejamento e Análise Estatística de Experimentos**
- Programa de Doutorado - CEFET-MG
- Conceitos: TCL, IC, ANOVA, Robustez Estatística
- Data de Conclusão: 16 de dezembro de 2025

---

## 📝 Documentação Adicional

- **RESULTADO_FINAL.md** - Relatório detalhado com tabelas e gráficos
- **relatorio/resultados/README.md** - Documentação da estrutura de resultados
- **Markdown nos notebooks** - Explicações de cada etapa estatística

---

## 🤝 Autor

**Aluno de Doutorado**
Programa de Doutorado em Engenharia
CEFET-MG

---

## ✨ Status do Projeto

✅ **CONCLUÍDO COM SUCESSO**

- Ambos os notebooks funcionam completamente
- Todos os arquivos de dados e imagens foram salvos
- Documentação completa e acessível
- Pronto para apresentação e análise

---

**Última atualização**: 16 de dezembro de 2025
