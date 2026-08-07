import requests
import pandas as pd

url = "https://api.bcra.gob.ar/estadisticascambiarias/v1.0/Cotizaciones/USD"
parametros = {
    "fechadesde": "2024-01-01",
    "fechahasta": "2026-08-06"
}

respuesta = requests.get(url, params=parametros)
datos = respuesta.json()

registros = []
for dia in datos["results"]:
    fecha = dia["fecha"]
    valor = dia["detalle"][0]["tipoCotizacion"]
    registros.append({"fecha": fecha, "valor_usd": valor})

df = pd.DataFrame(registros)
df["fecha"] = pd.to_datetime(df["fecha"])
df = df.sort_values("fecha")

df.to_csv("data/processed/tipo_cambio_usd.csv", index=False)

print(df.head())
print(df.shape)