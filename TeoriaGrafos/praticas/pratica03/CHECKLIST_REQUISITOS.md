# ✅ CHECKLIST - REQUISITOS DO TRABALHO PRÁTICO

**Disciplina:** Tópicos em Teoria dos Grafos  
**Professor:** Thiago de Souza Rodrigues  
**Data de Entrega:** 04 de janeiro de 2025  
**Status:** ✅ **COMPLETO E EXECUTADO**

---

## 📋 PARTE 1: FORÇA BRUTA

### ✅ Requisito 1.1 - Implementar Algoritmo de Força Bruta
- [x] Algoritmo que encontra todas as combinações de cores
- [x] Retorna o número cromático χ(G) exato
- [x] Localização: Seção 5 do notebook
- [x] Função: `algoritmo_forca_bruta_coloracao()`
- [x] Complexidade: O(k^n) - exponencial

**Validação:**
```python
# A função tenta com 1, 2, 3, ... cores até encontrar coloração válida
# Usa product() do itertools para gerar combinações
# Verifica se aresta (u,v) tem cores diferentes
```

---

### ✅ Requisito 1.2 - Gerar Instâncias Aleatórias
- [x] Tamanho: 5 a 13 vértices ✅
- [x] Geração automática e aleatória ✅
- [x] Não direcionados ✅
- [x] Não ponderados ✅
- [x] Sem loops ✅
- [x] Sem arestas paralelas ✅
- [x] Modelo: Erdős-Rényi G(n, p)

**Validação:**
```python
# Função: gerar_instancia_grafo_aleatorio()
# Usa nx.erdos_renyi_graph() - garante sem loops/arestas paralelas
# 3 instâncias por tamanho = 27 grafos totais (5-13 vértices)
```

---

### ✅ Requisito 1.3 - Medir Tempo de Execução
- [x] Tempo medido em cada instância ✅
- [x] 27 instâncias processadas ✅
- [x] Tempo agregado e por instância ✅
- [x] Dados salvos em CSV ✅

**Validação:**
```python
# Arquivo: resultados/parte1/csv/resultados_forca_bruta.csv
# Colunas: id_grafo, tamanho, numero_cromatico, tempo_segundos, arestas
```

---

### ✅ Requisito 1.4 - Gráfico de Crescimento Exponencial
- [x] Gráfico mostrando crescimento exponencial ✅
- [x] Eixo Y em escala logarítmica (semilogy) ✅
- [x] Eixo X com tamanho do grafo ✅
- [x] Intervalo min-max observado ✅
- [x] Arquivo PNG salvo em alta resolução ✅

**Validação:**
```python
# Arquivo: resultados/parte1/graficos/escalabilidade_forca_bruta.png
# Tipo: 2 gráficos (tempo vs tamanho + número cromático vs tamanho)
# Resolução: 150 dpi, formato PNG
```

---

## 📋 PARTE 2: HEURÍSTICA

### ✅ Requisito 2.1 - Implementar Heurística
- [x] Heurística implementada: **Welsh-Powell** ✅
- [x] Algoritmo guloso por grau decrescente ✅
- [x] Complexidade: O(n + m) - linear ✅
- [x] Localização: Seção 7 do notebook
- [x] Função: `algoritmo_welsh_powell()`

**Validação:**
```python
# Ordena vértices por grau decrescente
# Para cada vértice: atribui menor cor disponível
# Garante coloração válida (mas não necessariamente ótima)
```

---

### ✅ Requisito 2.2 - Aplicar em 5 Instâncias DIMACS
- [x] Instância a: 450 vértices, 8260 arestas ✅
- [x] Instância b: 864 vértices, 18707 arestas ✅
- [x] Instância c: 1000 vértices, 14378 arestas ✅
- [x] Instância d: 1916 vértices, 12506 arestas ✅
- [x] Instância e: 4730 vértices, 286722 arestas ✅
- [x] Leitura automática de arquivos DIMACS ✅
- [x] Função: `processar_instancias_dimacs()`

**Validação:**
```python
# Função ler_arquivo_dimacs() parseia formato DIMACS
# Linhas 'c': ignoradas (comentários)
# Linha 'p edge <n> <m>': dimensões
# Linhas 'e <u> <v>': arestas
```

---

### ✅ Requisito 2.3 - Verificar Número de Cores
- [x] Cores encontradas por heurística registradas ✅
- [x] Uma cor por instância ✅
- [x] Dados salvos em CSV ✅
- [x] Visualizações salvas (se n ≤ 500) ✅

**Validação:**
```python
# Arquivo: resultados/parte2/csv/resultados_heuristica.csv
# Colunas: instancia_id, cores_heuristica, tempo_segundos, 
#          num_vertices, num_arestas, densidade, grau_medio
```

---

### ✅ Requisito 2.4 - Gráficos de Análise
- [x] Gráfico 1: Cores por instância (bar chart) ✅
- [x] Gráfico 2: Tempo de execução (bar chart) ✅
- [x] Gráfico 3: Vértices vs Cores (scatter) ✅
- [x] Gráfico 4: Densidade vs Cores (scatter) ✅
- [x] Arquivo PNG salvo em alta resolução ✅

