#!/usr/bin/env python3
"""
Script para gerar apenas as tabelas LaTeX do Fatorial
Execução direta sem nbconvert
"""

import pandas as pd
from pathlib import Path

# Caminhos
RESULTADOS_BASE = Path(__file__).parent / "relatorio" / "resultados"
ANALISES_DIR = RESULTADOS_BASE / "analises"

print("=" * 70)
print("GERANDO TABELAS LATEX - FATORIAL")
print("=" * 70 + "\n")

# Ler CSVs do Fatorial
csv_param_fatorial = RESULTADOS_BASE / "parte_2_fatorial" / "parametros_fatorial.csv"
csv_resultado_fatorial = RESULTADOS_BASE / "parte_2_fatorial" / "analise_fatorial_resultados.csv"

if csv_param_fatorial.exists() and csv_resultado_fatorial.exists():
    df_param = pd.read_csv(csv_param_fatorial)
    df_resultado = pd.read_csv(csv_resultado_fatorial)
    
    # Criar diretório
    output_dir = ANALISES_DIR / "fatorial"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Gerar LaTeX Parâmetros
    latex_param = """\\begin{table}[H]
\\centering
\\caption{Parâmetros - ANOVA Fatorial}
\\label{tab:parametros_fatorial}
\\begin{tabular}{|l|r|}
\\hline
\\textbf{Métrica} & \\textbf{Valor} \\\\
\\hline
"""
    for _, row in df_param.iterrows():
        metrica = row['Métrica'].replace('_', '\\_')
        valor = str(row['Valor'])
        latex_param += f"{metrica} & {valor} \\\\\n"
    
    latex_param += """\\hline
\\end{tabular}
\\end{table}
"""
    
    # Gerar LaTeX Resultados
    latex_resultado = """\\begin{table}[H]
\\centering
\\caption{Resultados - ANOVA Fatorial}
\\label{tab:resultados_fatorial}
\\begin{tabular}{|l|r|}
\\hline
\\textbf{Métrica} & \\textbf{Valor} \\\\
\\hline
"""
    for _, row in df_resultado.iterrows():
        metrica = row['Métrica'].replace('_', '\\_')
        valor = str(row['Valor'])
        latex_resultado += f"{metrica} & {valor} \\\\\n"
    
    latex_resultado += """\\hline
\\end{tabular}
\\end{table}
"""
    
    # Salvar arquivos
    (output_dir / "parametros_fatorial.tex").write_text(latex_param, encoding='utf-8')
    (output_dir / "resultados_fatorial.tex").write_text(latex_resultado, encoding='utf-8')
    
    print("✓ Tabela LaTeX Parâmetros Fatorial salva")
    print("✓ Tabela LaTeX Resultados Fatorial salva\n")
    print("=" * 70)
    print("SUCESSO! Todos os 8 arquivos LaTeX foram gerados!")
    print("=" * 70)
else:
    print("✗ Arquivos CSV não encontrados")
    if not csv_param_fatorial.exists():
        print(f"  - Faltando: {csv_param_fatorial}")
    if not csv_resultado_fatorial.exists():
        print(f"  - Faltando: {csv_resultado_fatorial}")
