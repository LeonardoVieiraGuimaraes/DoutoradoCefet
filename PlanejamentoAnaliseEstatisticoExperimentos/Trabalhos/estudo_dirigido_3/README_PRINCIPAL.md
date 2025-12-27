# 🎓 Estudo Dirigido 3 - Análise Estatística com Dados Reais

**Disciplina:** Planejamento, Análise Estatística e Experimentos  
**Instituição:** CEFET-MG  
**Aluno:** Leonardo Vieira Guimarães  
**Status:** ✅ Pronto para Análise

---

## 📌 Estrutura do Projeto

Análise estatística com **dados reais de tráfego urbano (GTA)**, aplicando conceitos aprendidos nos Estudos Dirigidos 1 e 2:
- **ED1:** Teorema Central do Limite (TCL) e Intervalos de Confiança
- **ED2:** ANOVA e Testes Post-Hoc
- **Trabalho Final:** Integração prática com dados reais

---

## 📁 Arquivos Principais

### 📌 Arquivos Ativos (Use Estes)

```
📄 informacao.ipynb              ← Função para explorar dados CSV
📊 02_analise_dados_reais_gta.ipynb  ← ANÁLISE PRINCIPAL DO PROJETO
📝 README_TRABALHO_FINAL.md      ← Guia metodológico completo
📋 requirements.txt              ← Dependências Python
```

### 📁 Diretórios Importantes

```
📂 relatorio/                    # Resultados e documentação final
   └── resultados/              # Gráficos e tabelas geradas

📂 _arquivos_antigos/           # Scripts de suporte e análises anteriores
   ├── 01_analise_exponencial_simulada.ipynb    (análise simulada)
   ├── ler_pdfs.py, ler_pdfs_avancado.py        (leitura de PDFs)
   ├── exemplo_uso_pdfs.py, verificar_instalacao.py
   └── pdfs_extraidos/          (textos dos PDFs extraídos)

📂 estudos_dirigidos_1.pdf       # PDF original ED1
📂 estudos_dirigidos_2.pdf       # PDF original ED2
```

---

## 🚀 Como Usar

### 1️⃣ Explorar os Dados

```bash
jupyter notebook informacao.ipynb
```

Mostra:
- Tamanho dos arquivos CSV
- Número de linhas e colunas
- Lista de variáveis disponíveis

### 2️⃣ Executar Análise Principal

```bash
jupyter notebook 02_analise_dados_reais_gta.ipynb
```

Realiza:
- ✅ Análise exploratória
- ✅ Teste de normalidade (TCL - ED1)
- ✅ Intervalos de confiança (ED1)
- ✅ ANOVA e comparações (ED2)
- ✅ Testes Post-Hoc
- ✅ Validação do TCL em dados reais

### 3️⃣ Consultar Metodologia

```bash
Leia: README_TRABALHO_FINAL.md
```

Documento com:
- Objetivos e metodologia
- Código comentado para cada fase
- Checklist de tarefas
- Interpretação de resultados

---

## 📊 Dados Utilizados

**Fonte:** `D:\OneDrive\Pessoais\Doutorado\Cefet\data\`

**Variáveis Esperadas:**
- `tempo_viagem` - Tempo de deslocamento (minutos)
- `distancia` - Distância percorrida (km)
- `velocidade_media` - Velocidade média (km/h)
- `horario` - Período do dia (pico/fora-de-pico)
- `dia_semana` - Dia da semana
- `condicao_climatica` - Condições do tempo
- `tipo_veiculo` - Classe do veículo

---

## 📚 Conceitos Aplicados

### Do Estudo Dirigido 1:
✅ Teorema Central do Limite (TCL)  
✅ Intervalos de Confiança  
✅ Distribuições Assimétricas  

### Do Estudo Dirigido 2:
✅ ANOVA (Um Fator, Dois Fatores)  
✅ Testes Post-Hoc (Tukey HSD)  
✅ Verificação de Pressupostos  

### Integração:
✅ Validação de TCL em dados reais  
✅ Construção de IC em populações reais  
✅ Comparação de grupos com ANOVA  
✅ Interpretação prática de resultados  

---

## 🔧 Instalação de Dependências

```bash
pip install pandas numpy scipy matplotlib seaborn statsmodels scikit-learn
```

---

## 📋 Checklist do Projeto

- [ ] Explorar dados com `informacao.ipynb`
- [ ] Ler `README_TRABALHO_FINAL.md` para metodologia
- [ ] Executar `02_analise_dados_reais_gta.ipynb`
- [ ] Gerar gráficos em `relatorio/resultados/`
- [ ] Documentar conclusões
- [ ] Revisar e validar análises

---

## 💾 Saída Esperada

Após executar as análises, você terá:

```
relatorio/resultados/
├── ESTRUTURA_SEPARADA.md          # Resumo dos achados
├── graficos/
│   ├── distribuicoes.png
│   ├── qq_plots.png
│   ├── anova_resultados.png
│   └── ...
└── tabelas/
    ├── estatisticas_descritivas.csv
    ├── testes_normalidade.csv
    ├── anova_table.csv
    └── ...
```

---

## 📖 Documentação de Referência

| Arquivo | Conteúdo |
|---------|----------|
| `README_TRABALHO_FINAL.md` | Metodologia completa com exemplos de código |
| `informacao.ipynb` | Função para exploração de dados CSV |
| `02_analise_dados_reais_gta.ipynb` | Notebook principal com todas as análises |
| `requirements.txt` | Dependências Python necessárias |

---

## 🎯 Fluxo de Trabalho

```
1. EXPLORAÇÃO
   └─> informacao.ipynb
   
2. LEITURA DE MÉTODOS
   └─> README_TRABALHO_FINAL.md
   
3. ANÁLISE
   └─> 02_analise_dados_reais_gta.ipynb
   
4. DOCUMENTAÇÃO
   └─> relatorio/ESTRUTURA_SEPARADA.md
```

---

## ✨ Status

| Componente | Status |
|-----------|--------|
| 📚 Estudos Dirigidos | ✅ Completo (ED1 + ED2) |
| 📊 Estrutura de Projeto | ✅ Organizado |
| 📖 Documentação | ✅ Pronto |
| 📈 Análise Principal | 🔄 Pronto para executar |
| 📋 Resultados | ⏳ A gerar |

---

## 📞 Próximos Passos

1. Execute `informacao.ipynb` para explorar dados
2. Leia `README_TRABALHO_FINAL.md` para entender metodologia
3. Execute `02_analise_dados_reais_gta.ipynb` para rodar análises
4. Verifique `relatorio/ESTRUTURA_SEPARADA.md` para resumo de resultados

---

**Versão:** 1.0 - Estrutura Organizada  
**Última atualização:** 27 de dezembro de 2025
