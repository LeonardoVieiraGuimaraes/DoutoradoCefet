import pandas as pd

df = pd.read_csv('resultados/parte1/csv/resultados_forca_bruta.csv')

print("Verificando tempos mencionados no relatório:")
print("=" * 60)

for tamanho in [5, 10, 13]:
    dados = df[df['tamanho'] == tamanho]
    if not dados.empty:
        tempo_medio = dados['tempo_segundos'].mean()
        print(f"\nn={tamanho}:")
        print(f"  Tempo médio: {tempo_medio:.10f} segundos")
        print(f"  Em ms: {tempo_medio*1000:.4f} ms")
        print(f"  Notação científica: {tempo_medio:.2e} segundos")
        print(f"  Total de amostras: {len(dados)}")
        
print("\n" + "=" * 60)
print("Texto relata:")
print("  n=5: tempo médio ≈ 4×10⁻⁵ segundos (desprezível)")
print("  n=10: tempo médio ≈ 0.05 segundos")
print("  n=13: tempo médio ≈ 5 segundos")
