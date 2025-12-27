# 🎓 Análise Estatística com Dados Reais - Trabalho Final

**Programa:** Doutorado em Engenharia - Planejamento, Análise Estatística e Experimentos  
**Autor:** Leonardo Vieira Guimarães  
**Data:** Dezembro 2025  
**Instituição:** CEFET-MG

---

## 📋 Resumo Executivo

Este projeto executa uma análise estatística completa utilizando **dados reais de tráfego urbano (GTA)**, aplicando conceitos fundamentais de inferência estatística e delineamento experimental aprendidos nos Estudos Dirigidos 1 e 2:

- **Estudo Dirigido 1:** Simulação do Teorema Central do Limite (TCL) e Intervalos de Confiança (IC)
- **Estudo Dirigido 2:** ANOVA em diferentes delineamentos e testes Post-Hoc
- **Trabalho Final:** Aplicação em dados reais com interpretação prática

---

## 🎯 Objetivos

### Objetivo Geral
Demonstrar a aplicação de técnicas estatísticas avançadas em análise de dados reais de tráfego urbano, validando pressupostos teóricos e práticos.

### Objetivos Específicos

1. **Análise Descritiva:**
   - Caracterizar distribuição dos dados de tráfego
   - Verificar pressupostos de normalidade
   - Identificar outliers e padrões

2. **Inferência Estatística:**
   - Construir intervalos de confiança para parâmetros populacionais
   - Testar hipóteses sobre características do tráfego
   - Validar o TCL em dados reais assimétricos

3. **Delineamento Experimental:**
   - Comparar grupos (períodos, locais, condições)
   - Aplicar ANOVA em delineamentos adequados
   - Realizar testes Post-Hoc (Tukey HSD) para comparações múltiplas

4. **Interpretação Prática:**
   - Traduzir resultados estatísticos em insights práticos
   - Fazer recomendações baseadas em evidências
   - Documentar achados principais

---

## 📊 Estrutura de Dados

### Dataset: Tráfego Urbano (GTA)

**Fonte:** `D:\OneDrive\Pessoais\Doutorado\Cefet\data\`

**Variáveis Esperadas:**
- `tempo_viagem` - Tempo de deslocamento (minutos)
- `distancia` - Distância percorrida (km)
- `velocidade_media` - Velocidade média (km/h)
- `horario` - Período do dia (pico/fora-de-pico)
- `dia_semana` - Dia da semana
- `condicao_climatica` - Condições do tempo
- `tipo_veiculo` - Classe do veículo

### Estatísticas Descritivas
```
info_csv()  # Execute para visualizar estrutura dos dados
```

---

## 🔬 Metodologia

### Fase 1: Exploração e Limpeza

```python
# Carregar dados
import pandas as pd
df = pd.read_csv('dados_trafego.csv')

# Análise descritiva
df.describe()
df.info()

# Verificar valores faltantes e outliers
df.isnull().sum()
```

**Tarefas:**
- [ ] Carregar dataset completo
- [ ] Identificar variáveis-chave
- [ ] Remover ou tratar valores ausentes
- [ ] Detectar e tratar outliers

---

### Fase 2: Análise de Distribuições

**Basado no Estudo Dirigido 1:**

1. **Teste de Normalidade**
   - Shapiro-Wilk test
   - Kolmogorov-Smirnov test
   - Q-Q plots

2. **Análise de Assimetria**
   - Calcular coeficiente de assimetria (skewness)
   - Comparar com distribuições teóricas

3. **Construir Intervalos de Confiança**
   ```python
   from scipy import stats
   
   # IC 95% para média
   media = df['tempo_viagem'].mean()
   se = df['tempo_viagem'].std() / np.sqrt(len(df))
   ic = stats.t.interval(0.95, len(df)-1, loc=media, scale=se)
   ```

**Tarefas:**
- [ ] Gerar histogramas e boxplots
- [ ] Testar normalidade de variáveis principais
- [ ] Calcular IC para parâmetros de interesse
- [ ] Documentar pressupostos violados

---

### Fase 3: Comparação de Grupos (ANOVA)

**Baseado no Estudo Dirigido 2:**

#### 3.1 ANOVA Um Fator (Delineamento Simples)

Questão: O tempo médio de viagem varia entre períodos do dia?

```python
from scipy.stats import f_oneway

pico = df[df['horario'] == 'pico']['tempo_viagem']
fora_pico = df[df['horario'] == 'fora_pico']['tempo_viagem']

