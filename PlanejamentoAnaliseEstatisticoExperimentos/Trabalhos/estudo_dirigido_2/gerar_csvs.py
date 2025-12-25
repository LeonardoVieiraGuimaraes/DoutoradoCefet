#!/usr/bin/env python
"""Executar um experimento simplificado para gerar CSVs rápido"""

import numpy as np
import pandas as pd
from pathlib import Path
from scipy.stats import t, skew
from scipy.stats import f_oneway
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import warnings
warnings.filterwarnings('ignore')

print("\n" + "="*80)
print("ESTUDO DIRIGIDO 2 - PARTE 1: GERAÇÃO DE RESULTADOS E CSVS")
print("="*80 + "\n")

RESULTADOS_BASE = Path("relatorio/resultados")
RESULTADOS_BASE.mkdir(parents=True, exist_ok=True)

# ===== PARTE I: TCL =====
print("Gerando Parte I: TCL...")
DISTRIBUICAO = 'Exponencial'
TRUE_MEAN = 5
RATE = 0.2
SAMPLE_SIZES = [5, 50]
NUM_SIMULATIONS = 1000  # Reduzido para ser mais rápido
RANDOM_SEED = 1
CONFIDENCE_LEVEL = 0.95
ALPHA = 1 - CONFIDENCE_LEVEL
POP_SIZE = 100_000

np.random.seed(RANDOM_SEED)
population = np.random.exponential(scale=1/RATE, size=POP_SIZE)
pop_skewness = skew(population)

resultados_assimetria = {}
meios_dict = {}
for sample_size in SAMPLE_SIZES:
    meios = [np.mean(np.random.choice(population, sample_size)) for _ in range(NUM_SIMULATIONS)]
    meios_dict[sample_size] = meios
    assimetria_meios = skew(meios)
    resultados_assimetria[sample_size] = assimetria_meios

SAMPLE_SIZE = SAMPLE_SIZES[1]
ic_contains_mean = 0

for _ in range(NUM_SIMULATIONS):
    sample = np.random.choice(population, SAMPLE_SIZE, replace=False)
    sample_mean = np.mean(sample)
    sample_std = np.std(sample, ddof=1)
    standard_error = sample_std / np.sqrt(SAMPLE_SIZE)
    degrees_freedom = SAMPLE_SIZE - 1
    ic_lower, ic_upper = t.interval(confidence=CONFIDENCE_LEVEL, df=degrees_freedom, loc=sample_mean, scale=standard_error)
    if (ic_lower <= TRUE_MEAN) and (TRUE_MEAN <= ic_upper):
        ic_contains_mean += 1

proportion_success = ic_contains_mean / NUM_SIMULATIONS

RESULTADOS_DIR_TCL = RESULTADOS_BASE / "parte_1_tcl"
RESULTADOS_DIR_TCL.mkdir(parents=True, exist_ok=True)

# Salvar parâmetros
parametros_tcl = pd.DataFrame({
    'Métrica': ['Distribuição', 'Média (μ)', 'Taxa (λ)', 'Pop Size', 'Tamanhos Amostrais', 'Simulações', 'Confiança (%)', 'α', 'Seed'],
    'Valor': [DISTRIBUICAO, TRUE_MEAN, RATE, POP_SIZE, str(SAMPLE_SIZES), NUM_SIMULATIONS, CONFIDENCE_LEVEL*100, ALPHA, RANDOM_SEED]
})
parametros_tcl.to_csv(RESULTADOS_DIR_TCL / "parametros_tcl.csv", index=False, encoding='utf-8')

# Salvar resultados
resultados_tcl = pd.DataFrame({
    'Métrica': ['Assimetria População', 'Assimetria Médias n=5', 'Assimetria Médias n=50', 'Taxa Cobertura Obs', 'Taxa Cobertura Esp', 'Diferença'],
    'Valor': [round(pop_skewness, 4), round(resultados_assimetria[5], 4), round(resultados_assimetria[50], 4), round(proportion_success, 4), round(CONFIDENCE_LEVEL, 4), round(abs(proportion_success - CONFIDENCE_LEVEL), 4)]
})
resultados_tcl.to_csv(RESULTADOS_DIR_TCL / "analise_tcl_resultados.csv", index=False, encoding='utf-8')
print(f"✓ TCL: Parâmetros e resultados salvos\n")

