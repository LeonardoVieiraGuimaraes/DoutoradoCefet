"""
Exemplo de uso dos scripts de leitura de PDFs
"""

# Importar a classe ProcessadorPDF
import sys
from pathlib import Path

# Adicionar diretório ao path se necessário
sys.path.insert(0, str(Path(__file__).parent))

from ler_pdfs_avancado import ProcessadorPDF


def exemplo_basico():
    """Exemplo 1: Uso básico"""
    print("\n" + "="*80)
    print("EXEMPLO 1: Processamento Básico")
    print("="*80 + "\n")
    
    # Criar processador
    pdf = ProcessadorPDF('estudos_dirigidos_1.pdf')
    
    # Extrair todas as páginas
    if pdf.extrair_todas_paginas():
        print(f"✅ PDF processado com sucesso!")
        print(f"   Total de páginas: {pdf.metadados['total_paginas']}")
        print(f"   Título: {pdf.metadados['titulo']}")
        print(f"   Autor: {pdf.metadados['autor']}")
    else:
        print("❌ Erro ao processar PDF")


def exemplo_pagina_especifica():
    """Exemplo 2: Extrair página específica"""
    print("\n" + "="*80)
    print("EXEMPLO 2: Extrair Página Específica")
    print("="*80 + "\n")
    
    pdf = ProcessadorPDF('estudos_dirigidos_1.pdf')
    
    if pdf.extrair_todas_paginas():
        # Obter primeira página
        primeira_pagina = pdf.extrair_pagina_especifica(1)
        print("Primeiros 500 caracteres da página 1:")
        print(primeira_pagina[:500])
        print("...")


def exemplo_resumo():
    """Exemplo 3: Gerar resumo"""
    print("\n" + "="*80)
    print("EXEMPLO 3: Resumo do Documento")
    print("="*80 + "\n")
    
    pdf = ProcessadorPDF('estudos_dirigidos_1.pdf')
    
    if pdf.extrair_todas_paginas():
        # Gerar resumo (30 primeiras linhas por página)
        resumo = pdf.obter_resumo(linhas=30)
        print(resumo[:1000])  # Mostrar apenas os primeiros 1000 caracteres
        print("\n[... resumo continua ...]\n")


def exemplo_salvar():
    """Exemplo 4: Salvar em arquivo"""
    print("\n" + "="*80)
    print("EXEMPLO 4: Salvar em Arquivo TXT")
    print("="*80 + "\n")
    
    pdf1 = ProcessadorPDF('estudos_dirigidos_1.pdf')
    pdf2 = ProcessadorPDF('estudos_dirigidos_2.pdf')
    
    for pdf in [pdf1, pdf2]:
        if pdf.extrair_todas_paginas():
            arquivo_saida = pdf.salvar_em_arquivo('pdfs_extraidos', completo=True)
            print(f"✅ Salvo: {arquivo_saida}")
        else:
            print(f"❌ Erro ao processar {pdf.nome_arquivo}")


def exemplo_multiplos_pdfs():
    """Exemplo 5: Processar múltiplos PDFs"""
    print("\n" + "="*80)
    print("EXEMPLO 5: Processar Múltiplos PDFs")
    print("="*80 + "\n")
    
    pdfs_para_processar = [
        'estudos_dirigidos_1.pdf',
        'estudos_dirigidos_2.pdf'
    ]
    
    for nome_pdf in pdfs_para_processar:
        pdf = ProcessadorPDF(nome_pdf)
        
        if pdf.extrair_todas_paginas():
            arquivo = pdf.salvar_em_arquivo()
            linhas_char = sum(len(texto) for texto in pdf.paginas_texto.values())
            
            print(f"✅ {nome_pdf}")
            print(f"   Páginas: {pdf.metadados['total_paginas']}")
            print(f"   Caracteres: {linhas_char:,}")
            print(f"   Arquivo: {arquivo}\n")


def exemplo_buscar_texto():
    """Exemplo 6: Buscar texto em PDF"""
    print("\n" + "="*80)
    print("EXEMPLO 6: Buscar Texto em PDF")
    print("="*80 + "\n")
    
    pdf = ProcessadorPDF('estudos_dirigidos_1.pdf')
    
    if pdf.extrair_todas_paginas():
        termo_busca = "estatística"  # Trocar por termo desejado
        
        print(f"🔍 Buscando por: '{termo_busca}'...\n")
        
        encontradas = 0
        for num_pagina, texto in pdf.paginas_texto.items():
            ocorrencias = texto.lower().count(termo_busca.lower())
            if ocorrencias > 0:
                print(f"   Página {num_pagina}: {ocorrencias} ocorrência(s)")
                encontradas += ocorrencias
        
        if encontradas > 0:
            print(f"\n✅ Total: {encontradas} ocorrência(s) encontrada(s)")
        else:
            print(f"\n❌ Termo não encontrado")


if __name__ == "__main__":
    # Executar exemplos (descomente o que deseja testar)
    
    # exemplo_basico()
    # exemplo_pagina_especifica()
    # exemplo_resumo()
    exemplo_salvar()
    # exemplo_multiplos_pdfs()
    # exemplo_buscar_texto()
    
    print("\n" + "="*80)
    print("✅ Exemplos executados!")
    print("="*80)
    print("\n💡 Dica: Descomente outros exemplos no código para testá-los\n")
