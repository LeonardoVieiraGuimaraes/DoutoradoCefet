import pandas as pd
import numpy as np

print("="*80)
print("VERIFICAÇÃO DAS TABELAS LaTeX vs CSVs")
print("="*80)

# ========== FORÇA BRUTA ==========
print("\n[1] FORÇA BRUTA - Validação dos Dados")
print("-"*80)
df_fb = pd.read_csv("resultados_2/parte1/csv/resultados_forca_bruta.csv")

# Agrupar por tamanho
print("\nEstatísticas por Tamanho:")
for tamanho in sorted(df_fb['tamanho'].unique()):
    subset = df_fb[df_fb['tamanho'] == tamanho]
    cores_med = subset['num_cores'].mean()
    cores_min = subset['num_cores'].min()
    cores_max = subset['num_cores'].max()
    tempo_med = subset['tempo_execucao'].mean()
    tempo_min = subset['tempo_execucao'].min()
    tempo_max = subset['tempo_execucao'].max()
    
    print(f"Tamanho {tamanho:2d}: χ_méd={cores_med:.4f} (min={cores_min}, max={cores_max}), "
          f"tempo_méd={tempo_med:.4f}s (min={tempo_min:.4f}s, max={tempo_max:.4f}s)")

# Estatísticas gerais
print(f"\nResumo Geral Força Bruta:")
print(f"  • Total de instâncias: {len(df_fb)}")
print(f"  • Cores médias: {df_fb['num_cores'].mean():.6f}")
print(f"  • Cores mín/máx: {df_fb['num_cores'].min()}/{df_fb['num_cores'].max()}")
print(f"  • Tempo total: {df_fb['tempo_execucao'].sum():.2f}s")
print(f"  • Tempo médio: {df_fb['tempo_execucao'].mean():.6f}s")

# ========== WELSH-POWELL ==========
print("\n\n[2] WELSH-POWELL - Validação dos Dados")
print("-"*80)
df_wp = pd.read_csv("resultados_2/parte2/csv/resultados_welsh_powell.csv")

print(f"\nResultados Welsh-Powell:")
for idx, row in df_wp.iterrows():
    print(f"  {row['instancia_id']}: {row['num_vertices']:4d} vértices, "
          f"{row['cores_heuristica']:2d} cores, {row['tempo_segundos']:.6f}s")

print(f"\nResumo Geral Welsh-Powell:")
print(f"  • Total de instâncias: {len(df_wp)}")
print(f"  • Cores médias: {df_wp['cores_heuristica'].mean():.6f}")
print(f"  • Cores mín/máx: {df_wp['cores_heuristica'].min()}/{df_wp['cores_heuristica'].max()}")
print(f"  • Tempo total: {df_wp['tempo_segundos'].sum():.6f}s")
print(f"  • Tempo médio: {df_wp['tempo_segundos'].mean():.6f}s")

# ========== COMPARAÇÃO ==========
print("\n\n[3] TABELA DE COMPARAÇÃO - Valores Esperados")
print("-"*80)

comparacao_esperada = pd.DataFrame({
    'Algoritmo': ['Força Bruta', 'Welsh-Powell'],
    'Instâncias': [len(df_fb), len(df_wp)],
    'Cores Médias': [f"{df_fb['num_cores'].mean():.6f}", f"{df_wp['cores_heuristica'].mean():.6f}"],
    'Cores Mín.': [df_fb['num_cores'].min(), df_wp['cores_heuristica'].min()],
    'Cores Máx.': [df_fb['num_cores'].max(), df_wp['cores_heuristica'].max()],
    'Tempo Médio (s)': [f"{df_fb['tempo_execucao'].mean():.6f}", f"{df_wp['tempo_segundos'].mean():.6f}"],
    'Qualidade': ['Ótima (χ exato)', 'Aproximada'],
    'Complexidade': ['Exponencial', 'O(n²)']
})

print("\nValores Calculados:")
print(comparacao_esperada.to_string(index=False))

# Ler comparação salva
print("\n\nComparação Atual (no CSV):")
df_comparacao = pd.read_csv("resultados_2/comparacao_algoritmos.csv")
print(df_comparacao.to_string(index=False))

print("\n\n[4] VERIFICAÇÃO DE INTEGRIDADE")
print("-"*80)

# Verificar se força bruta tem dados para tabela LaTeX
for vértices in range(5, 21):
    dados_tamanho = df_fb[df_fb['tamanho'] == vértices]
    if len(dados_tamanho) > 0:
        cores_med = dados_tamanho['num_cores'].mean()
        cores_min = dados_tamanho['num_cores'].min()
        cores_max = dados_tamanho['num_cores'].max()
        tempo_med = dados_tamanho['tempo_execucao'].mean()
        tempo_min = dados_tamanho['tempo_execucao'].min()
        tempo_max = dados_tamanho['tempo_execucao'].max()
        
        print(f"{vértices} & {cores_med:.4f} & {tempo_med:.4f} & {tempo_min:.4f} & {tempo_max:.4f} \\\\")

print("\n" + "="*80)
print("✓ VERIFICAÇÃO CONCLUÍDA")
print("="*80)