# ===== PARTE II, EX 1: ONE-WAY =====
print("Gerando Parte II, Ex. 1: One-Way ANOVA...")
RANDOM_SEED_ONEWAY = 123
N_REP = 10
MEDIA_A, MEDIA_B, MEDIA_C = 20, 21, 28
STD_DEV = 1.5
ALPHA_TUKEY = 0.05

np.random.seed(RANDOM_SEED_ONEWAY)
dados_list = []
for nome, media in zip(['A', 'B', 'C'], [MEDIA_A, MEDIA_B, MEDIA_C]):
    for rep in range(N_REP):
        dados_list.append({'Revestimento': nome, 'Tempo_Secagem': np.random.normal(media, STD_DEV), 'Repetição': rep + 1})

df_oneway = pd.DataFrame(dados_list)
stats_oneway = df_oneway.groupby('Revestimento')['Tempo_Secagem'].agg([('n', 'count'), ('Média', 'mean'), ('DP', 'std'), ('Mín', 'min'), ('Máx', 'max')])

model_oneway = ols('Tempo_Secagem ~ C(Revestimento)', data=df_oneway).fit()
anova_oneway = anova_lm(model_oneway, typ=2)

RESULTADOS_DIR_ONEWAY = RESULTADOS_BASE / "parte_2_oneway"
RESULTADOS_DIR_ONEWAY.mkdir(parents=True, exist_ok=True)

parametros_oneway = pd.DataFrame({
    'Métrica': ['Seed', 'Repetições', 'Alpha', 'Média A', 'Média B', 'Média C', 'DP'],
    'Valor': [RANDOM_SEED_ONEWAY, N_REP, ALPHA_TUKEY, MEDIA_A, MEDIA_B, MEDIA_C, STD_DEV]
})
parametros_oneway.to_csv(RESULTADOS_DIR_ONEWAY / "parametros_oneway.csv", index=False, encoding='utf-8')

resultados_oneway = pd.DataFrame({
    'Métrica': ['A Média', 'A DP', 'A n', 'B Média', 'B DP', 'B n', 'C Média', 'C DP', 'C n', 'F-Stat', 'P-Value', 'R2', 'Resíduos'],
    'Valor': [
        round(stats_oneway.loc['A', 'Média'], 4), round(stats_oneway.loc['A', 'DP'], 4), int(stats_oneway.loc['A', 'n']),
        round(stats_oneway.loc['B', 'Média'], 4), round(stats_oneway.loc['B', 'DP'], 4), int(stats_oneway.loc['B', 'n']),
        round(stats_oneway.loc['C', 'Média'], 4), round(stats_oneway.loc['C', 'DP'], 4), int(stats_oneway.loc['C', 'n']),
        round(anova_oneway.loc['C(Revestimento)', 'F'], 4),
        round(anova_oneway.loc['C(Revestimento)', 'PR(>F)'], 6),
        round(model_oneway.rsquared, 4),
        round(np.sqrt(model_oneway.mse_resid), 4)
    ]
})
resultados_oneway.to_csv(RESULTADOS_DIR_ONEWAY / "analise_oneway_resultados.csv", index=False, encoding='utf-8')
print(f"✓ One-Way: Parâmetros e resultados salvos\n")

# ===== PARTE II, EX 2: RCBD =====
print("Gerando Parte II, Ex. 2: RCBD...")
RANDOM_SEED_RCBD = 456
NOMES_BLOCOS = ['G1', 'G2', 'G3']
NOMES_TRATAMENTOS = ['T1', 'T2', 'T3', 'T4']
BASE_GANHO = 50
EFEITOS_BLOCO = [0, 5, 10]
EFEITOS_TRATAMENTO = [0, 2, 5, 15]
STD_RCBD = 2
ALPHA_TUKEY_RCBD = 0.05

np.random.seed(RANDOM_SEED_RCBD)
dados_rcbd = []
for bloco_idx, bloco in enumerate(NOMES_BLOCOS):
    for trat_idx, tratamento in enumerate(NOMES_TRATAMENTOS):
        ganho = BASE_GANHO + EFEITOS_BLOCO[bloco_idx] + EFEITOS_TRATAMENTO[trat_idx] + np.random.normal(0, STD_RCBD)
        dados_rcbd.append({'Bloco': bloco, 'Tratamento': tratamento, 'Ganho': ganho})

