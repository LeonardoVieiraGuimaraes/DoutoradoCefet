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
pdflatex relatorio.tex  # Segunda execução para sumário e referências cruzadas
```

**Nota**: A segunda execução é **obrigatória** para gerar corretamente:
- Sumário (Table of Contents)
- Lista de Figuras
- Lista de Tabelas
- Referências cruzadas entre seções

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

- **Capa**: Título institucional completo
- **Página de Rosto**: Informações do trabalho e finalidade
- **Resumo (Abstract)**: Síntese dos objetivos e resultados
- **Sumário Automático**: 
  - Índice de Seções e Subseções
  - Lista de Figuras (5 figuras)
  - Lista de Tabelas (1 tabela)
- **Conteúdo Principal** (6 seções):
  1. Introdução
  2. Metodologia
  3. Resultados
  4. Análise e Discussão
  5. Conclusão
  6. Anexos
- **Figuras**: 5 gráficos e visualizações
- **Tabela**: Resultados das instâncias grandes
- **Código Fonte**: Formatado com syntax highlighting
- **Numeração**: Páginas iniciais em romano (i, ii, iii...), conteúdo em arábico (1, 2, 3...)
- **Referências Cruzadas**: Numeradas automaticamente

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
