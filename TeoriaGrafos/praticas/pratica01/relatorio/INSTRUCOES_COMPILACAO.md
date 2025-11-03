# Instruções de Compilação do Relatório

## Pré-requisitos

- **LaTeX**: Instalação completa (TeX Live, MiKTeX ou similar)
- **PDFLaTeX**: Compilador incluído nas distribuições LaTeX
- **Pacotes LaTeX necessários**:
  - inputenc, babel (brazilian)
  - graphicx, caption, subcaption
  - amsmath, booktabs
  - listings, xcolor
  - hyperref, geometry

## Compilação

### Opção 1: Linha de Comando

```bash
cd relatorio
pdflatex relatorio.tex
pdflatex relatorio.tex  # Segunda execução para referências cruzadas
```

### Opção 2: VS Code com LaTeX Workshop

1. Instale a extensão "LaTeX Workshop"
2. Abra `relatorio.tex`
3. Use `Ctrl+Alt+B` ou clique no botão "Build LaTeX project"

### Opção 3: Overleaf

1. Faça upload de:
   - `relatorio.tex`
   - Pasta `../implementacao/resultados/` (todas as imagens)
2. Compile online

## Estrutura de Arquivos

```
pratica01/
├── relatorio/
│   ├── relatorio.tex          # Documento principal
│   └── INSTRUCOES_COMPILACAO.md
└── implementacao/
    └── resultados/
        ├── dijkstra/
        │   └── img/
        │       ├── teste_comparacoes.png
        │       └── grafo_exemplo_n10.png
        ├── gulosa/
        │   └── img/
        │       └── teste_comparacoes.png
        └── comparacao/
            ├── teste_dijkstra_vs_gulosa.png
            └── instancias_grandes.png
```

## Resultado Esperado

O arquivo `relatorio.pdf` será gerado na pasta `relatorio/` com:

- Capa com título e autor
- Abstract
- 6 seções principais
- 5 figuras (gráficos e visualizações)
- 1 tabela (resultados das instâncias)
- Código fonte formatado com syntax highlighting
- Referências cruzadas numeradas automaticamente

## Troubleshooting

### Imagens não aparecem
- Verifique se os caminhos relativos estão corretos: `../implementacao/resultados/...`
- Certifique-se de que os arquivos PNG existem nos diretórios especificados

### Erros de compilação
- Execute `pdflatex` duas vezes para resolver referências cruzadas
- Instale pacotes faltantes (o compilador indicará quais)

### Caracteres especiais
- O arquivo usa UTF-8 encoding
- Certifique-se de que seu editor está configurado para UTF-8

## Notas

- O relatório foi preenchido com **dados reais** dos experimentos executados
- Todas as tabelas e gráficos correspondem aos resultados salvos em `implementacao/resultados/`
- Para atualizar os dados, execute novamente os notebooks e recompile o LaTeX
