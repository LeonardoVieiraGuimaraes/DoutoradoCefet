"""
Script avançado para ler e processar PDFs com opções de visualização
"""

import os
import sys
import argparse
from pathlib import Path
from typing import List, Tuple

try:
    import pdfplumber
except ImportError:
    print("❌ Erro: pdfplumber não está instalado.")
    print("   Instale com: pip install pdfplumber")
    sys.exit(1)


class ProcessadorPDF:
    """Classe para processar arquivos PDF"""
    
    def __init__(self, caminho_pdf: str):
        """
        Inicializa o processador
        
        Args:
            caminho_pdf: Caminho do arquivo PDF
        """
        self.caminho_pdf = caminho_pdf
        self.nome_arquivo = os.path.basename(caminho_pdf)
        self.paginas_texto = {}
        self.metadados = {}
        
    def extrair_todas_paginas(self) -> bool:
        """Extrai texto de todas as páginas do PDF"""
        try:
            with pdfplumber.open(self.caminho_pdf) as pdf:
                self.metadados['total_paginas'] = len(pdf.pages)
                self.metadados['autor'] = pdf.metadata.get('Author', 'Desconhecido')
                self.metadados['titulo'] = pdf.metadata.get('Title', 'Sem título')
                
                for i, pagina in enumerate(pdf.pages, 1):
                    try:
                        self.paginas_texto[i] = pagina.extract_text() or ""
                    except Exception as e:
                        self.paginas_texto[i] = f"[Erro ao extrair: {str(e)}]"
                
                return True
                
        except Exception as e:
            print(f"❌ Erro ao abrir PDF: {str(e)}")
            return False
    
    def extrair_pagina_especifica(self, numero_pagina: int) -> str:
        """
        Extrai texto de uma página específica
        
        Args:
            numero_pagina: Número da página (1-indexed)
            
        Returns:
            Texto da página ou mensagem de erro
        """
        if numero_pagina in self.paginas_texto:
            return self.paginas_texto[numero_pagina]
        return "❌ Página não extraída ou não existe"
    
    def obter_resumo(self, linhas: int = 50) -> str:
        """
        Obtém um resumo das primeiras linhas de cada página
        
        Args:
            linhas: Número de linhas a extrair por página
            
        Returns:
            String com resumo formatado
        """
        resumo = []
        for num_pagina, texto in sorted(self.paginas_texto.items()):
            linhas_pagina = texto.split('\n')[:linhas]
            resumo.append(f"\n{'='*80}\nPÁGINA {num_pagina}\n{'='*80}\n")
            resumo.append('\n'.join(linhas_pagina))
            resumo.append("\n[...continua...]\n")
        
        return ''.join(resumo)
    
    def salvar_em_arquivo(self, pasta_saida: str = 'pdfs_extraidos', completo: bool = True) -> str:
        """
        Salva o texto extraído em arquivo TXT
        
        Args:
            pasta_saida: Pasta para salvar
            completo: Se True salva tudo, senão apenas resumo
            
        Returns:
            Caminho do arquivo salvo
        """
        os.makedirs(pasta_saida, exist_ok=True)
        
        nome_saida = Path(self.nome_arquivo).stem + '.txt'
        caminho_saida = os.path.join(pasta_saida, nome_saida)
        
        with open(caminho_saida, 'w', encoding='utf-8') as f:
            # Header
            f.write(f"{'='*80}\n")
            f.write(f"ARQUIVO: {self.nome_arquivo}\n")
            f.write(f"TÍTULO: {self.metadados.get('titulo', 'N/A')}\n")
            f.write(f"AUTOR: {self.metadados.get('autor', 'N/A')}\n")
            f.write(f"TOTAL DE PÁGINAS: {self.metadados.get('total_paginas', 0)}\n")
            f.write(f"TAMANHO: {os.path.getsize(self.caminho_pdf) / (1024*1024):.2f} MB\n")
            f.write(f"{'='*80}\n\n")
            
            # Conteúdo
            if completo:
                for num_pagina, texto in sorted(self.paginas_texto.items()):
                    f.write(f"\n{'='*80}\nPÁGINA {num_pagina}\n{'='*80}\n{texto}\n")
            else:
                f.write(self.obter_resumo())
        
        return caminho_saida
    
    def exibir_pagina(self, numero_pagina: int, mostrar_numero_linhas: bool = False):
        """Exibe uma página específica no console"""
        texto = self.extrair_pagina_especifica(numero_pagina)
        
        if mostrar_numero_linhas:
            linhas = texto.split('\n')
            for i, linha in enumerate(linhas, 1):
                print(f"{i:4d} | {linha}")
        else:
            print(texto)


