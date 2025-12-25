#!/usr/bin/env python3
"""
Script para executar as células do notebook parte 1 e gerar CSVs
"""

import json
import subprocess
import sys
from pathlib import Path

notebook_path = Path(__file__).parent / "estudos_dirigidos_2_parte1_implementacao.ipynb"

print("=" * 70)
print("EXECUTANDO NOTEBOOK PARTE 1: Implementação dos Experimentos")
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
        print("\nArquivos gerados:")
        print("  - Parâmetros TCL: relatorio/resultados/parte_1_tcl/parametros_tcl.csv")
        print("  - Resultados TCL: relatorio/resultados/parte_1_tcl/analise_tcl_resultados.csv")
        print("  - Parâmetros One-Way: relatorio/resultados/parte_2_oneway/parametros_oneway.csv")
        print("  - Resultados One-Way: relatorio/resultados/parte_2_oneway/analise_oneway_resultados.csv")
        print("  - Parâmetros RCBD: relatorio/resultados/parte_2_rcbd/parametros_rcbd.csv")
        print("  - Resultados RCBD: relatorio/resultados/parte_2_rcbd/analise_rcbd_resultados.csv")
        print("  - Parâmetros Fatorial: relatorio/resultados/parte_2_fatorial/parametros_fatorial.csv")
        print("  - Resultados Fatorial: relatorio/resultados/parte_2_fatorial/analise_fatorial_resultados.csv")
        print("\nGráficos gerados (PNG):")
        print("  - Histogramas TCL (3 gráficos)")
        print("  - Boxplot One-Way")
        print("  - Boxplot RCBD")
        print("  - Interaction plot + Boxplot Fatorial")
    else:
        print(f"\n✗ Erro ao executar notebook (código {result.returncode})")
        sys.exit(1)

except Exception as e:
    print(f"Erro: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
