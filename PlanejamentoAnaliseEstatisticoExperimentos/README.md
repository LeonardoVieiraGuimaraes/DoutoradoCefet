# Planejamento e Análise Estatística de Experimentos

## 📚 Sobre o Repositório

Este repositório contém simulações e análises estatísticas que exploram conceitos fundamentais através de implementações práticas em Python. O objetivo é demonstrar numericamente o significado de conceitos estatísticos por meio da repetição de processos de amostragem.

**Instituição:** CEFET-MG  
**Programa:** Doutorado  
**Período:** 2025/1

## 🎯 Objetivos

Demonstrar através de simulações computacionais:
- Interpretação correta do **Nível de Confiança** em Intervalos de Confiança
- Comportamento de **Estimadores Não-Viciados**
- Significado prático do **Erro Tipo I** em testes de hipóteses

## 📊 Simulações Disponíveis

### 1. Simulação do Nível de Confiança (Intervalo de Confiança)

**Arquivo:** [`simulacao_intervalo_confianca.ipynb`](simulacao_intervalo_confianca.ipynb)

#### Conceito Explorado
O Nível de Confiança (ex: 95%) **não é** a probabilidade de que um IC específico contenha a média populacional (μ). É a proporção de intervalos que conteriam μ se repetíssemos o processo de amostragem infinitas vezes nas mesmas condições.

#### Parâmetros da Simulação
- **População:** N = 100.000, μ = 180, σ = 20
- **Tamanho da Amostra:** n = 100
- **Nível de Confiança:** 95%
- **Número de Simulações:** 10.000

#### Como Executar
```python
# Abra o notebook Jupyter
jupyter notebook simulacao_intervalo_confianca.ipynb

# Ou execute todas as células de uma vez
jupyter nbconvert --execute --to notebook simulacao_intervalo_confianca.ipynb
```

#### Resultado Esperado
Aproximadamente **9.500 dos 10.000 intervalos** (95%) devem conter a verdadeira média populacional μ = 180, demonstrando empiricamente o significado do nível de confiança.

#### Visualizações Incluídas
- Gráfico dos primeiros 100 intervalos de confiança (verde = contém μ, vermelho = não contém μ)
- Convergência da proporção de sucesso ao longo das simulações
- Análise estatística detalhada dos resultados

## 🛠️ Tecnologias e Ferramentas

### Linguagem Principal
- **Python 3.8+**

### Bibliotecas Utilizadas

#### NumPy
```python
import numpy as np
```
Biblioteca fundamental para computação numérica em Python. Utilizada para:
- Geração de números aleatórios com distribuições estatísticas
- Operações matemáticas em arrays e matrizes
- Cálculos de médias, desvios padrão e outras estatísticas

#### SciPy
```python
from scipy.stats import t
```
**SciPy** (Scientific Python) é uma biblioteca fundamental para computação científica em Python, construída sobre o NumPy.

**O que é o módulo `scipy.stats`?**

O módulo `scipy.stats` contém uma vasta coleção de distribuições de probabilidade e funções estatísticas:
- **Distribuições Contínuas e Discretas:** Normal, t-Student, chi-quadrado, binomial, Poisson, etc.
- **Funções Estatísticas:** Testes de hipóteses, correlação, regressão
- **Intervalos de Confiança:** Cálculo automático de ICs para diversas distribuições

**Por que usamos `t.interval()` nas simulações?**

A distribuição **t de Student** é usada quando:
- ✅ A população tem distribuição normal (ou aproximadamente normal)
- ✅ O desvio padrão populacional (σ) é **desconhecido**
- ✅ Estimamos σ usando o desvio padrão amostral (s)
- ✅ Tamanho de amostra pequeno (n < 30) ou médio

**Função `t.interval()`:**
```python
t.interval(confidence, df, loc, scale)
```

**Parâmetros:**
- `confidence`: Nível de confiança (ex: 0.95 para 95%)
- `df`: Graus de liberdade (n - 1)
- `loc`: Média amostral (centro do intervalo)
- `scale`: Erro padrão (s / √n)

**Retorna:** `(limite_inferior, limite_superior)` do intervalo de confiança

**Vantagens do SciPy:**
1. **Precisão:** Implementações numericamente estáveis e validadas
2. **Facilidade:** Uma linha de código substitui cálculos complexos
3. **Flexibilidade:** Suporta dezenas de distribuições diferentes
4. **Integração:** Funciona perfeitamente com NumPy e Pandas

**Alternativa Manual (sem SciPy):**
```python
# Sem SciPy - cálculo manual
t_critical = 1.984  # Valor crítico para 95% de confiança e 99 graus de liberdade
margin_error = t_critical * standard_error
ic_lower = sample_mean - margin_error
ic_upper = sample_mean + margin_error
```

Com SciPy, tudo isso é feito automaticamente com `t.interval()` ! 🎯

#### Matplotlib
```python
import matplotlib.pyplot as plt
```
Biblioteca principal para visualização de dados em Python. Utilizada para criar gráficos estáticos, animados e interativos.

#### Seaborn
```python
import seaborn as sns
```
Biblioteca de visualização de dados estatísticos construída sobre Matplotlib. Oferece estilos visuais mais atraentes e funções especializadas para gráficos estatísticos.

### Ambiente de Desenvolvimento
- **Jupyter Notebook** / JupyterLab
- VS Code com extensão Python

## 📁 Estrutura do Repositório

```
PlanejamentoAnaliseEstatisticoExperimentos/
├── README.md
├── simulacao_intervalo_confianca.ipynb
└── (futuros notebooks de simulação)
```

## 🚀 Como Começar

### 1. Clonar o Repositório
```bash
git clone https://github.com/LeonardoVieiraGuimaraes/DoutoradoCefet.git
cd DoutoradoCefet/PlanejamentoAnaliseEstatisticoExperimentos
```

### 2. Instalar Dependências
```bash
pip install numpy scipy matplotlib seaborn jupyter
```

### 3. Iniciar o Jupyter Notebook
```bash
jupyter notebook
```

### 4. Abrir e Executar os Notebooks
Navegue até o arquivo `.ipynb` desejado e execute as células sequencialmente.

## 📖 Conceitos Estatísticos Abordados

### Intervalo de Confiança
- Interpretação frequentista do nível de confiança
- Diferença entre confiança do método vs. probabilidade de um intervalo específico
- Visualização de múltiplos intervalos simultâneos

### Metodologia de Simulação
- Geração de populações com distribuição normal
- Amostragem aleatória sem reposição
- Cálculo de intervalos usando distribuição t de Student
- Análise de convergência através da Lei dos Grandes Números

## 📚 Referências Bibliográficas

- **DEVORE, Jay L.** *Probabilidade e Estatística para Engenharia e Ciências.* São Paulo: Cengage Learning, 2006.
- **MONTGOMERY, Douglas C.** *Design and Analysis of Experiments.* Wiley.

## 👨‍💻 Autor

**Leonardo Vieira Guimarães**  
Doutorando - CEFET-MG  
[GitHub](https://github.com/LeonardoVieiraGuimaraes)

## 📝 Licença

Este projeto é destinado para fins acadêmicos e educacionais.

## � Atualizações Futuras

- [ ] Simulação de Estimadores Não-Viciados
- [ ] Simulação de Erro Tipo I e Tipo II
- [ ] Análise de Variância (ANOVA) via simulação
- [ ] Comparação de diferentes testes estatísticos
- [ ] Visualizações interativas com Plotly

---

*Última atualização: 11 de novembro de 2025*
