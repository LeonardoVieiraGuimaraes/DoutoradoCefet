# 📚 Teoria dos Grafos - Notebooks Didáticos

Série completa de Jupyter Notebooks sobre **Teoria dos Grafos**, do básico ao avançado, com exemplos práticos usando **NetworkX**.

---

## 📋 Estrutura dos Notebooks

### 1️⃣ [Introdução e Motivação](01_introducao_motivacao.ipynb)
**Objetivo**: Entender o que são grafos e por que são úteis

**Tópicos**:
- O que é um grafo?
- Motivação e aplicações reais
- Definição formal: G = (V, E)
- Criando grafos com NetworkX
- Exercício prático: modelar rede social

**Pré-requisitos**: Nenhum  
**Tempo estimado**: 30-45 min

---

### 2️⃣ [Terminologia Básica](02_terminologia.ipynb)
**Objetivo**: Dominar os conceitos fundamentais

**Tópicos**:
- Adjacência de vértices
- Incidência de arestas
- Laços e arestas paralelas
- Subgrafos
- Operações básicas

**Pré-requisitos**: Notebook 1  
**Tempo estimado**: 45-60 min

---

### 3️⃣ [Tipos de Grafos](03_tipos_grafos.ipynb)
**Objetivo**: Conhecer diferentes categorias de grafos

**Tópicos**:
- Grafos simples
- Grafos direcionados (digrafos)
- Grafos completos (Kₙ)
- Grafos ciclo (Cₙ)
- Grafos roda (Wₙ)
- Fórmulas de contagem de arestas

**Pré-requisitos**: Notebooks 1-2  
**Tempo estimado**: 45-60 min

---

### 4️⃣ [Grafos Especiais](04_grafos_especiais.ipynb)
**Objetivo**: Estudar grafos com propriedades especiais

**Tópicos**:
- Grafos bipartidos (K_{m,n})
- Multigrafos
- Grafos ponderados
- Grafos planares
- Algoritmo de caminho mínimo (Dijkstra)

**Pré-requisitos**: Notebooks 1-3  
**Tempo estimado**: 60-75 min

---

### 5️⃣ [Grau e Teoremas](05_grau_teoremas.ipynb)
**Objetivo**: Entender propriedades fundamentais

**Tópicos**:
- Grau de vértices (grafos não direcionados)
- Grau de entrada/saída (digrafos)
- **Teorema do Aperto de Mãos** (Handshaking Theorem)
- Corolário: número par de vértices com grau ímpar
- Grafos regulares

**Pré-requisitos**: Notebooks 1-4  
**Tempo estimado**: 60-75 min

---

### 6️⃣ [O Problema de Königsberg](06_konigsberg.ipynb) 🌉
**Objetivo**: Resolver o problema que originou a Teoria dos Grafos!

**Tópicos**:
- Contexto histórico (1736, Euler)
- Modelagem do problema com grafos
- Caminhos e ciclos Eulerianos
- **Teorema de Euler**: condições para existência
- Aplicações modernas

**Pré-requisitos**: Notebooks 1-5 (especialmente 5)  
**Tempo estimado**: 60-90 min

---

## 🚀 Como Usar

### 1. Instalação das dependências

```bash
# Com uv (recomendado):
uv sync

# Alternativa com pip:
pip install networkx matplotlib jupyter numpy
```

### 2. Iniciar Jupyter

```bash
# Com uv:
uv run jupyter notebook

# Alternativa:
jupyter notebook
```

### 3. Navegue até a pasta `terminologia/` e abra o notebook desejado

---

## 📦 Dependências

- **Python** ≥ 3.10
- **NetworkX** ≥ 3.0 (manipulação de grafos)
- **Matplotlib** ≥ 3.5 (visualização)
- **NumPy** ≥ 1.21 (cálculos numéricos)
- **Jupyter** ≥ 1.0 (ambiente de notebooks)

---

## 🎯 Ordem Recomendada de Estudo

```
┌─────────────────────────────┐
│  1. Introdução e Motivação  │
└──────────┬──────────────────┘
           │
           ↓
┌─────────────────────────────┐
│   2. Terminologia Básica    │
└──────────┬──────────────────┘
           │
           ↓
┌─────────────────────────────┐
│    3. Tipos de Grafos       │
└──────────┬──────────────────┘
           │
           ↓
┌─────────────────────────────┐
│   4. Grafos Especiais       │
└──────────┬──────────────────┘
           │
           ↓
┌─────────────────────────────┐
│    5. Grau e Teoremas       │
└──────────┬──────────────────┘
           │
           ↓
┌─────────────────────────────┐
│ 6. Problema de Königsberg 🌉│
└─────────────────────────────┘
```

**📝 Nota**: Cada notebook pressupõe conhecimento dos anteriores!

---

## 💡 Dicas de Aprendizado

1. **Execute todas as células**: Não apenas leia, rode o código!
2. **Modifique os exemplos**: Experimente com diferentes parâmetros
3. **Faça os exercícios**: Estão no final de cada notebook
4. **Visualize**: Os grafos são visuais, use as visualizações para entender
5. **Consulte a documentação**: [NetworkX Docs](https://networkx.org/documentation/stable/)

---

## 🎓 Nível de Dificuldade

| Notebook | Dificuldade | Conceitos Chave |
|----------|-------------|-----------------|
| 1 | ⭐ Iniciante | Definições básicas |
| 2 | ⭐ Iniciante | Terminologia |
| 3 | ⭐⭐ Intermediário | Classificações |
| 4 | ⭐⭐ Intermediário | Propriedades especiais |
| 5 | ⭐⭐⭐ Avançado | Teoremas matemáticos |
| 6 | ⭐⭐⭐ Avançado | Problema clássico |

---

## 🔗 Recursos Adicionais

- 📖 **Livro**: Introduction to Graph Theory (Douglas West)
- 🌐 **NetworkX Tutorial**: https://networkx.org/documentation/stable/tutorial.html
- 📺 **Vídeos**: 3Blue1Brown - Discrete Math
- 🏫 **Curso Online**: Graph Theory on Coursera

---

## 🤝 Contribuições

Este material foi desenvolvido para fins educacionais. Sinta-se livre para:
- ✅ Sugerir melhorias
- ✅ Reportar erros
- ✅ Adicionar exemplos
- ✅ Criar exercícios adicionais

---

## 📄 Licença

MIT License - Uso educacional livre

---

**🎉 Bons estudos!** 

*"In mathematics you don't understand things. You just get used to them."* - John von Neumann
