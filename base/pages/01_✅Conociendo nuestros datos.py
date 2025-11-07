import pandas as pd
import streamlit as st

# Cargar datos
redes = pd.read_csv('digital.csv')

# Título y descripción
st.title("Parte 1")
st.header("Redes Sociales y jóvenes")
st.write("Este archivo CSV contiene los datos sobre una encuesta dirigida a los jóvenes sobre cuánto tiempo utilizan "
         "dichas redes de su preferencia.")

# Mostrar dimensiones del dataset
filas, columnas = redes.shape
with st.expander("¿Cuántas filas y columnas tiene el dataset?"):
    st.write(f"Tiene {filas} filas y {columnas} columnas")

# Obtener valores únicos
valores_edad = redes['Edad'].unique()
cant_ubic = len(valores_edad)
nombres_ubic = redes['Género'].unique()

# Mostrar valores únicos de Edad
with st.expander("¿Cuántos y cuáles son los valores únicos de la columna Edad?"):
    st.write(f"Hay {cant_ubic} valores únicos en la columna 'Edad':")
    st.write(valores_edad)

# Mostrar valores únicos de Género
with st.expander("¿Cuáles son los valores únicos de la columna Género?"):
    st.write(nombres_ubic)

# Mostrar nombres de las columnas
with st.expander("¿Cuáles son los nombres de las columnas?"):
    st.write(redes.columns)


        