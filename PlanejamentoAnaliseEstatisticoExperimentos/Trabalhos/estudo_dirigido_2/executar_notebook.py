#!/usr/bin/env python
"""Executar o notebook e gerar CSVs"""

import subprocess
import sys

# Executar o notebook usando papermill (alternativa ao nbconvert)
try:
    import papermill as pm
    pm.execute_notebook(
        'estudos_dirigidos_2_parte1_implementacao.ipynb',
        'estudos_dirigidos_2_parte1_implementacao.ipynb'
    )
    print("\n✓ Notebook executado com sucesso!")
except ImportError:
    print("Papermill não encontrado. Tentando com nbconvert...")
    # Tentar alternativa
    exec(open('estudos_dirigidos_2_parte1_implementacao.ipynb').read())
