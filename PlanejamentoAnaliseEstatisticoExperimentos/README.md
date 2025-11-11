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
```python
numpy          # Computação numérica e geração de dados
scipy          # Distribuições estatísticas e testes
matplotlib     # Visualização de dados
seaborn        # Gráficos estatísticos avançados
```

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
