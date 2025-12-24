#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import io

# Redirecionar stdout para UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

pdf_path = r'd:\GitHub\DoutoradoCefet\PlanejamentoAnaliseEstatisticoExperimentos\Trabalhos\estudo_dirigido_2\estudos_dirigidos_2.pdf'

try:
    import pdfplumber
    with pdfplumber.open(pdf_path) as pdf:
        print(f'Total de páginas: {len(pdf.pages)}\n')
        for i, page in enumerate(pdf.pages):
            print(f'===== PÁGINA {i+1} =====')
            text = page.extract_text()
            print(text if text else 'Sem texto')
            print('\n')
except Exception as e:
    print(f'Erro com pdfplumber: {e}')
    try:
        from PyPDF2 import PdfReader
        reader = PdfReader(pdf_path)
        print(f'Total de páginas: {len(reader.pages)}\n')
        for i, page in enumerate(reader.pages):
            print(f'===== PÁGINA {i+1} =====')
            text = page.extract_text()
            print(text if text else 'Sem texto')
            print('\n')
    except Exception as e2:
        print(f'Erro com PyPDF2: {e2}')
        print('Nenhuma biblioteca PDF disponível')
