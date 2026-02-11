import pandas as pd
import matplotlib.pyplot as plt

# Cargar dataset limpio
df = pd.read_csv("../Datos/output/df_marketing_clean.csv")

# Comprobación rápida
print(df.head())
print(df.info())
print(df.describe())    

# Normalizar columnas (snake_case)

df_marketing.columns = (
    df_marketing.columns
        .str.strip()
        .str.lower()
        .str.replace(' ', '_')
        .str.replace('.', '_', regex=False)
)

df_marketing.rename(columns={'id_': 'id'}, inplace=True)

print(df_marketing.columns)

"""Manejo de valores nulos en variables categóricas"""

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
df_marketing = categorical_cols(df_marketing, categorical_cols_list)

"""Se completa el valor nulo de la variable 'euribor3m' con el dato faltante que es el mismo en todos los casos"""

df_marketing['euribor3m']= df_marketing ['euribor3m'].fillna(4.857)

"""Se completa el valor nulo de la variable 'age' con la mediana de la misma"""

df_marketing['age'] = df_marketing['age'].fillna(df_marketing['age'].median())

""" Se cambia el formato de la variable 'cons_price_idx' para convertirla a numérica """

df_marketing['cons_price_idx'] = df_marketing['cons_price_idx'].astype(str).str.replace(',', '.').str.strip()

df_marketing['cons_price_idx'] = pd.to_numeric(df_marketing['cons_price_idx'], errors='coerce')

# Se completa el valor nulo de la variable 'cons_price_idx' con la mediana de la misma"""

df_marketing['cons_price_idx'] = df_marketing['cons_price_idx'].fillna(df_marketing['cons_price_idx'].median())


#Creación de diccionario de meses"""

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

# Reemplazo de meses en texto por meses en número"""

for mes_texto, mes_num in meses.items():
    df_marketing["date"] = df_marketing["date"].str.replace(
        f"-{mes_texto}-",
        f"-{mes_num}-",
        regex=False
    )

    
def impute_date_with_median(df, date_col):
    
    #Imputa valores nulos en una variable de fecha utilizando la mediana, creando previamente una variable indicadora y generando features temporales para análisis.
    
    # Variable indicadora: 1 si la fecha es nula, 0 si no
    df[f'{date_col}_missing'] = df[date_col].isnull().astype(int)

    # Cálculo de la mediana
    fecha_mediana = df[date_col].median()

    # Imputación de la fecha
    df[f'{date_col}_imputed'] = df[date_col].fillna(fecha_mediana)

    # Variables temporales
    df['year'] = df[f'{date_col}_imputed'].dt.year
    df['month'] = df[f'{date_col}_imputed'].dt.month
    df['weekday'] = df[f'{date_col}_imputed'].dt.day_name()

    return df

df_marketing = impute_date_with_median(df_marketing, 'date')
df_marketing[['date', 'date_missing', 'date_imputed', 'year', 'month', 'weekday']].head()