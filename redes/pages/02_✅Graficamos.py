import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

redes = pd.read_csv('digital.csv')


st.title("Gráfico de Edades")
st.write("El siguiente gráfico muestra la cantidad de jóvenes encuestados por cada edad.")

conteo_edades = redes['Edad'].value_counts().sort_index()

# Crear la figura
fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(conteo_edades.index, conteo_edades.values, color='skyblue', edgecolor='black')

# Agregar etiquetas y título
ax.set_xlabel('Edad', fontsize=12)
ax.set_ylabel('Cantidad de jóvenes', fontsize=12)
ax.set_title('Distribución de edades de los encuestados', fontsize=14)
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Mostrar valores encima de las barras
for i, v in enumerate(conteo_edades.values):
    ax.text(conteo_edades.index[i], v + 0.1, str(v), ha='center', fontsize=10)

# Mostrar gráfico en Streamlit
st.pyplot(fig)

with st.expander("Ver tabla con cantidad por edad"):
    st.write(conteo_edades)

