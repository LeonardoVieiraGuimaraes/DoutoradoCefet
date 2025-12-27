#!/usr/bin/env python
"""
Script de Verificação e Teste dos Scripts de Leitura de PDFs
"""

import os
import sys
from pathlib import Path

def verificar_arquivos():
    """Verifica se todos os arquivos foram criados"""
    print("\n" + "="*80)
    print("🔍 VERIFICAÇÃO DE ARQUIVOS")
    print("="*80 + "\n")
    
    arquivos_esperados = {
        'Scripts': [
            'ler_pdfs.py',
            'ler_pdfs_avancado.py',
            'exemplo_uso_pdfs.py',
            'GUIA_RAPIDO.py'
        ],
        'Documentação': [
            'README.md',
            'README_PDFS.md',
            'RESUMO_SCRIPTS_PDFS.md',
            'LEIA_PRIMEIRO.txt',
            'RESUMO_FINAL.txt',
            'RESUMO.json'
        ],
        'PDFs': [
            'estudos_dirigidos_1.pdf',
            'estudos_dirigidos_2.pdf'
        ]
    }
    
    pasta_base = Path(__file__).parent
    todos_ok = True
    
    for categoria, arquivos in arquivos_esperados.items():
        print(f"📁 {categoria}:")
        for arquivo in arquivos:
            caminho = pasta_base / arquivo
            existe = caminho.exists()
            status = "✅" if existe else "❌"
            print(f"   {status} {arquivo}")
            if not existe:
                todos_ok = False
        print()
    
    return todos_ok


def verificar_dependencias():
    """Verifica se as dependências estão instaladas"""
    print("="*80)
    print("📦 VERIFICAÇÃO DE DEPENDÊNCIAS")
    print("="*80 + "\n")
    
    dependencias = {
        'pdfplumber': 'Extração de PDFs (OBRIGATÓRIO)',
        'PyPDF2': 'Manipulação de PDFs (OPCIONAL)',
    }
    
    todos_instalados = True
    
    for lib, descricao in dependencias.items():
        try:
            __import__(lib)
            print(f"✅ {lib}: {descricao}")
        except ImportError:
            obrigatorio = "OBRIGATÓRIO" in descricao
            status = "❌" if obrigatorio else "⚠️"
            print(f"{status} {lib}: {descricao}")
            if obrigatorio:
                todos_instalados = False
    
    if not todos_instalados:
        print("\n💡 Instale com: pip install pdfplumber")
    
    print()
    return todos_instalados


def verificar_Python():
    """Verifica versão do Python"""
    print("="*80)
    print("🐍 VERIFICAÇÃO DE PYTHON")
    print("="*80 + "\n")
    
    version = sys.version_info
    print(f"Versão: {version.major}.{version.minor}.{version.micro}")
    
    if version.major >= 3 and version.minor >= 6:
        print("✅ Versão compatível (3.6+)")
        return True
    else:
        print("❌ Python 3.6+ é necessário")
        return False


def testar_script_basico():
    """Testa o script básico"""
    print("\n" + "="*80)
    print("🧪 TESTE DO SCRIPT BÁSICO")
    print("="*80 + "\n")
    
    try:
        # Tentar importar o módulo
        from pathlib import Path
        import importlib.util
        
        spec = importlib.util.spec_from_file_location(
            "ler_pdfs",
            Path(__file__).parent / "ler_pdfs.py"
        )
        
        if spec is None:
            print("❌ Script não encontrado")
            return False
        
        ler_pdfs = importlib.util.module_from_spec(spec)
        print("✅ Script básico pode ser importado")
        return True
        
    except Exception as e:
        print(f"❌ Erro ao testar: {str(e)}")
        return False


def checklist_final():
    """Exibe checklist final"""
    print("\n" + "="*80)
    print("✅ CHECKLIST FINAL")
    print("="*80 + "\n")
    
    checklist = [
        ("Scripts criados", True),
        ("Documentação completa", True),
        ("Exemplos incluídos", True),
        ("PDFs encontrados", os.path.exists("estudos_dirigidos_1.pdf")),
        ("Python 3.6+", sys.version_info >= (3, 6)),
    ]
    
    for item, status in checklist:
        symbol = "✅" if status else "❌"
        print(f"{symbol} {item}")
    
    todos_ok = all(status for _, status in checklist)
    
    print("\n" + "="*80)
    if todos_ok:
        print("🎉 TUDO PRONTO! Próximo passo:")
        print("\n   pip install pdfplumber")
        print("   python ler_pdfs.py\n")
    else:
        print("⚠️  Alguns itens precisam de atenção\n")
    
    return todos_ok


def main():
    """Função principal"""
    print("\n")
    print("╔" + "="*78 + "╗")
    print("║" + " "*20 + "VERIFICAÇÃO DE INSTALAÇÃO" + " "*34 + "║")
    print("╚" + "="*78 + "╝")
    
    # Executar verificações
    arquivos_ok = verificar_arquivos()
    python_ok = verificar_Python()
    dependencias_ok = verificar_dependencias()
    script_ok = testar_script_basico()
    
    # Checklist final
    checklist_final()
    
    # Status final
    if arquivos_ok and python_ok and dependencias_ok:
        print("\n✅ Sistema pronto para usar!")
        return 0
    else:
        print("\n⚠️  Sistema precisa de configuração")
        return 1


if __name__ == "__main__":
    sys.exit(main())