f_stat, p_value = f_oneway(pico, fora_pico)
```

#### 3.2 ANOVA Dois Fatores (Delineamento Fatorial)

Questão: Tempo de viagem varia por período × tipo de veículo?

```python
import statsmodels.api as sm
from statsmodels.formula.api import ols

modelo = ols('tempo_viagem ~ C(horario) + C(tipo_veiculo) + C(horario):C(tipo_veiculo)', 
             data=df).fit()
anova_table = sm.stats.anova_lm(modelo, typ=2)
```

#### 3.3 Testes Post-Hoc (Tukey HSD)

```python
from scipy.stats import tukey_hsd

resultado = tukey_hsd(grupo1, grupo2, grupo3)
print(resultado)
```

**Tarefas:**
- [ ] Verificar pressupostos ANOVA (normalidade, homocedasticidade)
- [ ] Aplicar ANOVA apropriada
- [ ] Interpretar resultados (F, p-value)
- [ ] Executar testes Post-Hoc se p < 0.05
- [ ] Documentar comparações múltiplas

---

### Fase 4: Validação do TCL em Dados Reais

**Aplicando aprendizado do Estudo Dirigido 1:**

Simulação: Coletar múltiplas amostras para verificar se a distribuição das médias é normal

```python
import numpy as np

# 1. Coletar 10.000 amostras
n_simulacoes = 10000
tamanho_amostra = 50
medias = []

for i in range(n_simulacoes):
    amostra = np.random.choice(df['tempo_viagem'], size=tamanho_amostra, replace=True)
    medias.append(amostra.mean())

# 2. Visualizar distribuição das médias
import matplotlib.pyplot as plt
plt.hist(medias, bins=50, density=True, alpha=0.7)
plt.xlabel('Média Amostral')
plt.ylabel('Frequência')
plt.title('Distribuição das Médias Amostrais (TCL)')
plt.show()

# 3. Testar normalidade das médias
from scipy.stats import shapiro
stat, p = shapiro(medias)
print(f"Shapiro-Wilk: p-value = {p:.4f}")
```

**Tarefas:**
- [ ] Implementar simulação TCL
- [ ] Gerar gráficos de convergência para normalidade
- [ ] Comparar com teórico N(μ, σ²/n)
- [ ] Documentar achados sobre o TCL em dados reais

---

## 📈 Análises Previstas

### A. Análise Temporal
- Variação de tráfego por hora do dia
- Padrões de pico vs fora-de-pico
- Dias úteis vs fins de semana

### B. Análise Geográfica
- Comparação entre diferentes regiões/rotas
- Identificação de gargalos

### C. Análise por Tipo de Veículo
- Diferenças de comportamento
- Tempos de trajeto específicos

### D. Análise Multivariada
- Correlações entre variáveis
- Modelos preditivos (opcional)

---

## 📚 Conceitos Teóricos Aplicados

### Do Estudo Dirigido 1:
- ✅ **Teorema Central do Limite (TCL):** Convergência para normalidade
- ✅ **Intervalos de Confiança:** Estimação de parâmetros populacionais
- ✅ **Distribuições Assimétricas:** Manejo de dados não-normais

### Do Estudo Dirigido 2:
- ✅ **ANOVA Um Fator:** Comparação de grupos independentes
- ✅ **ANOVA Dois Fatores:** Delineamento Fatorial 2x2 (ou mais)
- ✅ **Testes Post-Hoc:** Tukey HSD para comparações múltiplas
- ✅ **Pressupostos:** Normalidade e homocedasticidade

### Integração:
- ✅ **Dados Reais:** Validação de pressupostos teóricos
- ✅ **Interpretação Prática:** Tradução para decisões
- ✅ **Documentação:** Comunicação de resultados

---

## 📁 Estrutura do Projeto

```
estudo_dirigido_3/
├── README_TRABALHO_FINAL.md          ← VOCÊ ESTÁ AQUI
├── 01_analise_exponencial_simulada.ipynb
├── 02_analise_dados_reais_gta.ipynb
├── ler_pdfs.py
├── ler_pdfs_avancado.py
├── exemplo_uso_pdfs.py
├── informacao.ipynb
├── pdfs_extraidos/
│   ├── estudos_dirigidos_1.txt
│   └── estudos_dirigidos_2.txt
├── dados/
│   └── trafego_gta.csv              (será criado)
├── resultados/
│   ├── graficos/                    (será criado)
│   ├── tabelas/                     (será criado)
│   └── ESTRUTURA_SEPARADA.md        (relatório final)
└── relatorio/
    └── trabalho_final.md            (documento final)