def processar_multiplos_pdfs(pdfs: List[str], pasta_saida: str = 'pdfs_extraidos', 
                            resumo_apenas: bool = False) -> dict:
    """
    Processa múltiplos PDFs
    
    Args:
        pdfs: Lista de caminhos dos PDFs
        pasta_saida: Pasta para salvar os resultados
        resumo_apenas: Se True salva apenas resumo
        
    Returns:
        Dicionário com resultados do processamento
    """
    resultados = {}
    
    print("\n" + "="*80)
    print("📚 PROCESSADOR DE PDFs - Estudos Dirigidos")
    print("="*80 + "\n")
    
    for pdf_path in pdfs:
        if not os.path.exists(pdf_path):
            print(f"⚠️  {os.path.basename(pdf_path)} - ARQUIVO NÃO ENCONTRADO")
            continue
        
        print(f"📖 Processando: {os.path.basename(pdf_path)}...")
        
        processador = ProcessadorPDF(pdf_path)
        
        if processador.extrair_todas_paginas():
            print(f"   ✅ Extração bem-sucedida!")
            print(f"   📄 Páginas: {processador.metadados['total_paginas']}")
            
            # Salvar arquivo
            try:
                arquivo_saida = processador.salvar_em_arquivo(pasta_saida, completo=not resumo_apenas)
                print(f"   💾 Salvo em: {arquivo_saida}")
                resultados[os.path.basename(pdf_path)] = {
                    'processador': processador,
                    'sucesso': True,
                    'arquivo_saida': arquivo_saida
                }
            except Exception as e:
                print(f"   ❌ Erro ao salvar: {str(e)}")
                resultados[os.path.basename(pdf_path)] = {
                    'processador': processador,
                    'sucesso': False,
                    'erro': str(e)
                }
        else:
            print(f"   ❌ Erro ao processar")
            resultados[os.path.basename(pdf_path)] = {
                'sucesso': False,
                'erro': 'Falha na extração'
            }
        
        print()
    
    return resultados


def main():
    """Função principal com argumentos de linha de comando"""
    
    parser = argparse.ArgumentParser(
        description='Leitor e processador de PDFs dos Estudos Dirigidos'
    )
    parser.add_argument('--pasta', default='pdfs_extraidos', 
                       help='Pasta para salvar os resultados (padrão: pdfs_extraidos)')
    parser.add_argument('--resumo', action='store_true',
                       help='Salvar apenas resumo das primeiras linhas')
    parser.add_argument('--pagina', type=int,
                       help='Exibir página específica de um PDF')
    parser.add_argument('--pdf', default='',
                       help='Caminho específico de um PDF (opcional)')
    
    args = parser.parse_args()
    
    # Definir caminhos dos PDFs
    pasta_base = Path(__file__).parent
    pdfs = [
        str(pasta_base / 'estudos_dirigidos_1.pdf'),
        str(pasta_base / 'estudos_dirigidos_2.pdf')
    ]
    
    # Se um PDF específico foi informado
    if args.pdf:
        pdfs = [args.pdf]
    
    # Processar PDFs
    resultados = processar_multiplos_pdfs(pdfs, args.pasta, args.resumo)
    
    # Se foi solicitada uma página específica
    if args.pagina and resultados:
        primeiro_pdf = list(resultados.values())[0]
        if primeiro_pdf.get('sucesso') and 'processador' in primeiro_pdf:
            print("\n" + "="*80)
            print(f"PÁGINA {args.pagina}")
            print("="*80 + "\n")
            primeiro_pdf['processador'].exibir_pagina(args.pagina)
    
    # Resumo final
    print("\n" + "="*80)
    print("✅ PROCESSAMENTO CONCLUÍDO")
    print("="*80 + "\n")


if __name__ == "__main__":
    main()
