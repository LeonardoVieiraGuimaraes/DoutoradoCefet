"""
Script para ler e extrair conteúdo dos PDFs dos Estudos Dirigidos 1 e 2
"""

import os
import sys
from pathlib import Path

try:
    import pdfplumber
except ImportError:
    print("❌ Erro: pdfplumber não está instalado.")
    print("   Instale com: pip install pdfplumber")
    sys.exit(1)


def extrair_texto_pdf(caminho_pdf):
    """
    Extrai texto de um arquivo PDF
    
    Args:
        caminho_pdf (str): Caminho para o arquivo PDF
        
    Returns:
        dict: Dicionário com informações sobre o PDF e seu texto
    """
    try:
        resultado = {
            'arquivo': os.path.basename(caminho_pdf),
            'caminho': caminho_pdf,
            'existe': os.path.exists(caminho_pdf),
            'tamanho_mb': os.path.getsize(caminho_pdf) / (1024*1024) if os.path.exists(caminho_pdf) else 0,
            'paginas': 0,
            'texto': '',
            'erro': None
        }
        
        if not resultado['existe']:
            resultado['erro'] = f"Arquivo não encontrado: {caminho_pdf}"
            return resultado
        
        with pdfplumber.open(caminho_pdf) as pdf:
            resultado['paginas'] = len(pdf.pages)
            
            # Extrair texto de todas as páginas
            textos = []
            for i, pagina in enumerate(pdf.pages, 1):
                try:
                    texto_pagina = pagina.extract_text()
                    if texto_pagina:
                        textos.append(f"\n{'='*80}\nPÁGINA {i}\n{'='*80}\n{texto_pagina}")
                except Exception as e:
                    textos.append(f"\n[Erro ao extrair página {i}: {str(e)}]")
            
            resultado['texto'] = "\n".join(textos)
            
    except Exception as e:
        resultado['erro'] = str(e)
    
    return resultado


def salvar_texto_extraido(resultado, pasta_saida='pdfs_extraidos'):
    """
    Salva o texto extraído em um arquivo TXT
    
    Args:
        resultado (dict): Dicionário com informações do PDF
        pasta_saida (str): Pasta para salvar os arquivos extraídos
    """
    # Criar pasta de saída se não existir
    os.makedirs(pasta_saida, exist_ok=True)
    
    # Nome do arquivo de saída
    nome_arquivo = Path(resultado['arquivo']).stem + '.txt'
    caminho_saida = os.path.join(pasta_saida, nome_arquivo)
    
    # Salvar texto
    with open(caminho_saida, 'w', encoding='utf-8') as f:
        f.write(f"ARQUIVO ORIGINAL: {resultado['arquivo']}\n")
        f.write(f"TAMANHO: {resultado['tamanho_mb']:.2f} MB\n")
        f.write(f"TOTAL DE PÁGINAS: {resultado['paginas']}\n")
        f.write(f"{'='*80}\n\n")
        f.write(resultado['texto'])
    
    return caminho_saida


def main():
    """Função principal"""
    
    # Definir caminhos dos PDFs
    pasta_base = Path(__file__).parent
    pdfs = [
        pasta_base / 'estudos_dirigidos_1.pdf',
        pasta_base / 'estudos_dirigidos_2.pdf'
    ]
    
    print("\n" + "="*80)
    print("📄 LEITOR DE PDFs - Estudos Dirigidos")
    print("="*80 + "\n")
    
    resultados = []
    
    # Processar cada PDF
    for pdf_path in pdfs:
        print(f"📖 Processando: {pdf_path.name}...")
        
        resultado = extrair_texto_pdf(str(pdf_path))
        resultados.append(resultado)
        
        # Exibir informações
        if resultado['erro']:
            print(f"   ❌ ERRO: {resultado['erro']}\n")
        else:
            print(f"   ✅ Sucesso!")
            print(f"   📊 Tamanho: {resultado['tamanho_mb']:.2f} MB")
            print(f"   📄 Páginas: {resultado['paginas']}")
            print(f"   📝 Caracteres extraídos: {len(resultado['texto'])}\n")
    
    # Salvar resultados
    print("💾 Salvando textos extraídos...")
    for resultado in resultados:
        if not resultado['erro']:
            try:
                caminho_saida = salvar_texto_extraido(resultado)
                print(f"   ✅ {resultado['arquivo']} → {caminho_saida}")
            except Exception as e:
                print(f"   ❌ Erro ao salvar {resultado['arquivo']}: {str(e)}")
    
    # Resumo final
    print("\n" + "="*80)
    print("📊 RESUMO")
    print("="*80)
    
    total_paginas = sum(r['paginas'] for r in resultados if not r['erro'])
    total_caracteres = sum(len(r['texto']) for r in resultados if not r['erro'])
    total_tamanho = sum(r['tamanho_mb'] for r in resultados if not r['erro'])
    
    print(f"PDFs processados: {len([r for r in resultados if not r['erro']])}")
    print(f"Total de páginas: {total_paginas}")
    print(f"Total de caracteres extraídos: {total_caracteres:,}")
    print(f"Tamanho total dos PDFs: {total_tamanho:.2f} MB")
    print(f"Pasta de saída: {os.path.abspath('pdfs_extraidos')}")
    print("="*80 + "\n")


if __name__ == "__main__":
    main()
