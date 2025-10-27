# 🌳 Árvores - Notebooks

Material completo sobre **árvores** em teoria dos grafos, abrangendo desde definições básicas até conceitos avançados como centro e bicentro.

---

## 📋 Conteúdo

### 1️⃣ [Introdução às Árvores](01_introducao_arvores.ipynb)
**Objetivo**: Compreender as definições fundamentais de árvores

**Tópicos**:
- Definição: grafo conexo sem circuitos
- Árvores orientadas
- Distância entre vértices d(v,w)
- Aplicações práticas:
  - 🛣️ Construção de rodovias
  - 🌐 Redes de computadores
  - 🎮 Jogo da velha (árvore de estados)
  - 👨‍👩‍👧‍👦 Árvores genealógicas
- Verificação: é árvore?

**Pré-requisitos**: Conceitos básicos de grafos (terminologia)  
**Tempo estimado**: 60 min

---

### 2️⃣ [Propriedades de Árvores](02_propriedades_arvores.ipynb)
**Objetivo**: Explorar o teorema fundamental e propriedades equivalentes

**Tópicos**:
- **Teorema fundamental**: G é árvore ⇔ existe UM caminho entre cada par
- **5 definições equivalentes**:
  1. G é árvore (conexo + sem ciclos)
  2. G é conexo e tem n-1 arestas
  3. G tem n-1 arestas e sem ciclos
  4. Existe exatamente 1 caminho entre cada par
  5. Sem ciclos, e adicionar aresta cria exatamente 1 ciclo
- Propriedade n-1 arestas
- Soma dos graus: $\sum \text{grau}(v) = 2n - 2$
- Vértices pendentes (pelo menos 2)
- Construção incremental

**Pré-requisitos**: Notebook 1  
**Tempo estimado**: 75 min

---

### 3️⃣ [Árvores Enraizadas e Binárias](03_arvores_enraizadas_binarias.ipynb)
**Objetivo**: Estudar árvores com hierarquia e árvores binárias

**Tópicos**:
- **Árvore livre** vs. **árvore enraizada**
- Vértice raiz
- **Nível de um vértice**: distância da raiz
- **Altura**: comprimento do maior caminho da raiz
- **Vértice interno**: não-pendente (grau ≥ 2)
- **Árvore binária completa**:
  - Exatamente 1 vértice grau 2 (raiz)
  - Demais vértices: grau 1 ou 3
- **Proposição 1**: n sempre ímpar
- **Proposição 2**: $p = \frac{n+1}{2}$ (número de folhas)
- Relações: $n = 2^{h+1} - 1$, $p = 2^h$

**Pré-requisitos**: Notebooks 1-2  
**Tempo estimado**: 75 min

---

### 4️⃣ [Centro de um Grafo](04_centro_grafo.ipynb)
**Objetivo**: Encontrar o centro de árvores e grafos

**Tópicos**:
- **Excentricidade** $E(v)$: distância máxima de v
- **Raio** $r(G)$: mínima excentricidade
- **Diâmetro** $d(G)$: máxima excentricidade
- **Centro** $C(G)$: vértices com excentricidade mínima
- **Método de eliminação progressiva**:
  - Remover vértices pendentes iterativamente
  - Até restar 1 (centro) ou 2 (bicentro) vértices
- **Proposição**: Centro de árvore tem 1 ou 2 vértices
- **Proposição**: Remover pendentes preserva o centro
- Aplicação: escolha de líder em redes

**Pré-requisitos**: Notebooks 1-3  
**Tempo estimado**: 75 min

---

## 🚀 Como Usar

### 1. Iniciar Jupyter

```powershell
# Com uv:
uv run jupyter notebook

# Alternativa:
jupyter notebook
```

### 2. Navegue até `arvores/` e abra os notebooks em ordem

---

## 📦 Dependências

As mesmas do projeto principal:
- **NetworkX** 3.5 (manipulação de grafos)
- **Matplotlib** 3.10.7 (visualização)
- **NumPy** 2.3.4 (operações numéricas)
- **Jupyter** Lab 4.4.10

---

## 🎯 Ordem Recomendada

```
1. Introdução → 2. Propriedades → 3. Enraizadas/Binárias → 4. Centro
```

Cada notebook é progressivo e assume conhecimento dos anteriores.

---

## 📊 Resumo de Conceitos

### Definições Fundamentais

| Conceito | Definição |
|----------|-----------|
| **Árvore** | Grafo conexo sem circuitos |
| **n-1 arestas** | Árvore com n vértices tem exatamente n-1 arestas |
| **Caminho único** | Existe exatamente 1 caminho entre cada par de vértices |

### Árvores Enraizadas

| Conceito | Fórmula |
|----------|---------|
| **Nível** | $\text{nível}(v) = d(\text{raiz}, v)$ |
| **Altura** | $h = \max_{v} d(\text{raiz}, v)$ |
| **Folhas (binária completa)** | $p = \frac{n+1}{2} = 2^h$ |
| **Internos (binária completa)** | $i = \frac{n-1}{2} = 2^h - 1$ |

### Centro

| Conceito | Fórmula |
|----------|---------|
| **Excentricidade** | $E(v) = \max_{w} d(v, w)$ |
| **Raio** | $r(G) = \min_{v} E(v)$ |
| **Diâmetro** | $d(G) = \max_{v} E(v)$ |
| **Centro** | $C(G) = \{v : E(v) = r(G)\}$ |

