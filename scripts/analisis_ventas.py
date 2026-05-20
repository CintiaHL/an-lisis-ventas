
# KAN-2: Script de análisis estadístico de ventas
# Autor: Paco (P2 - Desarrollador Técnico)

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("datos/ventas.csv")

print("=== Estadísticas descriptivas ===")
print(df["sales_amount"].describe())

promedio = df["sales_amount"].mean()
print(f"\nPromedio de ventas: {promedio:.2f}")

plt.figure(figsize=(8, 4))
plt.plot(df["sales_date"], df["sales_amount"], marker="o", color="steelblue")
plt.axhline(promedio, color="red", linestyle="--", label=f"Promedio: {promedio:.2f}")
plt.title("Ventas Diarias")
plt.xlabel("Fecha")
plt.ylabel("Monto ($)")
plt.legend()
plt.tight_layout()
plt.savefig("resultados/grafico_ventas.png")
print("Gráfico guardado en /resultados/grafico_ventas.png ✓")
