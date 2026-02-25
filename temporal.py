# ============================================================
# temporal.py
# Estadísticas temporales de incidentes diarios
# ============================================================

import pandas as pd

# ------------------------------------------------------------
# 1. Cargar datos
# ------------------------------------------------------------

df = pd.read_csv("incidentes_crue_diarios.txt", sep=r"\s+")

# convertir fecha a datetime
df["fecha"] = pd.to_datetime(df["fecha"])

# crear columnas temporales
df["año"] = df["fecha"].dt.year
df["mes"] = df["fecha"].dt.month
df["dia_semana"] = df["fecha"].dt.day_name()

# traducir a español
dias_es = {
    "Monday": "Lunes",
    "Tuesday": "Martes",
    "Wednesday": "Miércoles",
    "Thursday": "Jueves",
    "Friday": "Viernes",
    "Saturday": "Sábado",
    "Sunday": "Domingo"
}

df["dia_semana"] = df["dia_semana"].map(dias_es)

# ------------------------------------------------------------
# 2. PROMEDIO POR AÑO
# ------------------------------------------------------------

prom_2022 = df[df["año"] == 2022]["incidentes"].mean()
prom_2023 = df[df["año"] == 2023]["incidentes"].mean()

diferencia = prom_2023 - prom_2022

# ------------------------------------------------------------
# # ------------------------------------------------------------
# 3. PROMEDIO POR DIA DE LA SEMANA
# ------------------------------------------------------------

# asegurar orden correcto como categoría
orden_dias = [
    "Lunes", "Martes", "Miércoles",
    "Jueves", "Viernes", "Sábado", "Domingo"
]

df["dia_semana"] = pd.Categorical(
    df["dia_semana"],
    categories=orden_dias,
    ordered=True
)

prom_dias = df.groupby("dia_semana", observed=False)["incidentes"].mean()

# rellenar posibles días sin datos con 0
prom_dias = prom_dias.fillna(0)

dia_mas_incidentes = prom_dias.idxmax()

# ------------------------------------------------------------
# 4. PROMEDIO POR MES
# ------------------------------------------------------------

prom_mes = df.groupby("mes")["incidentes"].mean()

top3 = prom_mes.sort_values(ascending=False).head(3)
mes_bajo = prom_mes.idxmin()

# ------------------------------------------------------------
# 5. Mostrar resultados
# ------------------------------------------------------------

print("\n========== PROMEDIO POR AÑO ==========")
print(f"Promedio 2022: {prom_2022:.2f}")
print(f"Promedio 2023: {prom_2023:.2f}")
print(f"Diferencia (2023-2022): {diferencia:.2f}")

print("\n====== PROMEDIO POR DIA DE LA SEMANA ======")

for dia in orden_dias:
    print(f"{dia}: {prom_dias[dia]:.2f}")

print(f"\nDía con MÁS incidentes: {dia_mas_incidentes}")

print("\n========== TOP 3 MESES ==========")

for i, (mes, valor) in enumerate(top3.items(), 1):
    print(f"Mes #{i}: {mes} -> {valor:.2f}")

print(f"\nMes más BAJO: {mes_bajo} -> {prom_mes[mes_bajo]:.2f}")

print("\n=================================")