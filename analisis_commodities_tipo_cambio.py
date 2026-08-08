import pandas as pd

tipo_cambio = pd.read_csv("data/processed/tipo_cambio_usd.csv")
precios = pd.read_csv("data/processed/precios_pizarra.csv")

tipo_cambio["fecha"] = pd.to_datetime(tipo_cambio["fecha"])
precios["fecha"] = pd.to_datetime(precios["fecha"]).dt.normalize()

df = pd.merge(precios, tipo_cambio, on="fecha", how="inner")

print("Filas después del cruce:", df.shape)
print(df.head())

#paso 2 
df["trigo_usd"] = df["trigo"] / df["valor_usd"]
df["maiz_usd"] = df["maiz"] / df["valor_usd"]
df["soja_usd"] = df["soja"] / df["valor_usd"]

print(df[["fecha", "trigo_usd", "maiz_usd", "soja_usd"]].head())

#paso 3
print(df[["trigo_usd", "maiz_usd", "soja_usd"]].describe())

#paso 4
import matplotlib
matplotlib.use("Agg")

grafico = df.plot(x="fecha", y=["trigo_usd", "maiz_usd", "soja_usd"], title="Precios en USD/tonelada")
grafico.get_figure().savefig("data/processed/grafico_precios_usd.png")

#paso 5
df.to_csv("data/processed/analisis_final.csv", index=False)