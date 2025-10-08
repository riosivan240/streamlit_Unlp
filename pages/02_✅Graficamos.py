import streamlit as st
import pandas as pd

import streamlit as st
import matplotlib.pyplot as plt

st.write("En este gráfico se muestra la cantidad de avistamientos de pumas, panteras y leopardos. Se observa que el felino más frecuentemente avistado es el puma, con un total de 1,629 avistamientos.")
st.write("Los leopardos registran 218 avistamientos, mientras que las panteras solo 172, siendo estas las menos vistas.")
felinos = pd.read_csv('felinos.csv')
st.title("Gráfico")
fig,ax = plt.subplots()
# Crear el gráfico de barras
conteo_tipos = felinos['genus'].value_counts()
conteo_tipos.plot(kind='bar', ax=ax, color='skyblue')
# Agregar etiquetas y título
ax.set_xlabel('gatitos')
ax.set_ylabel('Cantidad')
ax.set_title('Cantidad de avistamientos por provincia')

# Mostrar el gráfico
st.pyplot(fig)
