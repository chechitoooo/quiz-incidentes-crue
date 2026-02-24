# ============================================================
# descriptivo.py
# Calcula estadísticas descriptivas de incidentes diarios
# ============================================================

import pandas as pd
import numpy as np

# ------------------------------------------------------------
# 1. Cargar archivo
# ------------------------------------------------------------

# Lee el archivo (separado por espacios)
df = pd.read_csv("incidentes_crue_diarios.txt", sep=r"\s+")

# Convertir fecha a formato datetime
df["fecha"] = pd.to_datetime(df["fecha"])

# Extraer solo los valores de incidentes
incidentes = df["incidentes"]

# ------------------------------------------------------------
# 2. MEDIDAS DE TENDENCIA CENTRAL
# ------------------------------------------------------------

media = incidentes.mean()
mediana = incidentes.median()
moda = incidentes.mode()[0]

# ------------------------------------------------------------
# 3. MEDIDAS DE DISPERSIÓN
# ------------------------------------------------------------

desv_std = incidentes.std()
varianza = incidentes.var()
coef_variacion = desv_std / media
rango = incidentes.max() - incidentes.min()
max = incidentes.max()
min = incidentes.min()

# ------------------------------------------------------------
# 4. CUARTILES Y PERCENTILES
# ------------------------------------------------------------

Q1 = incidentes.quantile(0.25)
Q2 = incidentes.quantile(0.50)
Q3 = incidentes.quantile(0.75)

IQR = Q3 - Q1

P95 = incidentes.quantile(0.95)

# ------------------------------------------------------------
# 5. VALORES EXTREMOS
# ------------------------------------------------------------

valor_max = incidentes.max()
valor_min = incidentes.min()

fecha_max = df.loc[incidentes.idxmax(), "fecha"]
fecha_min = df.loc[incidentes.idxmin(), "fecha"]

# ------------------------------------------------------------
# 6. Mostrar resultados
# ------------------------------------------------------------

print("\n================ RESULTADOS =================\n")

print("MEDIDAS DE TENDENCIA CENTRAL")
print(f"Media: {media:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Moda: {moda}")

print("\nMEDIDAS DE DISPERSIÓN")
print(f"Desviación estándar: {desv_std:.2f}")
print(f"Varianza: {varianza:.2f}")
print(f"Coeficiente de variación: {coef_variacion:.4f}")
print(f"Rango: {rango}")

print("\nCUARTILES Y PERCENTILES")
print(f"Q1 (25%): {Q1:.2f}")
print(f"Q2 (Mediana): {Q2:.2f}")
print(f"Q3 (75%): {Q3:.2f}")
print(f"IQR: {IQR:.2f}")
print(f"Percentil 95: {P95:.2f}")

print("\nVALORES EXTREMOS")
print(f"Día con MÁS incidentes: {fecha_max.date()}")
print(f"Valor máximo: {valor_max}")
print(f"Día con MENOS incidentes: {fecha_min.date()}")
print(f"Valor mínimo: {valor_min}")

print("\n=================================================\n")