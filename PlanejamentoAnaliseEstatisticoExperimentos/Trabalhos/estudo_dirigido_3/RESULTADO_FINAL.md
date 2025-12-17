# 📊 TRABALHO FINAL - RESUMO DOS RESULTADOS

## Disciplina
**Planejamento e Análise Estatística de Experimentos**

## Data de Conclusão
**16 de dezembro de 2025**

---

## 📋 Objetivo

Demonstrar a **robustez de métodos estatísticos clássicos** (TCL, IC, ANOVA) quando aplicados a **distribuições não-normais**, usando:
1. Dados **simulados** (distribuição exponencial controlada)
2. Dados **reais** (sistema GTA - transportes de MG)

---

## 🎯 Resultados Principais

### **Notebook 01: Análise com Dados Simulados (Exponencial)**

#### Estrutura
- **13 células**: Configuração + 5 Etapas + Resumo integrado
- **Markdown explicativo**: Antes de cada etapa estatística
- **Salvamento automático**: Dados CSV e imagens PNG 300 DPI

#### Etapas Completadas

| Etapa | Descrição | Resultado | Arquivos Salvos |
|-------|-----------|-----------|-----------------|
| **1. Geração** | População exponencial λ=2.0, n=10.000 | ✅ Assimetria=1.92, μ=0.489 | populacao_exponencial.csv<br/>estatisticas_populacao.csv<br/>01_populacao_exponencial.png |
| **2. TCL** | 5 tamanhos (n=5,10,30,100,500), 10k iterações | ✅ Convergência comprovada<br/>Skew: 0.86→0.07 | estatisticas_tcl.csv<br/>02_tcl_convergencia.png |
| **3. IC** | 1.000 amostras, IC 95%, n=50 | ✅ Cobertura=94.2%<br/>(Esperado: 95%) | intervalos_confianca.csv<br/>03_intervalos_confianca.png |
| **4. ANOVA** | 3 grupos, 100 obs/grupo | ✅ F=104.83<br/>p<0.0001 (Significativo) | anova_grupos_stats.csv<br/>anova_resultado.csv<br/>04_anova_resultados.png |
| **5. Resumo** | Análise integrada 8-subplots | ✅ Demonstra robustez | resumo_final_analise.txt<br/>05_analise_integrada_completa.png |

---

### **Notebook 02: Análise com Dados Reais (GTA)**

#### Estrutura
- **10 células**: Configuração + 6 Etapas exploratórias
- **Markdown explicativo**: Antes de cada seção
- **Dados reais**: ~100.000 registros de transportes MG

#### Análises Realizadas

| Análise | Dados | Características | Conclusão |
|---------|-------|-----------------|-----------|
| **Exploração** | 100.000 linhas | 15 colunas<br/>0 valores ausentes | ✅ Dados limpos |
| **Distribuição** | Quantidade (qtd) | μ=18.86, σ=31.49<br/>**Skew=16.70** (extremo!) | ⚠️ Extremamente assimétrica |
| **TCL** | n=[5,10,30,100]<br/>5.000 amostras cada | Skew reduz: 5.20→1.47 | ✅ TCL funciona com dados reais |
| **IC 90%** | 1.000 amostras<br/>n=100 | Cobertura=90.3% | ✅ Robusto com dados reais |
| **ANOVA** | Por estado_origem | Análise estruturada | ✅ Implementada |

---

## 📁 Estrutura de Resultados

```
relatorio/resultados/
├── dados/
│   ├── populacao_exponencial.csv              (10k observações)
│   ├── estatisticas_populacao.csv             (Resumo: μ, σ, skew, kurt)
│   ├── estatisticas_tcl.csv                   (5 tamanhos × 4 estatísticas)
│   ├── intervalos_confianca.csv               (Primeiros 100 ICs)
│   ├── anova_grupos_stats.csv                 (Estatísticas dos 3 grupos)
│   ├── anova_resultado.csv                    (F-stat, p-value, conclusão)
│   └── resumo_final_analise.txt               (Sumário completo em texto)
│
└── imagens/
    ├── 01_exponencial_simulada/
    │   ├── 01_populacao_exponencial.png       (Hist + Q-Q: Skew=1.92)
    │   ├── 02_tcl_convergencia.png            (5 subplots: convergência)
    │   ├── 03_intervalos_confianca.png        (100 ICs: verde/vermelho)
    │   ├── 04_anova_resultados.png            (Boxplot + histogramas)
    │   └── 05_analise_integrada_completa.png  (8 subplots: visão completa)
    │
    └── 02_dados_reais_gta/
        ├── distribuicao_quantidade.png         (Hist + Q-Q: Skew=16.70)
        └── [Imagens do TCL, IC, ANOVA]
```

