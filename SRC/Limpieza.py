import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


import sys
sys.executable
sys.path.append('../')


import openpyxl
openpyxl.__version__
pd.__version__

df_marketing = pd.read_csv('../Datos/raw/bank-additional.csv')

# Snake case para nombres de columnas

df_marketing.columns = (
    df_marketing.columns
        .str.strip()
        .str.lower()
        .str.replace(' ', '_')
        .str.replace('.', '_', regex=False)
)
df_marketing.columns

df_marketing.rename(columns={'id_': 'id'}, inplace=True)


# Manejo de valores nulos en variables categóricas"""

def categorical_cols(df, columnas):
    for col in columnas:
        df[col] = df[col].fillna('unknown')
    return df
 
categorical_cols_list = [
    'job',
    'marital',
    'education',
    'default',
    'housing',
    'loan'
]

df_marketing['euribor3m']= df_marketing ['euribor3m'].fillna(4.857)

df_marketing['cons_price_idx'] = df_marketing['cons_price_idx'].astype(str).str.replace(',', '.').str.strip()

df_marketing['cons_price_idx'] = pd.to_numeric(df_marketing['cons_price_idx'], errors='coerce')

df_marketing['cons_price_idx'] = df_marketing['cons_price_idx'].fillna(df_marketing['cons_price_idx'].median())



meses = {
    "enero": "01",
    "febrero": "02",
    "marzo": "03",
    "abril": "04",
    "mayo": "05",
    "junio": "06",
    "julio": "07",
    "agosto": "08",
    "septiembre": "09",
    "octubre": "10",
    "noviembre": "11",
    "diciembre": "12"
}

df_marketing["date"] = (
    df_marketing["date"]
    .str.lower()
    .str.strip()
)

for mes_texto, mes_num in meses.items():
    df_marketing["date"] = df_marketing["date"].str.replace(
        f"-{mes_texto}-",
        f"-{mes_num}-",
        regex=False
    )
df_marketing["date"] = pd.to_datetime(
    df_marketing["date"],
    format="%d-%m-%Y",
    errors="coerce"
)

def impute_date_with_median(df, date_col):
    #Imputa valores nulos en una variable de fecha utilizando la mediana, creando previamente una variable indicadora y generando features temporales para análisis.
    
    # Variable indicadora: 1 si la fecha es nula, 0 si no
    df[f'{date_col}_missing'] = df[date_col].isnull().astype(int)

    # Cálculo de la mediana
    fecha_mediana = df[date_col].median()

    # Imputación de la fecha
    df[f'{date_col}_imputed'] = df[date_col].fillna(fecha_mediana)

# Normalización de "age" y se completan nulos con la mediana

df_marketing["age"] = df_marketing["age"].astype(int)

df_marketing['age'] = df_marketing['age'].fillna(df_marketing['age'].median())

#Normalización de "education"

df_marketing["education"] = df_marketing["education"].replace({
    "basic.4y": "basic",
    "basic.6y": "basic",
    "basic.9y": "basic",
    "high.school": "high school",
    "illiterate": "unknown"
})

# Datafreame limpio

df_marketing.to_csv("../Datos/output/df_marketing_clean.csv",
    index=False)

#Análisis del dataframe limpio
df_marketing_clean = pd.read_csv("../Datos/output/df_marketing_clean.csv")

#Varible objetivo "y"

df_marketing_clean["y"].value_counts(normalize=True)

plt.figure(figsize=(5,4))
df_marketing_clean["y"].value_counts().plot(kind="bar")
plt.title("Distribución de la variable objetivo (y)")
plt.xlabel("Suscripción")
plt.ylabel("Número de clientes")
plt.show()

#Análisis de variables categóricas

cat_cols = ["job", "education", "marital", "contact"]

for col in cat_cols:
    display(
        pd.crosstab(
            df_marketing_clean[col],
            df_marketing_clean["y"],
            normalize="index"
        ).round(3)
    )
#
# Análisis de variables numéricas

df_marketing_clean.groupby("y")[[
    "age",
    "duration",
    "campaign",
    "previous"
]].mean().round(2)

# Análisis de duración de la llamada vs suscripción

plt.figure(figsize=(6,4))
sns.boxplot(data=df_marketing_clean, x="y", y="duration")
plt.title("Duración de la llamada vs suscripción")
plt.show()

# Análisis de número de contactos durante la campaña vs suscripción

plt.figure(figsize=(6,4))
sns.boxplot(data=df_marketing_clean, x="y", y="campaign")
plt.title("Número de contactos durante la campaña")
plt.show()

#Análisis variable temporal "date"

plt.figure(figsize=(5,4))
sns.countplot(data=df_marketing_clean, x="date_missing", hue="y")
plt.title("Conversión según disponibilidad de fecha")
plt.xlabel("Fecha ausente (1 = sí, 0 = no)")
plt.ylabel("Número de campañas")
plt.show()

df_marketing_clean["y_bin"] = df_marketing_clean["y"].map({
    "yes": 1,
    "no": 0
})

conversion_by_month = (
    df_marketing_clean
    .groupby("month")["y_bin"]
    .mean()
)

# Visualización de la tasa de conversión por mes

plt.figure(figsize=(7,4))
conversion_by_month.plot(marker="o")
plt.title("Tasa de conversión media por mes")
plt.xlabel("Mes")
plt.ylabel("Tasa de conversión")
plt.grid(True)
plt.show()


# Matriz de correlación para variables numéricas

num_cols = df_marketing_clean.select_dtypes(include=np.number)

num_cols.columns = num_cols.columns.astype(str)

num_cols = num_cols.loc[:, ~num_cols.columns.str.lower().str.contains("unnamed")]

corr = num_cols.corr()

plt.figure(figsize=(12,8))
sns.heatmap(corr, cmap="coolwarm", center=0)
plt.title("Matriz de correlación - Dataset Marketing")
plt.show()

#Análisis dataframe "Clientes"

df_customers = pd.read_excel('../Datos/raw/customer-details.xlsx')

# Concatenación de hojas del archivo Excel

df_customers = pd.concat(
    xls.values(),
    ignore_index=True
)

#Snake case para nombres de columnas

df_customers.columns = (
    df_customers.columns
        .str.strip()
        .str.lower()
        .str.replace(' ', '_')
        .str.replace('.', '_', regex=False)
)

# se guardan los datos limpios en un nuevo archivo CSV

df_customers.to_csv("../Datos/output/df_customers_clean.csv",
    index=False)

#Dataframe limpio de clientes

df_customers_clean = pd.read_csv("../Datos/output/df_customers_clean.csv")

df_customers_clean["income"].hist(bins=50)
plt.title("Distribución de ingresos")
plt.show()

df_customers_clean[["kidhome", "teenhome"]].value_counts()

df_customers_clean["numwebvisitsmonth"].hist(bins=20)
plt.title("Visitas web mensuales")
plt.show()

#Cruce de dataframes

df_resultado = df_customers_clean.merge(
    df_marketing_clean,
    on='id',
    how='outer',
    indicator=True
)

# Análisis de ingresos vs suscripción

df_resultado.groupby("y")["income"].mean().round(2)

plt.figure(figsize=(6,4))
sns.boxplot(data=df_resultado, x="y", y="income")
plt.title("Ingresos vs suscripción")
plt.show()

# Análisis de número de visitas web mensuales vs suscripción
df_resultado.groupby("y")["numwebvisitsmonth"].mean().round(2)

#Matriz de correlación
plt.figure(figsize=(12,8))
sns.heatmap(
    corr,
    cmap="coolwarm",
    center=0
)
plt.title("Matriz de correlación – Dataset unificado")
plt.show()

