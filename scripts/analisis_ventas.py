
# KAN-2: Script de análisis estadístico de ventas simuladas
# Autor: Paco (P2 - Desarrollador Técnico)
# Dataset: ventas simuladas Q1 2024

import pandas as pd
import matplotlib.pyplot as plt

# Carga del dataset desde la carpeta /datos
df = pd.read_csv("datos/ventas.csv")

# Análisis estadístico descriptivo
print("=== Estadísticas descriptivas ===")
print(df["sales_amount"].describe())

# Cálculo del promedio de ventas
promedio = df["sales_amount"].mean()
print(f"Promedio de ventas: {promedio:.2f}")

# Generación del gráfico de ventas diarias
plt.figure(figsize=(8, 4))
plt.plot(df["sales_date"], df["sales_amount"], marker="o", color="steelblue")
plt.axhline(y=promedio, color="red", linestyle="--", label="Promedio")
plt.title("Ventas Diarias - Q1 2024")
plt.xlabel("Fecha")
plt.ylabel("Monto ($)")
plt.legend()
plt.tight_layout()
plt.savefig("resultados/grafico_ventas.png")
print("Gráfico guardado en /resultados/grafico_ventas.png")
