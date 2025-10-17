# 📊 Sistema de Análise de Dados CSV

Este projeto fornece ferramentas completas para análise de arquivos CSV, incluindo análise de informações básicas e análise fuzzy avançada.

## 🎯 Funcionalidades teste

### 📋 Análise de Informações (`informacao.ipynb`)
- **Informações básicas**: tamanho, dimensões, tipos de dados
- **Análise de qualidade**: dados faltantes, duplicatas
- **Estatísticas descritivas**: resumo de variáveis numéricas
- **Relatórios**: geração de relatórios detalhados
- **Visualização**: interface organizada e intuitiva

### 🔬 Análise Fuzzy (`analise_fuzzy.py`)
- **Fuzzy C-Means**: clustering com lógica fuzzy
- **Métricas de qualidade**: FPC, função objetivo
- **Visualizações**: gráficos dos clusters e pertinências
- **Análise múltipla**: processamento de vários arquivos
- **Configuração flexível**: parâmetros personalizáveis

### 🚀 Exemplos de Uso (`exemplo_uso.py`)
- **Dados de demonstração**: criação automática de datasets
- **Tutoriais interativos**: exemplos práticos
- **Menu de opções**: interface amigável
- **Casos de uso**: cenários reais de aplicação

## 📁 Estrutura do Projeto

```
ProjetoDoutorado/
├── 📓 informacao.ipynb          # Notebook principal (análise de informações)
├── 🔬 analise_fuzzy.py          # Módulo de análise fuzzy
├── 🚀 exemplo_uso.py            # Exemplos e tutoriais
├── 📖 README.md                 # Documentação (este arquivo)
├── 📊 data/                     # Diretório para arquivos CSV
│   ├── vendas.csv               # Dados de exemplo (criados automaticamente)
│   ├── sensores.csv             # Dados de exemplo (criados automaticamente)
│   └── clientes.csv             # Dados de exemplo (criados automaticamente)
└── 📄 resultados/               # Resultados das análises (criado automaticamente)
```

## 🔧 Instalação e Configuração

### Pré-requisitos

```bash
# Instalar Python 3.8+
python --version

# Instalar dependências básicas
pip install pandas numpy matplotlib seaborn scikit-learn

# Para análise fuzzy (opcional)
pip install scikit-fuzzy

# Para notebooks Jupyter
pip install jupyter ipykernel
```

### Instalação Rápida

```bash
# Clonar/baixar o projeto
# Navegar até o diretório
cd ProjetoDoutorado

# Instalar todas as dependências
pip install pandas numpy matplotlib seaborn scikit-learn scikit-fuzzy jupyter

# Executar exemplo
python exemplo_uso.py
```

## 📚 Como Usar

### 1. 📊 Análise de Informações (Notebook)

```python
# Abrir o notebook
jupyter notebook informacao.ipynb

# Executar a análise
resultado = analisar_informacoes_csv(
    data_dir='data',
    mostrar_detalhes=True,
    salvar_relatorio=True
)

# Visualizar resultados
print(resultado)
```

### 2. 🔬 Análise Fuzzy (Script Python)

```python
from analise_fuzzy import fuzzy_cmeans_analise

# Análise fuzzy básica
resultado = fuzzy_cmeans_analise(
    filepath='data/meu_arquivo.csv',
    colunas=['var1', 'var2', 'var3'],
    n_clusters=3
)

# Análise com parâmetros avançados
resultado = fuzzy_cmeans_analise(
    filepath='data/meu_arquivo.csv',
    colunas=['var1', 'var2'],
    n_clusters=4,
    metodo_normalizacao='standard',
    m=2.5,
    mostrar_graficos=True
)
```

### 3. 🚀 Exemplos Interativos

```bash
# Executar menu interativo
python exemplo_uso.py

# Criar dados de exemplo
python -c "from exemplo_uso import criar_dados_exemplo; criar_dados_exemplo()"
```

## 🎯 Exemplos Práticos

### Exemplo 1: Análise Básica de Informações

```python
# No notebook informacao.ipynb
resultado = analisar_informacoes_csv()

# Saída esperada:
# ✅ Encontrados 3 arquivos CSV
# 📁 Analisando: vendas.csv
# 📊 Tamanho: 0.05 MB
# 📏 Dimensões: 200 linhas × 7 colunas
# ...
```

### Exemplo 2: Análise Fuzzy Avançada

```python
from analise_fuzzy import fuzzy_cmeans_analise

resultado = fuzzy_cmeans_analise(
    filepath='data/clientes.csv',
    colunas=['idade', 'renda', 'gastos'],
    n_clusters=3,
    mostrar_graficos=True
)

# Acessar resultados
print(f"FPC: {resultado['fpc']:.3f}")
print(f"Iterações: {resultado['iteracoes']}")
```

### Exemplo 3: Análise Múltipla

```python
from analise_fuzzy import analisar_multiplos_arquivos_fuzzy

colunas_especificas = {
    'vendas.csv': ['quantidade', 'preco', 'receita'],
    'sensores.csv': ['temperatura', 'umidade', 'pressao'],
    'clientes.csv': ['idade', 'renda', 'gastos']
}

resultados = analisar_multiplos_arquivos_fuzzy(
    data_dir='data',
    colunas_por_arquivo=colunas_especificas,
    n_clusters=3
)
```

