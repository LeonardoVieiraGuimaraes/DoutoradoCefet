#!/usr/bin/env python
"""Extrair e executar código do notebook diretamente"""

import json
import sys
from pathlib import Path

# Carregar o notebook
notebook_path = Path("estudos_dirigidos_2_parte1_implementacao.ipynb")
with open(notebook_path, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

# Extrair e executar células de código
code_cells = [cell for cell in notebook['cells'] if cell['cell_type'] == 'code']

print(f"\n{'='*80}")
print(f"EXECUTANDO {len(code_cells)} CÉLULAS DE CÓDIGO")
print(f"{'='*80}\n")

for i, cell in enumerate(code_cells, 1):
    code = ''.join(cell['source'])
    if code.strip():
        print(f"\n[{i}/{len(code_cells)}] Executando célula...")
        try:
            exec(code)
        except Exception as e:
            print(f"✗ Erro na célula {i}: {type(e).__name__}: {e}")
            import traceback
            traceback.print_exc()

print(f"\n{'='*80}")
print("✓ EXECUÇÃO CONCLUÍDA!")
print(f"{'='*80}\n")

# Verificar CSVs gerados
import os
resultados_base = Path("relatorio/resultados")
if resultados_base.exists():
    csvs = list(resultados_base.rglob("*.csv"))
    print(f"\n✓ {len(csvs)} arquivos CSV gerados:")
    for csv in sorted(csvs):
        print(f"  - {csv}")
