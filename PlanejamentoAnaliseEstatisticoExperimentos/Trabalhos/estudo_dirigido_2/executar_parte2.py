#!/usr/bin/env python3
"""
Script para executar as células do notebook parte 2 e gerar LaTeX
"""

import subprocess
import sys
from pathlib import Path

notebook_path = Path(__file__).parent / "estudos_dirigidos_2_parte2_latex.ipynb"

print("=" * 70)
print("EXECUTANDO NOTEBOOK PARTE 2: Geração de Tabelas LaTeX")
print("=" * 70)

# Usar jupyter nbconvert com execute preprocessor
cmd = [
    sys.executable, "-m", "nbconvert",
    "--to", "notebook",
    "--execute",
    "--inplace",
    "--ExecutePreprocessor.timeout=600",
    str(notebook_path)
]

print(f"\nComando: {' '.join(cmd)}\n")

try:
    result = subprocess.run(cmd, capture_output=False, text=True)
    
    if result.returncode == 0:
        print("\n" + "=" * 70)
        print("✓ Notebook executado com sucesso!")
        print("=" * 70)
        print("\nArquivos LaTeX gerados:")
        print("  TCL:")
        print("    - relatorio/resultados/analises/tcl/parametros_tcl.tex")
        print("    - relatorio/resultados/analises/tcl/resultados_tcl.tex")
        print("  One-Way:")
        print("    - relatorio/resultados/analises/oneway/parametros_oneway.tex")
        print("    - relatorio/resultados/analises/oneway/resultados_oneway.tex")
        print("  RCBD:")
        print("    - relatorio/resultados/analises/rcbd/parametros_rcbd.tex")
        print("    - relatorio/resultados/analises/rcbd/resultados_rcbd.tex")
        print("  Fatorial:")
        print("    - relatorio/resultados/analises/fatorial/parametros_fatorial.tex")
        print("    - relatorio/resultados/analises/fatorial/resultados_fatorial.tex")
    else:
        print(f"\n✗ Erro ao executar notebook (código {result.returncode})")
        sys.exit(1)

except Exception as e:
    print(f"Erro: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
