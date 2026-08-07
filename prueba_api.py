import requests

url = "https://api.bcra.gob.ar/estadisticascambiarias/v1.0/Cotizaciones/USD"

respuesta = requests.get(url)

print(respuesta.status_code)
print(respuesta.json())