## 📈 Funcionalidades Detalhadas

### 📊 Análise de Informações

| Funcionalidade | Descrição |
|---------------|-----------|
| **Informações Básicas** | Tamanho, dimensões, tipos de dados |
| **Qualidade dos Dados** | Dados faltantes, duplicatas |
| **Estatísticas** | Média, mediana, desvio padrão |
| **Relatórios** | Exportação para arquivo de texto |
| **Visualização** | Interface organizada e clara |

### 🔬 Análise Fuzzy

| Parâmetro | Descrição | Padrão |
|-----------|-----------|---------|
| `n_clusters` | Número de clusters | 3 |
| `m` | Parâmetro de fuzziness | 2.0 |
| `error` | Critério de parada | 0.005 |
| `maxiter` | Iterações máximas | 1000 |
| `metodo_normalizacao` | Normalização dos dados | 'minmax' |

### 📊 Métricas de Qualidade

- **FPC (Fuzzy Partition Coefficient)**: Mede a separação dos clusters
  - FPC > 0.7: Excelente separação
  - FPC > 0.5: Boa separação
  - FPC ≤ 0.5: Separação moderada

## 🛠️ Personalização

### Modificar Parâmetros de Análise

```python
# Análise de informações personalizada
resultado = analisar_informacoes_csv(
    data_dir='minha_pasta',
    mostrar_detalhes=False,  # Análise rápida
    salvar_relatorio=True    # Salvar relatório
)

# Análise fuzzy personalizada
resultado = fuzzy_cmeans_analise(
    filepath='meu_arquivo.csv',
    colunas=['col1', 'col2'],
    n_clusters=5,
    m=2.5,
    error=0.001,
    maxiter=2000,
    metodo_normalizacao='standard'
)
```

### Adicionar Novos Tipos de Análise

```python
# Exemplo: função personalizada
def minha_analise_personalizada(df):
    # Sua lógica aqui
    return resultado

# Integrar com o sistema existente
# (adicionar ao notebook ou criar novo módulo)
```

## 🔍 Solução de Problemas

### Problemas Comuns

1. **Erro: "Diretório 'data' não encontrado"**
   - Solução: Criar pasta `data` e colocar arquivos CSV
   - Ou usar `criar_dados_exemplo()` para gerar dados de teste

2. **Erro: "scikit-fuzzy não instalado"**
   - Solução: `pip install scikit-fuzzy`

3. **Erro: "Nenhuma coluna numérica encontrada"**
   - Solução: Verificar se o arquivo CSV tem colunas numéricas
   - Ou especificar colunas manualmente

4. **Gráficos não aparecem**
   - Solução: Instalar `matplotlib` e `seaborn`
   - Verificar se está usando ambiente gráfico

### Logs e Depuração

```python
# Ativar logs detalhados
import logging
logging.basicConfig(level=logging.DEBUG)

# Verificar dados carregados
df = pd.read_csv('data/meu_arquivo.csv')
print(df.info())
print(df.describe())
```

## 📊 Resultados e Saídas

### Arquivos Gerados

- `relatorio_csv_YYYYMMDD_HHMMSS.txt`: Relatório detalhado
- `fuzzy_resultado_ARQUIVO.csv`: Dados com clusters fuzzy
- Gráficos: Visualizações dos clusters e pertinências

### Estrutura dos Resultados

```python
# Resultado da análise fuzzy
resultado = {
    'dados_originais': DataFrame,
    'dados_com_clusters': DataFrame,
    'centros_normalizados': array,
    'centros_originais': array,
    'pertinencias': array,
    'labels': array,
    'fpc': float,
    'funcao_objetivo': list,
    'iteracoes': int,
    'scaler': Scaler,
    'colunas_utilizadas': list,
    'n_clusters': int
}
```

## 🚀 Extensões Futuras

### Funcionalidades Planejadas

- [ ] Análise de séries temporais
- [ ] Clustering hierárquico
- [ ] Análise de correlação avançada
- [ ] Interface web interativa
- [ ] Integração com bancos de dados
- [ ] Análise de texto (NLP)
- [ ] Machine Learning automatizado

### Como Contribuir

1. Fork do projeto
2. Criar branch para nova funcionalidade
3. Implementar e testar
4. Criar pull request
5. Documentar mudanças

## 📋 Checklist de Uso

### Antes de Começar
- [ ] Python 3.8+ instalado
- [ ] Dependências instaladas
- [ ] Pasta 'data' criada
- [ ] Arquivos CSV preparados

### Para Análise de Informações
- [ ] Notebook `informacao.ipynb` aberto
- [ ] Dados na pasta 'data'
- [ ] Executar células em sequência
- [ ] Verificar resultados

### Para Análise Fuzzy
- [ ] scikit-fuzzy instalado
- [ ] Arquivo `analise_fuzzy.py` importado
- [ ] Colunas numéricas identificadas
- [ ] Parâmetros configurados

## 📞 Suporte

### Documentação
- README.md (este arquivo)
- Comentários no código
- Docstrings das funções

### Contato
- Autor: Projeto Doutorado
- Data: 2025
- Versão: 1.0

## 📄 Licença

Este projeto é parte de um trabalho acadêmico de doutorado. Uso livre para fins educacionais e de pesquisa.

---

**🎯 Pronto para começar? Execute `python exemplo_uso.py` para iniciar!**
