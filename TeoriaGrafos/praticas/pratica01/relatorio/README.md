# Relatório da Prática 01 - LaTeX

Este diretório contém o relatório em LaTeX da 1ª Avaliação Prática.

## Estrutura

```
relatorio/
├── relatorio.tex          # Documento LaTeX principal
├── img/                   # Gráficos gerados pelo notebook
│   └── comparacoes_grafos_completos.png
├── resultados_10k.txt     # Resultados numéricos (10k vértices)
├── resultados_1M.txt      # Resultados numéricos (1M vértices)
└── README.md             # Este arquivo
```

## Como Compilar

### Opção 1: pdflatex (recomendado)

```bash
cd relatorio
pdflatex relatorio.tex
pdflatex relatorio.tex  # Executar 2x para resolver referências
```

### Opção 2: latexmk (automático)

```bash
cd relatorio
latexmk -pdf relatorio.tex
```

### Opção 3: Overleaf

1. Faça upload de `relatorio.tex` e da pasta `img/`
2. Compile diretamente no Overleaf

## Pré-requisitos

- Distribuição LaTeX instalada (TeX Live, MiKTeX, etc.)
- Pacotes necessários:
  - `inputenc`, `babel`, `graphicx`
  - `amsmath`, `listings`, `xcolor`
  - `hyperref`, `geometry`
  - `booktabs`, `caption`, `subcaption`

## Como Atualizar os Resultados

1. Execute o notebook `pratica01_experimentos.ipynb` completamente
2. Os gráficos serão salvos automaticamente em `relatorio/img/`
3. Os resultados numéricos serão salvos em `resultados_10k.txt` e `resultados_1M.txt`
4. Copie os valores dos arquivos `.txt` para a Tabela 1 no `relatorio.tex`:
   - Seção "Instâncias do Moodle"
   - Substitua `[PREENCHER]` pelos valores corretos

## Personalização

Edite as seguintes seções em `relatorio.tex`:

- **Linha 28**: Substitua `[Seu Nome]` pelo seu nome
- **Tabela 1** (linha ~220): Preencha os valores de comparações
- **Seção 4**: Adicione suas análises e observações

## Saída

Após compilar, você terá:
- `relatorio.pdf` - Documento final pronto para entrega

## Limpeza

Para remover arquivos temporários:

```bash
# Linux/Mac
rm -f *.aux *.log *.out *.toc *.bbl *.blg

# Windows (PowerShell)
Remove-Item *.aux,*.log,*.out,*.toc,*.bbl,*.blg
```
