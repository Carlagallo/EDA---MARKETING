import pandas as pd

# Cargar dataset limpio
df = pd.read_csv("../Datos/output/df_marketing_clean.csv")

# Comprobación rápida
print(df.head())
print(df.info())

df.groupby("month")["y"].value_counts(normalize=True).unstack().plot(kind="bar")
plt.title("Contratación por mes")
plt.show()
