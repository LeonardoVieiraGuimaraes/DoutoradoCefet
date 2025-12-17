# 📊 Resultados da Análise Estatística

## 📁 Estrutura de Diretórios

```
resultados/
├── dados/                          # Arquivos de dados (CSV e TXT)
│   ├── populacao_exponencial.csv   # Dados da população exponencial simulada
│   ├── estatisticas_tcl.csv        # Resultados do Teorema Central do Limite
│   ├── intervalos_confianca.csv    # Intervalos de confiança calculados
│   ├── dados_gta.csv               # Dados reais do GTA
│   └── resumo_resultados.txt       # Resumo textual de todas as análises
│
├── imagens/                         # Figuras e gráficos
│   ├── 01_exponencial_simulada/    # Imagens da análise com dados simulados
│   │   ├── populacao_exponencial.png
│   │   ├── tcl_convergencia.png
│   │   ├── intervalos_confianca.png
│   │   ├── anova_resultados.png
│   │   └── analise_integrada.png
│   │
│   └── 02_dados_reais_gta/         # Imagens da análise com dados reais
│       ├── distribuicao_gta.png
│       ├── tcl_dados_reais.png
│       ├── intervalos_confianca_gta.png
│       ├── anova_gta.png
│       └── resumo_analise_gta.png
│
└── README.md                        # Este arquivo

```

## 📝 Descrição dos Arquivos

### Dados (CSV/TXT)

- **populacao_exponencial.csv**: Amostra de 10.000 valores da população exponencial (λ=2.0)
- **estatisticas_tcl.csv**: Médias amostrais de diferentes tamanhos de amostra
- **intervalos_confianca.csv**: Limites inferior e superior dos ICs calculados
- **dados_gta.csv**: Amostra dos dados reais carregados do arquivo GTA
- **resumo_resultados.txt**: Estatísticas resumidas (média, desvio padrão, assimetria, etc.)

### Imagens

#### Análise 1: Exponencial Simulada
- **populacao_exponencial.png**: Distribuição da população com histograma e Q-Q plot
- **tcl_convergencia.png**: Convergência do TCL para diferentes tamanhos de amostra
- **intervalos_confianca.png**: Visualização dos 100 primeiros ICs calculados
- **anova_resultados.png**: Boxplots e distribuição dos grupos (ANOVA)
- **analise_integrada.png**: Painel com 8 subplots mostrando toda a análise

#### Análise 2: Dados Reais GTA
- **distribuicao_gta.png**: Distribuição dos dados reais com Q-Q plot
- **tcl_dados_reais.png**: TCL aplicado aos dados reais
- **intervalos_confianca_gta.png**: ICs calculados a partir dos dados reais
- **anova_gta.png**: ANOVA para os grupos disponíveis
- **resumo_analise_gta.png**: Visualizações consolidadas dos dados reais

## 🚀 Como Gerar os Resultados

Execute os notebooks na ordem:

1. **01_analise_exponencial_simulada.ipynb**: Análise com dados simulados
   ```bash
   jupyter notebook 01_analise_exponencial_simulada.ipynb
   ```

2. **02_analise_dados_reais_gta.ipynb**: Análise com dados reais
   ```bash
   jupyter notebook 02_analise_dados_reais_gta.ipynb
   ```

Os resultados serão automaticamente salvos nesta pasta.

## 📊 Métodos Utilizados

### Teorema Central do Limite (TCL)
- Tamanhos de amostra: n = 5, 10, 30, 50, 100, 500
- Número de iterações: 10.000 amostras por tamanho
- Verificação: Redução da assimetria conforme n aumenta

### Intervalo de Confiança (IC)
- Nível de confiança: 95%
- Distribuição: t-student
- Tamanho de amostra: 50 observações
- Número de ICs: 1.000

### Análise de Variância (ANOVA)
- Teste: One-way ANOVA
- Hipótese nula (H₀): As médias dos grupos são iguais
- Nível de significância: α = 0.05

### Distribuições Assimétricas
- **Simulada**: Distribuição Exponencial (λ=2.0)
- **Real**: Dados de transportes do GTA (apresenta assimetria direita)

## 📈 Resultados Esperados

### Exponencial Simulada
- Assimetria populacional: ~1.92
- Convergência do TCL: Comprovada
- Cobertura de IC: ~94-95%
- ANOVA: Significativa (p < 0.05)

### Dados Reais GTA
- Assimetria: Alta (direita)
- TCL: Valida mesmo com distribuição assimétrica
- IC: Cobertura esperada
- ANOVA: Depende da disponibilidade de grupos

---

**Data de geração**: 16 de dezembro de 2025  
**Disciplina**: Planejamento e Análise Estatística de Experimentos  
**Universidade**: CEFET-MG
