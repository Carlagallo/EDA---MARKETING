# EDA---MARKETING
Proyecto EDA/python - ThePower

Estructura de capertas:

EDA---MARKETING/
│
├── Datos/
│   ├── raw/
│   │   └── bank-additional.csv
│   │   └──customer-details
│   │
│   └── Output
│       └── df_marketing_clean.csv
│       └── df_customers_clean
│
├── notebooks/
│   └── 01-Analisis_preeliminar.ipynb
│
└── src/
    └── Limpieza.py/
└── Análisis documental
    └── Desarrollo del Análisis Exploratorio de Datos
└── README
└── (W) DataProject_ Proyecto EDA con Python


Para este proyecto se han proporcionado dos conjunto de datos "bank-additional" y "customer-details"

 ## LIMPIEZA DE DATASETS

Se realiza un anális de la información (columnas, tipo de datos, nulos, duplicados) y en base a ello se toman decisiónes que posibiliten su normalización y mejora de los datos para el posterior análisis. 

# Datos limpios:

Una vez finalizada la limpieza y normalización de los datos, se generó un dataset procesado que fue utilizado como base para los análisis descriptivos, separando claramente la fase de preparación de datos de la fase de análisis.

df_customers_clean
df_marketing_clean

# Comentarios sobre el proceso:

El proceso no fue lineal, ya que el tratamiento de datos me ha generado dificultades por mi falta de experiencia y he ido de menos a más en una primera etapa donde realizaba limpieza o normalización por dato, intentando trasladarlo a toda una serie hasta que pude advertir la posibilidad de realizar funciones que llevaran esa ejecución a tipo de series (por ejemplo normalización de series numericas en una sola función)
Lo mismo sucedio con la información nula o faltante, fui avanzando en decisiones más elevadas mientras se desarrollaba la transformación logrando incoporar acciones de mayor profundidad. 
 
 ## Resumen y Conclusiones: 

 Se ha trabajado con dos dataset en limpieza y transformación, se genero un dataset unificado por la variable ID y se logro un análisis de casusticas. 

 Se observa información importante sobre la tasa de conversión, la duración de llamadas, y se advierte un mayor números de clientes en base de datos que alcanzados por la campaña. 
 Respecto de los clientes se observan variedad socioeconomica. 

 La conclusiones del análisis se desarollan con más profundidad en el archivo "Desarrollo del Análisis Exploratorio de Datos"