df_rcbd = pd.DataFrame(dados_rcbd)
stats_trat_rcbd = df_rcbd.groupby('Tratamento')['Ganho'].agg([('n', 'count'), ('Média', 'mean'), ('DP', 'std'), ('Mín', 'min'), ('Máx', 'max')])

model_rcbd = ols('Ganho ~ C(Tratamento) + C(Bloco)', data=df_rcbd).fit()
anova_rcbd = anova_lm(model_rcbd, typ=2)

RESULTADOS_DIR_RCBD = RESULTADOS_BASE / "parte_2_rcbd"
RESULTADOS_DIR_RCBD.mkdir(parents=True, exist_ok=True)

parametros_rcbd = pd.DataFrame({
    'Métrica': ['Seed', 'Blocos', 'Tratamentos', 'Base Ganho', 'DP', 'Alpha', 'Efeitos Bloco', 'Efeitos Tratamento'],
    'Valor': [RANDOM_SEED_RCBD, len(NOMES_BLOCOS), len(NOMES_TRATAMENTOS), BASE_GANHO, STD_RCBD, ALPHA_TUKEY_RCBD, str(EFEITOS_BLOCO), str(EFEITOS_TRATAMENTO)]
})
parametros_rcbd.to_csv(RESULTADOS_DIR_RCBD / "parametros_rcbd.csv", index=False, encoding='utf-8')

resultados_rcbd = pd.DataFrame({
    'Métrica': ['T1 Média', 'T1 DP', 'T1 n', 'T2 Média', 'T2 DP', 'T2 n', 'T3 Média', 'T3 DP', 'T3 n', 'T4 Média', 'T4 DP', 'T4 n', 'F-Trat', 'P-Trat', 'F-Bloco', 'P-Bloco', 'R2', 'Resíduos'],
    'Valor': [
        round(stats_trat_rcbd.loc['T1', 'Média'], 4), round(stats_trat_rcbd.loc['T1', 'DP'], 4), int(stats_trat_rcbd.loc['T1', 'n']),
        round(stats_trat_rcbd.loc['T2', 'Média'], 4), round(stats_trat_rcbd.loc['T2', 'DP'], 4), int(stats_trat_rcbd.loc['T2', 'n']),
        round(stats_trat_rcbd.loc['T3', 'Média'], 4), round(stats_trat_rcbd.loc['T3', 'DP'], 4), int(stats_trat_rcbd.loc['T3', 'n']),
        round(stats_trat_rcbd.loc['T4', 'Média'], 4), round(stats_trat_rcbd.loc['T4', 'DP'], 4), int(stats_trat_rcbd.loc['T4', 'n']),
        round(anova_rcbd.loc['C(Tratamento)', 'F'], 4), round(anova_rcbd.loc['C(Tratamento)', 'PR(>F)'], 6),
        round(anova_rcbd.loc['C(Bloco)', 'F'], 4), round(anova_rcbd.loc['C(Bloco)', 'PR(>F)'], 6),
        round(model_rcbd.rsquared, 4), round(np.sqrt(model_rcbd.mse_resid), 4)
    ]
})
resultados_rcbd.to_csv(RESULTADOS_DIR_RCBD / "analise_rcbd_resultados.csv", index=False, encoding='utf-8')
print(f"✓ RCBD: Parâmetros e resultados salvos\n")

# ===== PARTE II, EX 3: FATORIAL =====
print("Gerando Parte II, Ex. 3: ANOVA Fatorial...")
RANDOM_SEED_FATORIAL = 789
NIVEIS_TEMPERATURA = [70, 85]
NIVEIS_PRESSAO = [50, 60, 70]
N_REP_FATORIAL = 5
MEDIAS_FATORIAL = {(70, 50): 50, (70, 60): 55, (70, 70): 60, (85, 50): 48, (85, 60): 45, (85, 70): 42}
STD_FATORIAL = 2
ALPHA_TUKEY_FATORIAL = 0.05

