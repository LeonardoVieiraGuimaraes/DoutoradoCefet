# Trabalho 02 - Árvores Binárias de Pesquisa e AVL

## Objetivos

### 1. Implementação de Árvore Binária de Pesquisa Sem Balanceamento
Implementar uma classe que realize a **INSERÇÃO** e a **BUSCA** de um elemento em uma Árvore Binária de Pesquisa Sem Balanceamento. A árvore deve possuir somente elementos inteiros.

### 2. Implementação de Árvore AVL
Implementar uma classe que realize a **INSERÇÃO** e a **BUSCA** de um elemento em uma Árvore AVL. A árvore deve possuir somente elementos inteiros.

## 3. Experimentos

### A. Para a Árvore Binária de Pesquisa Sem Balanceamento:

#### I. Experimento com Elementos Ordenados
- Gerar 10 árvores a partir de n elementos **ORDENADOS**
- n variando de 1.000 até 10.000, com intervalo de 1.000
- Em cada árvore gerada pesquisar pelo elemento 10.001
- Verificar o número de comparações realizadas

#### II. Experimento com Elementos Aleatórios
- Gerar 10 árvores a partir de n elementos **ALEATÓRIOS**
- n variando de 1.000 até 10.000, com intervalo de 1.000
- Em cada árvore gerada pesquisar pelo elemento 10.001
- Verificar o número de comparações realizadas

#### III. Gráfico BST - Inserções Ordenadas
Fazer um único gráfico de **n x número de comparações** levando em consideração as árvores geradas com inserções ordenadas.

### B. Para a Árvore AVL:

#### I. Experimento com Elementos Ordenados
- Gerar 10 árvores a partir de n elementos **ORDENADOS**
- n variando de 1.000 até 10.000, com intervalo de 1.000
- Em cada árvore gerada pesquisar pelo elemento 10.001
- Verificar o número de comparações realizadas

#### II. Experimento com Elementos Aleatórios
- Gerar 10 árvores a partir de n elementos **ALEATÓRIOS**
- n variando de 1.000 até 10.000, com intervalo de 1.000
- Em cada árvore gerada pesquisar pelo elemento 10.001
- Verificar o número de comparações realizadas

#### III. Gráfico AVL - Inserções Aleatórias
Fazer um único gráfico de **n x número de comparações** levando em consideração as árvores geradas com inserções aleatórias.

## 4. Análise dos Resultados
Explicar o comportamento dos gráficos gerados.

## Entregas

### Data da Entrega: 15/07/2025

### Relatório (via Moodle)
O relatório deve conter:
- Nome
- Gráfico do tópico 3.A.III (BST - Inserções Ordenadas)
- Gráfico do tópico 3.B.III (AVL - Inserções Aleatórias)
- Item 4 (Explicação do comportamento dos gráficos)

### Código Fonte (via Moodle)
- Código fonte brevemente comentado
- Linguagens aceitas: Java, C, C++ ou Python

## Estrutura do Projeto

```
Trabalho02/
├── readme.md                    # Este arquivo
├── bst.py                      # Implementação da BST
├── avl.py                      # Implementação da AVL
├── experimentos.py             # Scripts dos experimentos
├── resultados/                 # Pasta para resultados
│   ├── graficos/              # Gráficos gerados
│   └── dados/                 # Dados dos experimentos
└── relatorio.md               # Relatório final
```