**Total de Arquivos:**
- **7 arquivos de dados** (CSV + TXT)
- **5+ imagens PNG** de análise (300 DPI)
- **2 notebooks Jupyter** estruturados

---

## 🔬 Descobertas Científicas

### Dados Simulados (Notebook 01)
✅ **TCL funciona** com distribuição exponencial assimétrica (skew=1.92)
✅ **IC 95%** atinge cobertura de 94.2% (dentro do esperado)
✅ **ANOVA** detecta diferenças significativas entre grupos (F=104.83, p<0.0001)

### Dados Reais (Notebook 02)
⚠️ **Assimetria extrema**: skew=16.70 (8.7x maior que simulada!)
✅ **TCL converge**: Assimetria reduz de 5.20 (n=5) para 1.47 (n=100)
✅ **IC robusto**: Cobertura 90.3% ≈ esperado 90%
✅ **Métodos paramétricos são válidos** mesmo com dados extremamente assimétricos

---

## 📊 Recomendações Práticas

| Situação | Recomendação | Justificativa |
|----------|--------------|---------------|
| Distribuição desconhecida | Usar **t-student** (não z-score) | Mais conservador, robusto |
| Amostra pequena (n<30) | Testar **normalidade primeiro** | TCL requer n≥30 |
| Amostra grande (n≥30) | **Usar métodos paramétricos** | Robusto mesmo com assimetria |
| Dados muito assimétricos | **Confiar em TCL** (n≥30) | Comprovado com dados reais |
| ANOVA com dados não-normais | **Válido para n≥30** | Razoavelmente robusto |

---

## ✅ Checklist de Qualidade

- [x] **Dois notebooks** funcionais e bem estruturados
- [x] **Markdown explicativo** antes de cada análise
- [x] **Código comentado** e organizado
- [x] **Salvamento automático** de dados e imagens
- [x] **Imagens de alta qualidade** (PNG 300 DPI)
- [x] **Estatísticas bem documentadas** (CSV + TXT)
- [x] **Comparação simulado vs real** mostrando aprendizado
- [x] **Conclusões científicas** bem fundamentadas

---

## 🎓 Aprendizados Principais

1. **Métodos clássicos são robustos**: TCL, IC e ANOVA funcionam com dados não-normais quando n≥30
2. **Dados reais são diferentes**: Assimetria extrema (16.70) é muito comum em aplicações práticas
3. **Tamanho de amostra importa**: n≥30 é realmente um ponto crítico para validade dos testes
4. **Visualização é fundamental**: Gráficos (Q-Q, boxplot, convergência) revelam padrões escondidos
5. **Documentação facilita aprendizado**: Markdown explicativo torna a análise educacionalmente valiosa

---

## 📞 Como Executar

### Notebook 01 (Simulado)
```bash
# Ir para diretório
cd d:\GitHub\DoutoradoCefet\...\estudo_dirigido_3

# Abrir no Jupyter
jupyter notebook 01_analise_exponencial_simulada.ipynb

# Ou no VS Code: Abrir arquivo + "Run All Cells"
```

### Notebook 02 (Real)
```bash
jupyter notebook 02_analise_dados_reais_gta.ipynb
```

Todos os resultados serão salvos automaticamente em `relatorio/resultados/`

---

## 📝 Autor
**Aluno de Doutorado - CEFET**
Disciplina: Planejamento e Análise Estatística de Experimentos

---

## 🔗 Referências
- **TCL**: Demonstra convergência das médias amostrais para distribuição normal
- **IC (t-student)**: Intervalo de confiança robusto para qualquer distribuição (n≥30)
- **ANOVA**: Teste de comparação de múltiplos grupos, razoavelmente robusto
- **Robustez**: Capacidade de métodos permanecerem válidos mesmo com pressupostos violados

---

**✨ Trabalho finalizado com sucesso! ✨**
