import pandas as pd
import streamlit as st

felinos =  pd.read_csv('felinos.csv')
st.title("Parte 1")

st.header("Datos que encontraron")
st.write("En esta base de datos de gatitos, primero revisé los valores únicos de algunas columnas para entender mejor qué tipo de información contenían. También exploré todas las columnas disponibles para ver cómo estaban organizados los datos. A partir de eso, hice algunos análisis y creé gráficos que ayudaron a visualizar mejor la información y a encontrar ciertos patrones o curiosidades dentro del conjunto de datos.")
filas, columnas = felinos.shape
with st.expander("¿Cuántas filas y columnas tiene el dataset de Felinos?"):
    filas, columnas = felinos.shape
    st.write(f'Tiene { filas} filas y {columnas} columnas')


nombres_ubic = felinos['stateProvince'].unique()
cant_ubic = len(felinos['genus'].unique())


with st.expander("¿Cuáles son los valores unicos de la columna genus?"):
    st.write(cant_ubic)
with st.expander("¿Cuáles son los valores unicos de la columna statePronvince?"):
    st.write(nombres_ubic)
with st.expander("¿Cuáles son los nombres de las columnas ?"):

    st.write(felinos.columns)

