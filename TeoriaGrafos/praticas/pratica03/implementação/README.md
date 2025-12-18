# Coloração de Vértices - Prática 03

Implementação da Prática 03 de Tópicos em Teoria dos Grafos - CEFET/MG

## 📋 Descrição

Este projeto implementa e analisa dois enfoques para o problema de **Coloração de Vértices**:

### Parte 1: Algoritmo de Força Bruta
- Implementação exaustiva para encontrar o **número cromático** de um grafo
- Testes de escalabilidade com grafos de 2 a 12 vértices
- Análise de crescimento temporal (linear e logarítmica)

### Parte 2: Algoritmos Heurísticos
- **Greedy (Welsh-Powell)**: Ordenação por grau decrescente
- **DSATUR**: Ordenação por grau de saturação
- Aplicação em 5 instâncias grandes (450 a 4.730 vértices)
- Análise comparativa de desempenho

## 🚀 Como Usar

### Opção 1: Executar via Script Python

```bash
cd implementação
python gerar_relatorio.py
```

Este script:
- ✅ Executa o notebook completo
- ✅ Gera todos os gráficos e relatórios
- ✅ Organiza os resultados em pastas estruturadas
- ✅ Exibe resumo dos arquivos gerados

### Opção 2: Executar Manualmente no Jupyter

```bash
cd implementação
jupyter notebook coloracao_vertices.ipynb
```

Em seguida, execute todas as células na ordem (`Cell` → `Run All Cells`).

## 📁 Estrutura de Saída

Após a execução, os resultados são organizados em:

```
relatorio/
├── parte_1_forca_bruta/
│   ├── 01_crescimento_temporal.png
│   │   └─ Gráficos de crescimento: escala linear e logarítmica
│   └── 02_resultados_forca_bruta.csv
│       └─ Tabela: tamanho, tempo médio, número cromático
│
└── parte_2_heuristica/
    ├── 01_comparacao_heuristicas.png
    │   └─ Gráficos comparativos: cores usadas e tempo de execução
    ├── 02_resultados_heuristicas.csv
    │   └─ Tabela: instância, Greedy, DSATUR com tempos
    ├── 03_analise_estatistica.csv
    │   └─ Análise: diferenças entre heurísticas e razões
    └── 04_grafo_teste_colorido.png
        └─ Visualização: colorações de força bruta, Greedy e DSATUR
```

## 📊 Resultados Esperados

### Parte 1: Força Bruta
- **11 instâncias** testadas (2 a 12 vértices)
- **Crescimento exponencial** observado
- **Número cromático** determinado com precisão

### Parte 2: Heurísticas
- **5 instâncias** de teste
- **Comparação** entre Greedy e DSATUR
- **Análise estatística** de desempenho

## 📦 Dependências

```
networkx==3.6.1
matplotlib==3.10.8
numpy==2.3.5
pandas==2.3.3
scipy==1.16.3
seaborn
jupyter
ipython
```

Instalar: `pip install -r requirements.txt`

## 🔧 Detalhes Técnicos

### Algoritmo de Força Bruta
```python
def numero_cromatico_forca_bruta(grafo):
    """Tenta colorações com k cores até encontrar válida"""
    for k in range(1, len(grafo) + 1):
        # Tenta todas as combinações de k cores
        # Retorna k se encontrar coloração válida
```

### DSATUR (Heurística)
```python
def coloracao_greedy_dsatur(grafo):
    """Ordena vértices por grau de saturação
    (número de cores diferentes em vizinhos)"""
    # Prioritiza vértices com maior saturação
```

## 📈 Precisão de Saída

- **Gráficos PNG**: Resolução 300 DPI (alta qualidade)
- **Valores CSV**: Precisão de 6 casas decimais
- **Nomes de arquivos**: Formato sequencial para fácil referência

## 💾 Salvamento Automático

Todos os arquivos são salvos **automaticamente** durante a execução:
- Diretórios criados se não existirem (`exist_ok=True`)
- Caminhos usando `os.path.join()` para compatibilidade
- Confirmação via print das operações

## ⚙️ Configurações

Éditar arquivo `coloracao_vertices.ipynb` para:
- Alterar tamanhos de grafos (Parte 1)
- Mudar quantidade de instâncias (Parte 2)
- Ajustar sementes aleatórias para reprodutibilidade
- Modificar estilos de gráficos (matplotlib)

## 📝 Notas

- ✅ Reprodutibilidade garantida com sementes fixas (42-46)
- ✅ Grafos aleatórios usam modelo Erdős-Rényi
- ✅ Instâncias sintéticas com 5 tamanhos variados
- ✅ Análise estatística com estatísticas descritivas

## 🐛 Troubleshooting

**Erro: "jupyter: comando não encontrado"**
```bash
pip install jupyter
```

**Erro: "No module named 'networkx'"**
```bash
pip install -r requirements.txt
```

**Notebook não executa**
- Verifique se Python 3.10+ está instalado
- Execute com: `jupyter notebook --debug`

## 👨‍💻 Autor

Prática 03 - Tópicos em Teoria dos Grafos
CEFET/MG - Doutorado

---

**Última atualização**: 2024
