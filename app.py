import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import plotly.express as px

# Configurar la página
st.set_page_config(page_title="Análisis de Incidentes", layout="wide")

# Cargar el archivo Parquet
df = pd.read_parquet('homicidios_bolivar.parquet')

# Introducción
st.title("Análisis de Homicidios en el Departamento de Bolívar")
st.markdown("""
Este análisis presenta los datos relacionados con los homicidios ocurridos en el departamento de Bolívar, Colombia, desde el año 2017 hasta el 2024. Se han seleccionado diversas variables para evaluar la cantidad de incidentes por municipio, tipo de arma empleada y la evolución temporal de estos hechos. 
Utilizando gráficos interactivos, podemos obtener una mejor comprensión de cómo han variado los homicidios a lo largo del tiempo y su distribución geográfica.
""")

# Barra lateral para filtros
st.sidebar.header('Filtros')

# Filtro por rango de fechas (Años)
min_year, max_year = 2017, 2024
rango_fechas = st.sidebar.slider('Seleccionar rango de años', min_year, max_year, (min_year, max_year))

# Filtro por tipo de arma
tipo_arma = st.sidebar.multiselect(
    'Seleccionar Tipo de Arma',
    ['ARMA DE FUEGO', 'ARMA BLANCA / CORTOPUNZANTE', 'CONTUNDENTES', 'ARTEFACTO EXPLOSIVO/CARGA DINAMITA',
     'CUERDA/SOGA/CADENA', 'SIN EMPLEO DE ARMAS', 'ALMOHADA', 'MINA ANTIPERSONA'],
    default=['ARMA DE FUEGO', 'ARMA BLANCA / CORTOPUNZANTE', 'CONTUNDENTES']
)

# Filtro por municipio
municipios = st.sidebar.multiselect(
    'Seleccionar Municipio',
    ['CARTAGENA (CT)', 'EL CARMEN DE BOLÍVAR', 'SAN PABLO', 'MAGANGUÉ', 'ARJONA', 'TURBACO', 'SANTA ROSA DEL SUR',
     'MARÍA LA BAJA', 'SANTA ROSA', 'SIMITÍ', 'VILLANUEVA', 'NOROSÍ', 'MORALES', 'SANTA CATALINA', 'MOMPÓS', 'MONTECRISTO',
     'SAN JACINTO', 'MAHATES', 'CANTAGALLO', 'TIQUISIO', 'BARRANCO DE LOBA', 'CLEMENCIA', 'ACHÍ', 'CALAMAR'],
    default=['CARTAGENA (CT)', 'MAGANGUÉ', 'TURBACO']
)

# Filtro por género
genero = st.sidebar.selectbox('Seleccionar Género', ['Ambos', 'MASCULINO', 'FEMENINO'])

# Aplicar filtros
df_filtrado = df[(df['FECHA HECHO'].dt.year >= rango_fechas[0]) & (df['FECHA HECHO'].dt.year <= rango_fechas[1])]
df_filtrado = df_filtrado[df_filtrado['ARMA MEDIO'].isin(tipo_arma)]
df_filtrado = df_filtrado[df_filtrado['MUNICIPIO'].isin(municipios)]

# Filtro por género
if genero != 'Ambos':
    df_filtrado = df_filtrado[df_filtrado['GENERO'].str.contains(genero)]

# Distribuir gráficos en dos columnas
col1, col2 = st.columns(2)

# Gráfico de barras - Número de incidentes por tipo de arma y género
col1.header("Número de Incidentes por Tipo de Arma y Género")
fig_barras, ax = plt.subplots()
df_arma_genero = df_filtrado.groupby(['ARMA MEDIO', 'GENERO'])['CANTIDAD'].sum().reset_index()

# Crear el gráfico de barras con distinción por género
sns.barplot(x='ARMA MEDIO', y='CANTIDAD', hue='GENERO', data=df_arma_genero, ax=ax)

# Añadir etiquetas con los totales en las barras
for p in ax.patches:
    ax.annotate(f'{p.get_height():.0f}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='baseline', fontsize=10, color='black', xytext=(0, 3),
                textcoords='offset points')

ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
ax.set_title("Número de Incidentes por Tipo de Arma y Género")
col1.pyplot(fig_barras)

# Gráfico de líneas - Evolución de los incidentes a lo largo del tiempo
col2.header("Evolución de los Incidentes a lo Largo del Tiempo")
df_tiempo = df_filtrado.groupby(df_filtrado['FECHA HECHO'].dt.to_period('M'))['CANTIDAD'].sum().reset_index()
df_tiempo['FECHA HECHO'] = df_tiempo['FECHA HECHO'].dt.to_timestamp()
fig_lineas = px.line(df_tiempo, x='FECHA HECHO', y='CANTIDAD', title='Incidentes a lo largo del tiempo')
col2.plotly_chart(fig_lineas)

# Distribuir gráficos en dos columnas
col3, col4 = st.columns(2)

# Gráfico de pastel - Distribución de incidentes por municipio
col3.header("Distribución de Incidentes por Municipio")
df_municipios = df_filtrado.groupby('MUNICIPIO')['CANTIDAD'].sum().reset_index()
fig_pie = px.pie(df_municipios, names='MUNICIPIO', values='CANTIDAD', title='Distribución de Incidentes por Municipio')
col3.plotly_chart(fig_pie)

# Gráfico de calor - Relación entre municipios y tipos de armas
col4.header("Relación entre Municipios y Tipos de Armas Utilizadas")
df_calor = df_filtrado.pivot_table(index='MUNICIPIO', columns='ARMA MEDIO', values='CANTIDAD', aggfunc='sum', fill_value=0)
fig_calor, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(df_calor, annot=True, cmap='coolwarm', ax=ax)
col4.pyplot(fig_calor)

# Mostrar tabla de datos filtrados
st.header("Datos Filtrados")
st.write(df_filtrado)
