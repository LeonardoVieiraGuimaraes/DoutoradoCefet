# 📊 Estudo Dirigido 3: Análise Estatística com Dados Reais

## 🎯 Descrição do Projeto

Projeto de análise estatística aplicada integrando **Teorema Central do Limite (TCL)**, **Intervalos de Confiança (IC)** e **Análise de Variância (ANOVA)** em dados reais do GTA (Grand Theft Auto). O trabalho transita da teoria para a prática, utilizando dados simulados e reais para validar conceitos estatísticos fundamentais.

---

## 📋 Conteúdo dos Notebooks

### 1️⃣ `01_analise_exponencial_simulada.ipynb`
**Análise estatística com dados simulados (distribuição exponencial)**

Demonstra conceitos teóricos usando dados controlados e simulados:
- Geração de amostras de distribuição exponencial
- Aplicação do Teorema Central do Limite
- Cálculo de Intervalos de Confiança
- Visualizações de convergência

**Saídas:**
- Gráficos de distribuições e Q-Q plots
- Tabelas com estatísticas descritivas

---

### 2️⃣ `analise_tcl_ic_anova_dados_reais.ipynb` ⭐ **PRINCIPAL**
**Análise estatística completa com dados reais do GTA**

Implementação completa das três técnicas estatísticas em dados reais:

#### 📊 **Parte 1 - Exploração de Dados**
- Carregamento e análise de 100.000 registros
- Estatísticas descritivas (média, mediana, desvio padrão, etc.)
- Testes de normalidade (Shapiro-Wilk)
- Visualização: histograma + Q-Q plot

**Arquivo de saída:** `01_estatisticas_dados_reais.csv`

#### 📈 **Parte 2 - Teorema Central do Limite (TCL)**
Valida a convergência para a distribuição normal com amostras de tamanho $n = 5$ e $n = 50$

- Extração de 10.000 amostras para cada tamanho
- Cálculo das médias amostrais
- Comparação com distribuição teórica (z-score)

**Visualizações separadas:**
- `02_tcl_histograma_n5.png` - Histograma das médias (n=5)
- `02_tcl_histograma_n50.png` - Histograma das médias (n=50)
- `02_tcl_qqplot_n5.png` - Q-Q plot (n=5)
- `02_tcl_qqplot_n50.png` - Q-Q plot (n=50)

**Arquivo de saída:** `02_tcl_resultados.csv`

#### 🎯 **Parte 3 - Intervalos de Confiança (IC)**
Construção e validação de intervalos de confiança a 95%

- Geração de 10.000 intervalos independentes
- Cálculo da taxa de cobertura (esperado ≈ 95%)
- Análise da variabilidade dos limites

**Visualizações separadas:**
- `03_ic_intervalos_amostra.png` - Primeiros 100 intervalos
- `03_ic_distribuicao_limites.png` - Distribuição dos limites inferior e superior

**Arquivos de saída:** 
- `03_ic_resumo.csv` - Resumo dos resultados
- `03_ic_amostra_1000.csv` - Amostra de 1.000 intervalos

#### 🔬 **Parte 4 - Análise de Variância (ANOVA)**
Teste de diferenças entre grupos (por estado)

- Particionamento dos dados por unidade federativa
- Teste ANOVA de um fator
- Cálculo de F-statistic e p-value

**Visualizações separadas:**
- `04_anova_distribuicao_histograma.png` - Histograma da distribuição
- `04_anova_estatisticas_tabela.png` - Tabela de estatísticas

**Arquivos de saída:**
- `04_anova_resumo.csv` - Resumo do teste ANOVA
- `04_estatisticas_por_grupo.csv` - Estatísticas descritivas por grupo

#### 📋 **Parte 5 - Consolidação Final**
Agregação de todos os parâmetros e resultados

**Arquivo de saída:** `parametros_completos.csv` - Parâmetros consolidados de todas as análises

---

### 3️⃣ `02_analise_dados_reais_gta.ipynb`
**Análise exploratória adicional com dados reais**

Complementa a análise principal com explorações específicas dos dados GTA.

---

### 4️⃣ `explorador_dados.ipynb`
**Utilitário de exploração e documentação de CSV**

Ferramenta automatizada para:
- Detecção automática de delimitadores
- Análise de estrutura de dados
- Geração de documentação automática

**Saídas:**
- `relatorio_dados_detalhado.csv` - Relatório estruturado dos arquivos CSV analisados

---

## 📁 Estrutura de Arquivos

