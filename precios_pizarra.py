import pandas as pd

df = pd.read_excel("data/raw/precios_pizarra_bcr.xlsx", header=4)

limpio = pd.DataFrame({
    "fecha": df.iloc[:, 0],
    "trigo": pd.to_numeric(df.iloc[:, 1], errors="coerce"),
    "maiz": pd.to_numeric(df.iloc[:, 8], errors="coerce"),
    "soja": pd.to_numeric(df.iloc[:, 22], errors="coerce"),
})

limpio["fecha"] = pd.to_datetime(limpio["fecha"])
limpio = limpio.sort_values("fecha")

print("Faltantes antes de rellenar:")
print(limpio[["trigo", "maiz", "soja"]].isna().sum())

limpio[["trigo", "maiz", "soja"]] = limpio[["trigo", "maiz", "soja"]].ffill()

limpio.to_csv("data/processed/precios_pizarra.csv", index=False)

print(limpio.head())
print(limpio.shape)