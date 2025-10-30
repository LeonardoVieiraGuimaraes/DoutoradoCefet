# Instruções Completas - Prática 01

## 📂 Estrutura de Arquivos

```
praticas/pratica01/
├── pratica01_experimentos.ipynb  # Notebook principal (EXECUTAR ESTE)
├── relatorio/
│   ├── relatorio.tex             # Documento LaTeX
│   ├── README.md                 # Instruções de compilação
│   ├── .gitignore                # Ignora arquivos temporários do LaTeX
│   ├── img/                      # Gráficos (gerados automaticamente)
│   │   └── comparacoes_grafos_completos.png
│   ├── resultados_10k.txt        # Resultados numéricos (gerados)
│   └── resultados_1M.txt         # Resultados numéricos (gerados)
└── [arquivos auxiliares .py - removidos, tudo está no notebook]
```

## 🚀 Fluxo de Trabalho

### 1️⃣ Executar o Notebook

```bash
# Ativar ambiente virtual
cd d:\GitHub\DoutoradoCefet\TeoriaGrafos
uv sync  # ou source .venv/bin/activate

# Abrir notebook
jupyter notebook praticas/pratica01/pratica01_experimentos.ipynb
```

**No Jupyter:**
1. Execute todas as células na ordem (Run All)
2. Aguarde a execução dos benchmarks
3. Os gráficos serão salvos automaticamente em `relatorio/img/`
4. Os resultados numéricos serão salvos em arquivos `.txt`

### 2️⃣ Compilar o Relatório LaTeX

```bash
cd praticas/pratica01/relatorio
pdflatex relatorio.tex
pdflatex relatorio.tex  # Executar 2x para referências
```

**Ou usar latexmk (mais fácil):**
```bash
cd praticas/pratica01/relatorio
latexmk -pdf relatorio.tex
```

### 3️⃣ Completar o Relatório

Edite `relatorio/relatorio.tex`:

1. **Linha 28**: Substitua `[Seu Nome]` pelo seu nome
2. **Tabela 1** (Seção 3.2): Copie os valores de `resultados_10k.txt` e `resultados_1M.txt`:
   ```latex
   10.000 vértices    & 123456 & 234567 \\
   1.000.000 vértices & 9876543 & 8765432 \\
   ```
3. **Seção 4**: Adicione suas análises e discussões

### 4️⃣ Entregar

Enviar no Moodle:
- `relatorio.pdf` (documento compilado)
- `pratica01_experimentos.ipynb` (código-fonte comentado)

## 📊 O que o Notebook Faz

### Parte 1 - Dijkstra
- ✅ Implementação do algoritmo de Dijkstra com contagem de comparações
- ✅ Testes em grafos completos (n=4,9,14,...,50)
- ✅ Plotagem e salvamento automático do gráfico
- ✅ Teste na instância de 10k vértices
- ✅ Teste na instância de 1M vértices (opcional, RUN_LARGE=True)

### Parte 2 - Heurística Gulosa
- ✅ Implementação da heurística gulosa com contagem de comparações
- ✅ Mesmos testes da Parte 1
- ✅ Comparação lado a lado no mesmo gráfico

### Saídas Automáticas
- `relatorio/img/comparacoes_grafos_completos.png` - Gráfico Item 2.II.e e 3.II.e
- `relatorio/resultados_10k.txt` - Contagens Item 2.II.f e 3.II.f
- `relatorio/resultados_1M.txt` - Contagens Item 2.II.f e 3.II.f

## 🎯 Checklist de Entrega

- [ ] Notebook executado completamente
- [ ] Gráfico salvo em `relatorio/img/`
- [ ] Resultados numéricos capturados
- [ ] Nome inserido no `relatorio.tex`
- [ ] Tabela 1 preenchida com os valores corretos
- [ ] Análises adicionadas na Seção 4
- [ ] PDF compilado com sucesso
- [ ] Código-fonte comentado (já está no notebook)
- [ ] Arquivos enviados no Moodle

## ⚙️ Configurações Importantes

### Grafos Completos
- **Nmax atual**: 50 vértices (seguro para memória)
- **Para aumentar**: Edite célula 14 do notebook
- **Cuidado**: Grafos completos usam O(n²) memória!

### Instância 1M
- **Padrão**: Desativada (RUN_LARGE=False)
- **Para ativar**: Célula 18 do notebook, mude para `RUN_LARGE = True`
- **Requer**: ~4GB RAM disponível

## 🔧 Troubleshooting

### Erro: Arquivo não encontrado (instâncias)
- Verifique os caminhos no notebook (células 16 e 18)
- Caminhos atuais apontam para OneDrive

### Erro: Memória insuficiente
- Reduza `Nmax` no benchmark de grafos completos
- Não execute a instância de 1M se tiver <4GB RAM

### Erro: LaTeX não compila
- Instale pacotes faltantes: `tlmgr install [pacote]`
- Use Overleaf como alternativa online

## 📝 Observações

- Todos os comentários no código seguem as diretrizes do enunciado
- As implementações são autocontidas (sem dependências externas além de stdlib)
- A estrutura segue exatamente os itens da avaliação
- Os gráficos são salvos em alta resolução (300 DPI)