```
estudo_dirigido_3/
├── 01_analise_exponencial_simulada.ipynb
├── 02_analise_dados_reais_gta.ipynb
├── analise_tcl_ic_anova_dados_reais.ipynb  ⭐ Notebook principal
├── explorador_dados.ipynb
├── requirements.txt
├── README.md
│
└── relatorio/
    └── resultados/
        ├── imagens/
        │   ├── 01_distribuicao_dados_reais.png
        │   ├── 02_tcl_histograma_n5.png
        │   ├── 02_tcl_histograma_n50.png
        │   ├── 02_tcl_qqplot_n5.png
        │   ├── 02_tcl_qqplot_n50.png
        │   ├── 03_ic_intervalos_amostra.png
        │   ├── 03_ic_distribuicao_limites.png
        │   ├── 04_anova_distribuicao_histograma.png
        │   └── 04_anova_estatisticas_tabela.png
        │
        ├── 01_estatisticas_dados_reais.csv
        ├── 02_tcl_resultados.csv
        ├── 03_ic_resumo.csv
        ├── 03_ic_amostra_1000.csv
        ├── 04_anova_resumo.csv
        ├── 04_estatisticas_por_grupo.csv
        ├── parametros_completos.csv
        └── relatorio_dados_detalhado.csv
│
└── _arquivos_antigos/
    ├── analise_dados_reais_gta.ipynb
    ├── informacao.ipynb
    ├── trabalho_final_com_dados_reais.ipynb
    └── trabalhofinal/
```

---

## 📊 Dados Utilizados

**Fonte:** Base de dados GTA  
**Tamanho:** 950.40 MB (8.3 milhões de registros)  
**Amostra:** 100.000 registros para análise  

**Características dos dados:**
- Distribuição: Altamente assimétrica (assimetria: 16.70)
- Curtose: 687.43 (distribuição com caudas muito pesadas)
- Teste de normalidade: Rejeita hipótese nula (não-normal)
- Grupos: 1 estado (MG) na análise ANOVA

---

## 🔧 Configuração do Ambiente

### Requisitos
- **Python:** 3.8 ou superior
- **Jupyter Notebook:** Latest version
- **Bibliotecas:** Ver `requirements.txt`

### Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/LeonardoVieiraGuimaraes/DoutoradoCefet.git
   cd DoutoradoCefet/PlanejamentoAnaliseEstatisticoExperimentos/Trabalhos/estudo_dirigido_3
   ```

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Inicie o Jupyter:**
   ```bash
   jupyter notebook
   ```

### Dependências Principais
- **pandas**: Manipulação de dados
- **numpy**: Computação numérica
- **scipy.stats**: Testes e distribuições estatísticas
- **matplotlib** e **seaborn**: Visualizações
- **scikit-learn**: Testes adicionais

---

## 📖 Como Usar

### Opção 1: Análise Simples (Dados Simulados)
Execute `01_analise_exponencial_simulada.ipynb` para visualizar:
- Geração de dados controlados
- Aplicação de TCL, IC e ANOVA em ambiente sem ruído

### Opção 2: Análise Completa (Dados Reais) ⭐ **RECOMENDADO**
Execute `analise_tcl_ic_anova_dados_reais.ipynb` para:
- Análise estatística completa de dados reais
- Validação teórica em cenário prático
- Visualizações publication-quality em alta resolução (300 dpi)

### Opção 3: Exploração de Dados
Execute `explorador_dados.ipynb` para:
- Gerar relatório automático da estrutura dos dados
- Detectar delimitadores e tipos de dados
- Criar documentação CSV estruturada

---

## 📈 Resultados Esperados

### Teorema Central do Limite
- ✅ Convergência para distribuição normal conforme $n$ aumenta
- ✅ Melhor aproximação com $n = 50$ comparado a $n = 5$
- ✅ Validação via Q-Q plot e testes estatísticos

### Intervalos de Confiança (95%)
- ✅ Taxa de cobertura ≈ 95%
- ✅ Amplitude dos intervalos decresce com maior tamanho amostral
- ✅ Validação da relação entre nível de confiança e largura do intervalo

### ANOVA
- ✅ Teste de igualdade de médias entre grupos
- ✅ Cálculo de F-statistic e p-value
- ✅ Visualização de distribuições por grupo

---

## 📂 Saídas Geradas

### Arquivos CSV
| Arquivo | Descrição | Linhas |
|---------|-----------|--------|
| `01_estatisticas_dados_reais.csv` | Estatísticas descritivas dos dados reais | 1 |
| `02_tcl_resultados.csv` | Resultados do TCL para n=5 e n=50 | Múltiplas |
| `03_ic_resumo.csv` | Resumo dos intervalos de confiança | 1 |
| `03_ic_amostra_1000.csv` | Amostra de 1.000 intervalos | 1.001 |
| `04_anova_resumo.csv` | Resultado do teste ANOVA | 1 |
| `04_estatisticas_por_grupo.csv` | Estatísticas por grupo | 2+ |
| `parametros_completos.csv` | Consolidação de todos os parâmetros | Múltiplos |
| `relatorio_dados_detalhado.csv` | Documentação automática dos CSVs | 8 |

### Arquivos PNG (Imagens - 300 dpi)
| Arquivo | Descrição |
|---------|-----------|
| `01_distribuicao_dados_reais.png` | Histograma + Q-Q plot dos dados |
| `02_tcl_histograma_n5.png` | Distribuição das médias (n=5) |
| `02_tcl_histograma_n50.png` | Distribuição das médias (n=50) |
| `02_tcl_qqplot_n5.png` | Q-Q plot vs normal (n=5) |
| `02_tcl_qqplot_n50.png` | Q-Q plot vs normal (n=50) |
| `03_ic_intervalos_amostra.png` | Primeiros 100 intervalos |
| `03_ic_distribuicao_limites.png` | Distribuição dos limites |
| `04_anova_distribuicao_histograma.png` | Histograma da distribuição |
| `04_anova_estatisticas_tabela.png` | Tabela de estatísticas |

---

## 🔍 Verificação de Integridade

Todos os arquivos de saída são gerados automaticamente com:
- ✅ Delimitador: `;` (semicolon)
- ✅ Codificação: UTF-8 com BOM
- ✅ Decimal: `.` (ponto)
- ✅ Imagens: PNG 300 dpi
- ✅ Validação: Sem dados corrompidos

---

## 📚 Conceitos Teóricos

### Teorema Central do Limite (TCL)
Demonstra que a distribuição das médias amostrais converge para uma distribuição normal, independentemente da distribuição original da população.

$$\sqrt{n} \left(\bar{X}_n - \mu\right) \xrightarrow{d} N(0, \sigma^2)$$

### Intervalos de Confiança (IC)
Intervalo de estimação que contém o parâmetro populacional com probabilidade $\alpha$ (e.g., 95%).

$$IC: \left[\bar{X} - z_{\alpha/2} \frac{\sigma}{\sqrt{n}}, \bar{X} + z_{\alpha/2} \frac{\sigma}{\sqrt{n}}\right]$$

### Análise de Variância (ANOVA)
Teste estatístico para verificar se há diferenças significativas entre as médias de grupos.

$$F = \frac{MS_{between}}{MS_{within}}$$

---

## 📝 Notas Importantes

1. **Dados Reais:** A análise utiliza uma amostra de 100.000 registros de um total de 8.3 milhões
2. **Distribuição Assimétrica:** Os dados possuem distribuição não-normal, o que valida ainda mais o uso do TCL
3. **Single Group ANOVA:** Com apenas 1 estado (MG), a análise ANOVA é adaptada para gerar visualizações descritivas
4. **Reprodutibilidade:** Execute novamente o notebook para gerar novas análises (com diferentes amostras aleatórias)

---

## 👤 Autor

**Leonardo Vieira Guimarães**  
Doutorado em Planejamento e Análise Estatística de Experimentos  
CEFET-MG

---

## 📜 Licença

Este projeto é parte do programa de Doutorado em Engenharia e não possui restrições de uso interno.

---

## 📞 Suporte

Para dúvidas ou problemas:
1. Verifique se todas as dependências estão instaladas (`pip install -r requirements.txt`)
2. Limpe a saída dos notebooks e execute novamente
3. Certifique-se de que tem espaço em disco suficiente (>2 GB recomendado)

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

---

## 🎓 TRABALHO FINAL: ANÁLISE COM DADOS REAIS

### 📌 Objetivo

O **Estudo Dirigido 3** é a preparação para o **Trabalho Final**, que consiste em:

✅ **Aplicar todos os conceitos aprendidos nos Estudos Dirigidos 1 e 2**  
✅ **Analisar dados reais utilizando técnicas estatísticas avançadas**  
✅ **Gerar relatório completo com interpretação dos resultados**  

### 🔍 Escopo do Trabalho Final

A partir deste estudo dirigido, você irá:

1. **Selecionar um conjunto de dados reais** (pode ser dos dados GTA ou outro dataset)
2. **Aplicar todas as técnicas aprendidas**:
   - Análise exploratória de dados
   - Testes de normalidade
   - Teorema Central do Limite
   - Intervalo de Confiança
   - Análise de Variância (ANOVA)
   - Regressão Linear (se aplicável)
   - Testes de hipóteses

3. **Gerar visualizações** para comunicar os resultados
4. **Escrever relatório técnico** com:
   - Descrição dos dados
   - Metodologia utilizada
   - Resultados e discussão
   - Conclusões e interpretações

### 📋 Próximos Passos

1. ✅ Completar este Estudo Dirigido 3
2. 📝 Revisar os conceitos dos Estudos Dirigidos 1 e 2
3. 🔧 Preparar o ambiente (notebooks, bibliotecas, dados)
4. 🎯 Iniciar o Trabalho Final com dados reais

### 💡 Dicas

- Revise regularmente os conceitos teóricos
- Execute os notebooks e experimente com os parâmetros
- Tente reproduzir os resultados com diferentes dados
- Documente suas análises e descobertas
- Consulte a literatura sobre interpretação de resultados

---

**Sucesso em seu trabalho final! 🚀**