```

---

## 🔧 Como Usar Este Projeto

### 1️⃣ Configuração Inicial

```bash
# Instalar dependências
pip install pandas numpy scipy matplotlib seaborn statsmodels

# Verificar dados disponíveis
python informacao.ipynb
```

### 2️⃣ Executar Análises

```bash
# Análise exploratória (Notebook 1)
jupyter notebook 01_analise_exponencial_simulada.ipynb

# Análise com dados reais (Notebook 2)
jupyter notebook 02_analise_dados_reais_gta.ipynb
```

### 3️⃣ Gerar Relatório

Os notebooks gerarão automaticamente:
- Gráficos em `resultados/graficos/`
- Tabelas em `resultados/tabelas/`
- Resumo em `relatorio/trabalho_final.md`

---

## 📊 Checklist de Análises

### Análise Exploratória
- [ ] Carregamento de dados
- [ ] Verificação de integridade
- [ ] Estatísticas descritivas
- [ ] Visualizações iniciais

### Análise de Distribuições
- [ ] Histogramas e density plots
- [ ] Q-Q plots
- [ ] Testes de normalidade
- [ ] Cálculo de assimetria

### Intervalos de Confiança
- [ ] IC para médias
- [ ] IC para variâncias
- [ ] IC para proporções
- [ ] Interpretação dos IC

### ANOVA e Comparações
- [ ] Verificação de pressupostos
- [ ] ANOVA Um Fator
- [ ] ANOVA Dois Fatores (se aplicável)
- [ ] Testes Post-Hoc

### Validação do TCL
- [ ] Simulação em dados reais
- [ ] Comparação com teórico
- [ ] Demonstração de convergência

### Relatório Final
- [ ] Documentação de métodos
- [ ] Tabelas de resultados
- [ ] Gráficos explicativos
- [ ] Conclusões e recomendações

---

## 💡 Dicas de Análise

1. **Sempre visualize antes de testar:** Gráficos revelam padrões que testes numéricos podem perder

2. **Verifique pressupostos:** Não assuma normalidade/homocedasticidade - teste!

3. **Tamanho da amostra importa:** Com amostras grandes, pequenas diferenças podem ser significativas

4. **Use múltiplas perspectivas:** ANOVA + visualizações + IC + effect size

5. **Documente decisões:** Por que removeu outliers? Por que escolheu esse teste?

---

## 📖 Referências dos Estudos Dirigidos

- **ED 1:** Simulação do TCL em distribuições assimétricas (Exponencial)
- **ED 2:** ANOVA em delineamentos Simples, em Blocos e Fatorial

**Principais Conceitos:**
- Teorema Central do Limite e convergência para normalidade
- Intervalos de Confiança e interpretação
- Análise de Variância (ANOVA)
- Testes Post-Hoc (Tukey HSD)
- Delineamentos Experimentais

---

## ✅ Status do Projeto

| Fase | Descrição | Status |
|------|-----------|--------|
| 📚 Estudos Dirigidos | ED1 e ED2 | ✅ Completo |
| 📖 Leitura de PDFs | Scripts criados | ✅ Pronto |
| 📊 Análise Exploratória | Notebook 01 | 🔄 Próxima |
| 📈 Análise com Dados Reais | Notebook 02 | 🔄 Próxima |
| 📋 Relatório Final | Documentação | 🔄 Próxima |

---

## 📞 Próximos Passos

1. **Carregar e explorar dados** - Executar análise descritiva
2. **Testar pressupostos** - Normalidade, homocedasticidade
3. **Construir intervalos de confiança** - Validar IC em dados reais
4. **Aplicar ANOVA** - Comparar grupos
5. **Realizar testes Post-Hoc** - Comparações múltiplas se necessário
6. **Validar TCL** - Simulação em dados reais
7. **Documentar conclusões** - Relatório final

---

## 📝 Notas Importantes

- Os PDFs dos estudos dirigidos estão em `pdfs_extraidos/` em formato texto
- Use os notebooks existentes como base para suas análises
- Mantenha versionamento adequado de código
- Documente todas as decisões analíticas
- Salve gráficos e tabelas para o relatório final

---

**Última atualização:** 27 de dezembro de 2025  
**Versão:** 1.0 - Estrutura Inicial