---

## 🔑 Teoremas Principais

### Teorema 1: Definições Equivalentes

Para um grafo G(V,A) com n vértices, são **EQUIVALENTES**:
1. G é árvore
2. G é conexo e tem n-1 arestas
3. G tem n-1 arestas e sem ciclos
4. Existe exatamente 1 caminho entre cada par
5. Sem ciclos, e adicionar aresta cria exatamente 1 ciclo

### Teorema 2: Centro de Árvore

> O centro de uma árvore possui **1 ou 2 vértices**.
> - Se |C| = 1: **centro**
> - Se |C| = 2: **bicentro** (vértices adjacentes)

### Teorema 3: Preservação do Centro

> Remover vértices pendentes de uma árvore **preserva o centro**.

---

## 💡 Aplicações Práticas

### Construção de Infraestrutura
- ✅ Redes rodoviárias (minimizar custo)
- ✅ Distribuição elétrica
- ✅ Redes de água/esgoto
- ✅ Cabeamento de rede

### Estruturas de Dados
- ✅ Árvores binárias de busca
- ✅ Heaps (filas de prioridade)
- ✅ Tries (busca de strings)
- ✅ Sistemas de arquivos

### Tomada de Decisão
- ✅ Árvores de decisão (ML)
- ✅ Jogos (minimax)
- ✅ Planejamento (árvore de estados)

### Otimização
- ✅ Localização de centros de distribuição
- ✅ Escolha de líder em redes
- ✅ Posicionamento de servidores
- ✅ Roteamento eficiente

---

## 🧮 Algoritmos Implementados

### 1. Verificação de Árvore
- Checa se G é conexo
- Verifica ausência de ciclos
- Confirma m = n-1

### 2. Cálculo de Centro (Eliminação)
```python
ENQUANTO n > 2:
    Remover vértices pendentes
Retornar vértices restantes
```
**Complexidade**: O(n)

### 3. Cálculo de Excentricidades
- Calcular distâncias de v para todos w
- Tomar máximo
**Complexidade**: O(n²)

---

## 📈 Fórmulas Importantes

### Árvore Geral
- Arestas: $m = n - 1$
- Soma dos graus: $\sum \text{grau}(v) = 2(n-1)$
- Vértices pendentes: $\geq 2$ (se n ≥ 2)

### Árvore Binária Completa
- Total de vértices: $n = 2^{h+1} - 1$
- Folhas: $p = 2^h = \frac{n+1}{2}$
- Internos: $i = 2^h - 1 = \frac{n-1}{2}$
- Relação: $p = i + 1$
- n sempre **ímpar**

### Centro
- Raio: $r(G) \leq d(G) \leq 2r(G)$
- |C(árvore)| ∈ {1, 2}

---

## 🎓 Exercícios por Notebook

### Notebook 1
1. Criar árvore com 8 vértices (verificar 7 arestas)
2. Calcular todas as distâncias
3. Modelar hierarquia de empresa
4. Árvore de diretórios
5. Contar caminhos de comprimento k

### Notebook 2
1. Provar que remover aresta desconecta
2. Mostrar máximo n-2 vértices internos
3. Verificar adição de aresta → 1 ciclo
4. Demonstrar ≥ 2 vértices pendentes
5. Criar árvore com 5 pendentes

### Notebook 3
1. Provar máximo $2^h$ folhas
2. Criar binária completa com 15 vértices
3. Verificar $\sum \text{grau} = 2n-2$
4. Implementar cálculo de altura
5. Verificar $p - i = 1$

### Notebook 4
1. Provar $r(T) \leq d(T) \leq 2r(T)$
2. Centro único em caminho ímpar
3. Implementar eliminação iterativa
4. Árvore onde centro ≠ vértice de maior grau
5. Provar |C| = 2 → adjacentes
6. Árvore com 3 vértices na periferia
7. Centro de árvore genealógica

---

## 🔗 Recursos Complementares

### Livros
- 📖 **CLRS** - "Introduction to Algorithms" (Cap. 22)
- 📘 **Diestel** - "Graph Theory" (Cap. 1)
- 📗 **Bondy & Murty** - "Graph Theory"

### Online
- 🌐 **NetworkX Docs**: https://networkx.org/
- 📺 **MIT OCW**: 6.006 Graph Algorithms
- 🎓 **Khan Academy**: Tree structures

---

## 🎯 Objetivos de Aprendizagem

Ao completar este módulo, você será capaz de:

- ✅ Identificar e definir árvores formalmente
- ✅ Aplicar as 5 definições equivalentes
- ✅ Calcular propriedades (altura, centro, raio)
- ✅ Implementar algoritmos (verificação, centro)
- ✅ Modelar problemas reais com árvores
- ✅ Analisar complexidades de operações
- ✅ Trabalhar com árvores binárias
- ✅ Otimizar localização usando centro

---

## 📊 Estatísticas

- **Total de notebooks**: 4
- **Conceitos introduzidos**: ~25
- **Teoremas demonstrados**: 8+
- **Algoritmos implementados**: 5+
- **Visualizações**: 30+
- **Exercícios**: 35+
- **Tempo total estimado**: ~5 horas

---

## 📄 Licença

MIT License - Uso educacional livre

---

**🌳 Bons estudos!**

*"Uma árvore é o grafo mais simples que conecta todos os vértices - nem mais, nem menos."*
