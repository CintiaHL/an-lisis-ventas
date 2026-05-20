# Análisis de Ventas Simuladas — Q1 2024

## Integrantes del equipo

| Rol | Nombre | Responsabilidad |
|-----|--------|-----------------|
| P1 - Líder y Organizador | Hugo | Gobernanza del repositorio, estructura de carpetas, README |
| P2 - Desarrollador Técnico | Paco | Script de análisis estadístico en Python |
| P3 - Revisor y QA | Luis | Peer review, documentación, Pull Request y merge final |

## Escenario elegido

Análisis exploratorio de ventas comerciales diarias correspondientes al primer trimestre del año 2024 (Q1 2024), identificando tendencias, estadísticas descriptivas y comportamiento mensual de los ingresos.

## Dataset utilizado

- **Nombre:** Dataset de Ventas Simuladas
- **Fuente:** Datos ficticios generados para ejercicios educativos
- **Formato:** CSV
- **Registros:** 91 registros diarios (01/01/2024 — 31/03/2024)
- **Columnas:**
  - `id` — Identificador único del registro
  - `sales_date` — Fecha de la venta (YYYY-MM-DD)
  - `sales_amount` — Monto de venta en pesos ($)
- **Ubicación en el repositorio:** `/datos/ventas.csv`

## Estructura del repositorio

```
proyecto/
├── datos/
│   └── ventas.csv              # Dataset de ventas Q1 2024
├── scripts/
│   └── analisis_ventas.py      # Script principal de análisis
├── resultados/
│   ├── resumen_estadistico.csv
│   ├── ventas_mensuales.csv
│   ├── grafico_ventas_diarias.png
│   └── grafico_ventas_mensuales.png
├── README.md
└── .gitignore
```

## Instrucciones para ejecutar el script

### Opción A — Local

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/usuario/repo.git
   cd repo
   ```
2. Instalar dependencias:
   ```bash
   pip install pandas matplotlib
   ```
3. Ejecutar el script:
   ```bash
   cd scripts
   python analisis_ventas.py
   ```

### Opción B — Google Colab

1. Clonar el repositorio en Colab:
   ```python
   !git clone https://github.com/usuario/repo.git
   %cd repo/scripts
   ```
2. Instalar dependencias:
   ```python
   !pip install pandas matplotlib
   ```
3. Ejecutar:
   ```python
   !python analisis_ventas.py
   ```

Los resultados se guardan automáticamente en la carpeta `/resultados/`.