np.random.seed(RANDOM_SEED_FATORIAL)
dados_fatorial = []
for temp in NIVEIS_TEMPERATURA:
    for pressao in NIVEIS_PRESSAO:
        media = MEDIAS_FATORIAL[(temp, pressao)]
        for rep in range(N_REP_FATORIAL):
            valor = np.random.normal(media, STD_FATORIAL)
            dados_fatorial.append({'Temperatura': temp, 'Pressao': pressao, 'Temp_Pressao': f"{temp}C-{pressao}psi", 'Rendimento': valor, 'Repetição': rep + 1})

df_fatorial = pd.DataFrame(dados_fatorial)
stats_fatorial = df_fatorial.groupby('Temp_Pressao')['Rendimento'].agg([('n', 'count'), ('Média', 'mean'), ('DP', 'std'), ('Mín', 'min'), ('Máx', 'max')])

model_fatorial = ols('Rendimento ~ C(Temperatura) * C(Pressao)', data=df_fatorial).fit()
anova_fatorial = anova_lm(model_fatorial, typ=2)

RESULTADOS_DIR_FATORIAL = RESULTADOS_BASE / "parte_2_fatorial"
RESULTADOS_DIR_FATORIAL.mkdir(parents=True, exist_ok=True)

parametros_fatorial = pd.DataFrame({
    'Métrica': ['Seed', 'Temperaturas', 'Pressões', 'Repetições', 'DP', 'Alpha', 'Médias'],
    'Valor': [RANDOM_SEED_FATORIAL, str(NIVEIS_TEMPERATURA), str(NIVEIS_PRESSAO), N_REP_FATORIAL, STD_FATORIAL, ALPHA_TUKEY_FATORIAL, str(MEDIAS_FATORIAL)]
})
parametros_fatorial.to_csv(RESULTADOS_DIR_FATORIAL / "parametros_fatorial.csv", index=False, encoding='utf-8')

cols = ['Níveis Temp', 'Níveis Press', 'Total Obs', 'Repetições', 'DP']
vals = [len(NIVEIS_TEMPERATURA), len(NIVEIS_PRESSAO), len(df_fatorial), N_REP_FATORIAL, STD_FATORIAL]

for combo in stats_fatorial.index:
    cols.append(f"{combo} Média")
    vals.append(round(stats_fatorial.loc[combo, 'Média'], 4))

for combo in stats_fatorial.index:
    cols.append(f"{combo} DP")
    vals.append(round(stats_fatorial.loc[combo, 'DP'], 4))

for combo in stats_fatorial.index:
    cols.append(f"{combo} n")
    vals.append(int(stats_fatorial.loc[combo, 'n']))

cols.extend(['F-Temp', 'P-Temp', 'F-Press', 'P-Press', 'F-Inter', 'P-Inter', 'R2', 'Resíduos'])
vals.extend([
    round(anova_fatorial.loc['C(Temperatura)', 'F'], 4),
    round(anova_fatorial.loc['C(Temperatura)', 'PR(>F)'], 6),
    round(anova_fatorial.loc['C(Pressao)', 'F'], 4),
    round(anova_fatorial.loc['C(Pressao)', 'PR(>F)'], 6),
    round(anova_fatorial.loc['C(Temperatura):C(Pressao)', 'F'], 4),
    round(anova_fatorial.loc['C(Temperatura):C(Pressao)', 'PR(>F)'], 6),
    round(model_fatorial.rsquared, 4),
    round(np.sqrt(model_fatorial.mse_resid), 4)
])

resultados_fatorial = pd.DataFrame({'Métrica': cols, 'Valor': vals})
resultados_fatorial.to_csv(RESULTADOS_DIR_FATORIAL / "analise_fatorial_resultados.csv", index=False, encoding='utf-8')
print(f"✓ Fatorial: Parâmetros e resultados salvos\n")

# ===== RESUMO =====
print("\n" + "="*80)
print("✓ TODOS OS RESULTADOS SALVOS COM SUCESSO!")
print("="*80)

# Listar CSVs
csvs = list(RESULTADOS_BASE.rglob("*.csv"))
print(f"\n✓ {len(csvs)} arquivos CSV gerados:")
for csv in sorted(csvs):
    size = csv.stat().st_size
    print(f"  - {csv.relative_to(RESULTADOS_BASE)} ({size} bytes)")

print("\n" + "="*80 + "\n")
