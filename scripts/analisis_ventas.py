
# KAN-3: Revisión QA y mejora de documentación
# Autor: Luis (P3 - Revisor y QA)

import pandas as pd
import matplotlib.pyplot as plt

# Carga del dataset desde la carpeta /datos
df = pd.read_csv("datos/ventas.csv")

# Validación básica: verificar que el archivo no esté vacío
if df.empty:
    raise ValueError("El dataset está vacío. Verificar el archivo fuente.")

print("=== Estadísticas descriptivas ===")
print(df["sales_amount"].describe())

# Cálculo del promedio de ventas
promedio = df["sales_amount"].mean()
print(f"\nPromedio de ventas: {promedio:.2f}")

# Generación del gráfico con línea de promedio
plt.figure(figsize=(8, 4))
plt.plot(df["sales_date"], df["sales_amount"], marker="o", color="steelblue", label="Ventas diarias")
plt.axhline(promedio, color="red", linestyle="--", label=f"Promedio: {promedio:.2f}")
plt.title("Ventas Diarias")
plt.xlabel("Fecha")
plt.ylabel("Monto ($)")
plt.legend()
plt.tight_layout()
plt.savefig("resultados/grafico_ventas.png")
print("Gráfico guardado en /resultados/grafico_ventas.png ✓")