**Validação:**
```python
# Arquivo: resultados/parte2/graficos/analise_heuristica.png
# 4 subgráficos (2x2) com análises detalhadas
# Resolução: 150 dpi, formato PNG
```

---

## 📦 ENTREGÁVEIS

### ✅ Código Fonte
- [x] Arquivo principal: `solucao_coloracao_completa.ipynb` ✅
- [x] Código comentado e documentado ✅
- [x] 32 células estruturadas ✅
- [x] Docstrings em todas as funções ✅
- [x] Type hints em todos os parâmetros ✅

**Funções Principais:**
1. `extrair_parametros_grafo()` - Extrai métricas
2. `visualizar_e_salvar_grafo()` - Cria PNG do grafo
3. `ler_arquivo_dimacs()` - Parser DIMACS
4. `gerar_instancia_grafo_aleatorio()` - Gerador ER
5. `algoritmo_forca_bruta_coloracao()` - Força bruta **[REQUISITO 1.1]**
6. `processar_instancias_por_tamanho()` - Pipeline Parte 1 **[REQUISITO 1.2, 1.3]**
7. `algoritmo_welsh_powell()` - Heurística **[REQUISITO 2.1]**
8. `processar_instancias_dimacs()` - Pipeline Parte 2 **[REQUISITO 2.2, 2.3]**
9. `salvar_resultados_csv_parte1()` - Exportação CSV
10. `salvar_resultados_csv_parte2()` - Exportação CSV
11. `gerar_graficos_parte1()` - Gráficos **[REQUISITO 1.4]**
12. `gerar_graficos_parte2()` - Gráficos **[REQUISITO 2.4]**
13. `executar_solucao_completa()` - Orquestração

---

### ✅ Arquivos Gerados (Resultados)

#### Parte 1 - Força Bruta:
- [x] `resultados/parte1/csv/parametros_grafos.csv` (27 linhas)
- [x] `resultados/parte1/csv/resultados_forca_bruta.csv` (27 linhas)
- [x] `resultados/parte1/grafos/grafo_n05_i01.png` ... `grafo_n13_i03.png` (27 arquivos)
- [x] `resultados/parte1/graficos/escalabilidade_forca_bruta.png` (2 gráficos)

#### Parte 2 - Heurística:
- [x] `resultados/parte2/csv/resultados_heuristica.csv` (5 linhas)
- [x] `resultados/parte2/grafos/instancia_a.png` ... `instancia_e.png` (até 5 arquivos)
- [x] `resultados/parte2/graficos/analise_heuristica.png` (4 gráficos)

---

### ✅ Relatório com Gráficos

**Gráfico 1 - Crescimento Exponencial (Força Bruta):**
- ✅ Mostra tempo vs tamanho em escala logarítmica
- ✅ Demonstra inviabilidade de força bruta para n > ~15
- ✅ Intervalo min-max por tamanho

**Gráfico 2 - Análise Heurística:**
- ✅ Cores encontradas por instância DIMACS
- ✅ Tempo de execução (muito mais rápido que força bruta)
- ✅ Correlações: vértices vs cores, densidade vs cores

---

## 📊 ESTATÍSTICAS EXECUTADAS

### Parte 1 - Força Bruta
- **Total de Instâncias:** 27 grafos
- **Tamanhos:** 5, 6, 7, 8, 9, 10, 11, 12, 13 vértices (3 cada)
- **Tempo Total:** Medido e registrado
- **χ(G) Exato:** Encontrado para cada grafo

### Parte 2 - Heurística
- **Total de Instâncias:** 5 grafos DIMACS (a-e)
- **Maiores Dimensões:** 4730 vértices, 286722 arestas
- **Tempo de Execução:** O(n+m) linear
- **Cores Encontradas:** 1 valor por instância

---

## ✅ RESUMO FINAL

| Requisito | Descrição | Status | Evidência |
|-----------|-----------|--------|-----------|
| 1.1 | Força Bruta | ✅ | Seção 5, função `algoritmo_forca_bruta_coloracao()` |
| 1.2 | Geração Aleatória | ✅ | Seção 4, função `gerar_instancia_grafo_aleatorio()` |
| 1.3 | Medir Tempo | ✅ | CSV: `resultados_forca_bruta.csv` |
| 1.4 | Gráfico Crescimento | ✅ | `escalabilidade_forca_bruta.png` |
| 2.1 | Heurística | ✅ | Seção 7, função `algoritmo_welsh_powell()` |
| 2.2 | 5 Instâncias | ✅ | Seção 9, função `processar_instancias_dimacs()` |
| 2.3 | Cores Encontradas | ✅ | CSV: `resultados_heuristica.csv` |
| 2.4 | Gráficos Análise | ✅ | `analise_heuristica.png` |
| Código | Comentado | ✅ | Arquivo `.ipynb` com docstrings |
| Relatório | Gráficos | ✅ | PNG em `resultados/*/graficos/` |

---

**🎓 TRABALHO VALIDADO E PRONTO PARA ENTREGA**

Todas as especificações do trabalho foram implementadas, testadas e executadas com sucesso.

Data de Validação: **1 de janeiro de 2026**  
Versão do Notebook: **32 células estruturadas e executadas**
