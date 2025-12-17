import os

RESULTADOS = r'relatorio\resultados'

print('='*80)
print('RESUMO FINAL DE ARQUIVOS GERADOS')
print('='*80)

# Contar e listar por seção
sections = {
    'Parte I - TCL': 'parte_1_tcl',
    'Parte II - One-Way ANOVA': 'parte_2_oneway',
    'Parte II - RCBD': 'parte_2_rcbd',
    'Parte II - Fatorial': 'parte_2_fatorial',
    'Parte III - Análises TEX': 'analises'
}

total_files = 0
for section_name, section_dir in sections.items():
    section_path = os.path.join(RESULTADOS, section_dir)
    if os.path.exists(section_path):
        files = []
        for root, dirs, filenames in os.walk(section_path):
            files.extend(filenames)
        
        print(f'\n▶ {section_name}')
        print(f'  Diretório: {section_dir}/')
        print(f'  Arquivos: {len(files)}')
        
        for file in sorted(files):
            print(f'    ✓ {file}')
        total_files += len(files)

print('\n' + '='*80)
print(f'TOTAL DE ARQUIVOS GERADOS: {total_files}')
print('='*80)
