# 📊 Representações de Grafos - Notebooks

Material completo sobre as **duas principais formas de representar grafos** computacionalmente: **Lista de Adjacência** e **Matriz de Adjacência**.

---

## 📋 Conteúdo

### 1️⃣ [Introdução às Representações](01_introducao_representacoes.ipynb)
**Objetivo**: Entender por que existem diferentes representações

**Tópicos**:
- Por que diferentes representações?
- Lista vs. Matriz: visão geral
- Comparação visual
- Grafos esparsos vs. densos
- Grafos ponderados
- Quando usar cada uma

**Pré-requisitos**: Notebooks básicos de teoria dos grafos  
**Tempo estimado**: 45-60 min

---

### 2️⃣ [Lista de Adjacência](02_lista_adjacencia.ipynb)
**Objetivo**: Implementação completa da lista de adjacência

**Tópicos**:
- Estrutura de dados (array + listas encadeadas)
- **Classe `Aresta`**: Representa arestas com peso
- **Classe `Celula`**: Nó da lista encadeada
- **Classe `Lista`**: Lista encadeada genérica
- **Classe `GrafoLista`**: Grafo completo
- Operações: inserir, remover, verificar, percorrer
- Análise de complexidade
- Implementação de BFS

**Complexidades**:
- Espaço: **O(V + E)**
- Inserir aresta: **O(1)**
- Verificar adjacência: **O(grau(v))**
- Listar vizinhos: **O(grau(v))**

**Pré-requisitos**: Notebook 1  
**Tempo estimado**: 60-90 min

---

### 3️⃣ [Matriz de Adjacência](03_matriz_adjacencia.ipynb)
**Objetivo**: Implementação completa da matriz de adjacência

**Tópicos**:
- Estrutura de dados (matriz V×V)
- **Classe `GrafoMatriz`**: Grafo completo
- Array `pos[]` para percorrer adjacências
- Operações: inserir, remover, verificar, percorrer
- Análise de complexidade
- Propriedades matemáticas da matriz
- Algoritmo Floyd-Warshall simplificado
- Comparação detalhada com Lista

**Complexidades**:
- Espaço: **O(V²)**
- Inserir aresta: **O(1)**
- Verificar adjacência: **O(1)** ✓✓
- Listar vizinhos: **O(V)**

**Pré-requisitos**: Notebooks 1-2  
**Tempo estimado**: 60-90 min

---

## 🚀 Como Usar

### 1. Iniciar Jupyter

```powershell
# Com uv:
uv run jupyter notebook

# Alternativa:
jupyter notebook
```

### 2. Navegue até `representacoes/` e abra os notebooks em ordem

---

## 📦 Dependências

As mesmas do projeto principal:
- **NetworkX** 3.5 (criação e análise)
- **Matplotlib** 3.10.7 (visualização)
- **NumPy** 2.3.4 (operações matriciais)
- **Jupyter** Lab 4.4.10

---

## 🎯 Ordem Recomendada

```
1. Introdução → 2. Lista de Adjacência → 3. Matriz de Adjacência
```

Cada notebook é progressivo e assume conhecimento dos anteriores.

---

## 📊 Comparação Rápida

| Aspecto | Lista de Adjacência | Matriz de Adjacência |
|---------|---------------------|----------------------|
| **Espaço** | O(V + E) ✓ | O(V²) |
| **Inserir aresta** | O(1) | O(1) |
| **Remover aresta** | O(grau) | O(1) ✓ |
| **Verificar adjacência** | O(grau) | O(1) ✓✓ |
| **Listar vizinhos** | O(grau) ✓ | O(V) |
| **Percorrer arestas** | O(V + E) ✓ | O(V²) |
| **Ideal para** | Grafos esparsos | Grafos densos |
| **Uso comum** | 90% dos casos | 10% dos casos |

---

## 💡 Regra de Ouro

> **Use Lista de Adjacência por padrão!**  
> Só use Matriz se:
> - Grafo é **muito denso** (|E| ≈ |V|²)
> - Precisa verificar adjacência com **muita frequência**
> - Está implementando **algoritmos matriciais** (Floyd-Warshall)

---

## 🔍 Exemplos de Aplicação

### Lista de Adjacência é melhor para:
- ✅ Redes sociais (grafos esparsos)
- ✅ Mapas rodoviários
- ✅ Grafos de dependências
- ✅ Algoritmos BFS, DFS, Dijkstra
- ✅ Árvores

### Matriz de Adjacência é melhor para:
- ✅ Grafos completos pequenos
- ✅ Floyd-Warshall (todos caminhos mínimos)
- ✅ Análise de alcançabilidade
- ✅ Multiplicação de matrizes
- ✅ Grafos densíssimos

---

## 📈 Exemplo Numérico

### Rede Social (esparso)
- **Vértices**: 1.000.000 usuários
- **Arestas**: 10.000.000 amizades
- **Lista**: 11M unidades (~44 MB) ✓
- **Matriz**: 1T unidades (~4 TB) ❌

### Torneio Completo (denso)
- **Vértices**: 100 times
- **Arestas**: 4.950 jogos
- **Lista**: 10K unidades
- **Matriz**: 10K unidades (similar!)
- **Vantagem Matriz**: O(1) nas consultas ✓

---

## 🔧 Classes Implementadas

### Lista de Adjacência
```python
class Aresta          # Representa aresta com peso
class Celula          # Nó da lista encadeada
class Lista           # Lista encadeada genérica
class GrafoLista      # Grafo completo
```

### Matriz de Adjacência
```python
class Aresta          # Mesma classe
class GrafoMatriz     # Grafo com matriz V×V
```

---

## 📚 Algoritmos Demonstrados

1. **BFS** (Busca em Largura) - Lista de Adjacência
2. **Floyd-Warshall** (Caminhos mínimos) - Matriz de Adjacência
3. **Percurso de adjacências** - Ambas
4. **Verificação de adjacência** - Ambas

---

## 🎓 Conceitos Aprendidos

- ✅ Trade-off **espaço** vs. **tempo**
- ✅ Complexidade **assintótica** vs. **constantes**
- ✅ Grafos **esparsos** vs. **densos**
- ✅ **Listas encadeadas** em Python
- ✅ **Operações matriciais** em NumPy
- ✅ **Análise de algoritmos** em grafos

---

## 🔗 Recursos Adicionais

- 📖 **CLRS**: "Introduction to Algorithms" - Cap. 22 (Grafos)
- 📘 **Sedgewick**: "Algorithms" - Graph representations
- 🌐 **NetworkX Docs**: https://networkx.org/
- 📺 **MIT OCW**: 6.006 - Graph representations

---

## 🤝 Exercícios Propostos

1. Implementar DFS usando lista de adjacência
2. Comparar performance de BFS em lista vs. matriz
3. Implementar detecção de ciclos
4. Converter lista ↔ matriz dinamicamente
5. Implementar grafo direcionado com ambas representações
6. Otimizar verificação de adjacência em lista (hash)

---

## 📄 Licença

MIT License - Uso educacional livre

---

**🎯 Bons estudos!**

*"A escolha da estrutura de dados correta pode fazer a diferença entre O(1) e O(V)."*
