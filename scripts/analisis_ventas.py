import math
 

# PROY-2: Análisis de Ventas Simuladas - Q1 2024
# Autor: P2 - Paco

 
# Datos de ventas (lista de montos)
ventas = [
    4986, 5143, 3872, 6210, 4500, 5980, 3100, 7200, 4850, 5600,
    6340, 4120, 5780, 4950, 6100, 3800, 5200, 4700, 6500, 5050,
    4300, 5900, 4100, 6700, 5400, 4800, 3600, 5700, 6200, 4900,
    5100, 5300, 4600, 6800, 5000, 4400, 5600, 3900, 6100, 5200,
    4700, 5800, 4300, 6400, 7100, 5500, 4200, 5900, 4800, 6300,
    5100, 4500, 5700, 4000, 6600, 5300, 4900, 3700, 5400, 5800,
    6200, 4700, 5500, 4100, 6900, 5200, 4600, 5800, 4300, 6500,
    5000, 4800, 5700, 4400, 6100, 5300, 4900, 3800, 5600, 6300,
    4700, 5100, 4500, 6700, 5400, 4200, 5800, 4600, 6400, 5200,
    4800
]
 
# Función: calcular promedio
def calcular_promedio(lista):
    total = 0
    for venta in lista:
        total = total + venta
    promedio = total / len(lista)
    return promedio
 
# Función: encontrar el valor máximo
def calcular_maximo(lista):
    maximo = lista[0]
    for venta in lista:
        if venta > maximo:
            maximo = venta
    return maximo
 
# Función: encontrar el valor mínimo
def calcular_minimo(lista):
    minimo = lista[0]
    for venta in lista:
        if venta < minimo:
            minimo = venta
    return minimo
 
#Función: contar ventas por encima del promedio 
def ventas_sobre_promedio(lista, promedio):
    contador = 0
    for venta in lista:
        if venta > promedio:
            contador = contador + 1
    return contador
 
# Función: calcular desviación estándar 
def calcular_desviacion(lista, promedio):
    suma = 0
    for venta in lista:
        diferencia = venta - promedio
        suma = suma + (diferencia ** 2)
    desviacion = math.sqrt(suma / len(lista))
    return desviacion
 
# Función: mostrar reporte
def mostrar_reporte(lista):
    print("=" * 40)
    print("   REPORTE DE VENTAS - Q1 2024")
    print("=" * 40)
 
    promedio   = calcular_promedio(lista)
    maximo     = calcular_maximo(lista)
    minimo     = calcular_minimo(lista)
    desviacion = calcular_desviacion(lista, promedio)
    sobre_prom = ventas_sobre_promedio(lista, promedio)
 
    print(f"Total de registros : {len(lista)}")
    print(f"Venta promedio     : ${promedio:.2f}")
    print(f"Venta máxima       : ${maximo}")
    print(f"Venta mínima       : ${minimo}")
    print(f"Desviación estándar: ${desviacion:.2f}")
    print(f"Días sobre promedio: {sobre_prom} de {len(lista)}")
    print("=" * 40)
 
#Función: mostrar tabla de ventas por mes
def ventas_por_mes(lista):
    print("\n--- VENTAS TOTALES POR MES ---")
 
    meses = ["Enero", "Febrero", "Marzo"]
    dias_por_mes = [31, 29, 31]   # Q1 2024 (febrero tiene 29 días)
 
    inicio = 0
    for i in range(3):
        fin = inicio + dias_por_mes[i]
        mes_ventas = lista[inicio:fin]
 
        total = 0
        for v in mes_ventas:
            total = total + v
 
        print(f"{meses[i]:10}: ${total:,.0f}")
        inicio = fin
 
# Programa principal
mostrar_reporte(ventas)
ventas_por_mes(ventas)
 
