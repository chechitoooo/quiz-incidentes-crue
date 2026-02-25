# 📊 Análisis de Incidentes (2022-2023)

## 📋 Descripción de los datos
Este proyecto analiza una base de datos de incidentes registrados durante el período **2022-2023**.  
- **Total de registros:** 730 (1 por día)  
- **Período:** 01/01/2022 al 31/12/2023  

Los datos incluyen el número diario de incidentes y su evolución temporal, permitiendo calcular medidas de tendencia central, dispersión, cuartiles, así como promedios por año, mes y día de la semana.

## 👥 Colaboradores

| Nombre            | GitHub                                      |
|-------------------|---------------------------------------------|
| Sergio Huertas      | [github.com/estudianteA](https://github.com/chechitooo) |
| Sergio Prieto      | [github.com/estudianteB](https://github.com/ssseergiopp) |

## 🔍 Hallazgos principales

| Estadística                               | Valor         |
|-------------------------------------------|---------------|
| Promedio diario de incidentes             | 1717.47       |
| Mediana                                   | 1711.0        |
| Moda (valor más frecuente)                | 1812          |
| Desviación estándar                       | 256.31        |
| Varianza                                  | 65694.62      |
| Coeficiente de variación                  | 0.1492        |
| Rango (máx - mín)                         | 2340          |
| Q1 (percentil 25)                         | 1559.50       |
| Q3 (percentil 75)                         | 1859.0        |
| Rango intercuartílico (IQR)               | 299.50        |
| Percentil 95                              | 2081.75       |
| Día con más incidentes                     | 2022-12-25 (3275) |
| Día con menos incidentes                   | 2022-04-15 (935)  |
| Promedio 2022                              | 1667.10       |
| Promedio 2023                              | 1767.85       |
| Diferencia 2023-2022                       | +100.75       |
| Día de la semana con más incidentes        | Domingo (1880.04) |
| Mes con más incidentes                      | Diciembre (1881.02) |
| Mes con menos incidentes                    | Enero (1460.61)   |

## 🤔 ¿Se puede predecir?
Sí, se observan patrones estacionales claros: los incidentes aumentan los fines de semana y en los últimos meses del año. Sin embargo, la alta variabilidad diaria (desviación estándar de 256) sugiere que un modelo predictivo debería considerar tanto la estacionalidad como factores externos no incluidos en estos datos (clima, eventos especiales, etc.). Un enfoque de series temporales (como ARIMA o Prophet) podría ofrecer predicciones razonables a corto plazo.

