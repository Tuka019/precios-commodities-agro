# Precios de Commodities Agropecuarios Argentina

Análisis de precios de trigo, maíz y soja (pizarra, en pesos) cruzados con el tipo de cambio oficial, para ver su evolución en dólares.

## Fuentes de datos
- Tipo de cambio USD/ARS: API pública del BCRA (Estadísticas Cambiarias)
- Precios de pizarra: Bolsa de Comercio de Rosario

## Decisiones de limpieza
- Los días sin cotización ("S/C") se rellenaron con el último precio conocido (forward fill), asumiendo que un mercado sin operar no cambió de precio.
- Girasol se excluyó del análisis: el 58% de sus días no tenían cotización, demasiado para un relleno confiable.
- El cruce entre datasets usa solo fechas presentes en ambas fuentes.


## Comentarios:
primer proyecto realizado de analisis de datos economicos con CLAUDE, utilizando el preico de los commodities agropecuarios argentinos, con el tipo de cambio (fuente Bcra), los pasos detallados del proceso de aprendizaje seran cargados en otra carpeta (esta contendra de manera textual como fue todo el proceso para llevar a cabo esto, con los scrips y traduciendo lo que se llevo a cabo)


## Estado
✅ Datos obtenidos, limpiados, cruzados y calculados en USD.
🚧 Pendiente: dashboard en Power BI.