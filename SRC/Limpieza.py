import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import sys
sys.executable
sys.path.append('../')
from SRC import Limpieza as lp

import openpyxl
openpyxl.__version__
pd.__version__

df_marketing = pd.read_csv('../Datos/raw/bank-additional.csv')

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

df_marketing.to_csv("../Datos/output/df_marketing_clean.csv",
    index=False)