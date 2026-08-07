import pandas as pd

df = pd.read_excel("data/raw/precios_pizarra_bcr.xlsx")

print(df.columns.tolist())
print(df.head(8))
print(df.shape)