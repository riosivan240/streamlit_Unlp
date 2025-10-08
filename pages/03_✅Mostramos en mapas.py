import folium
import streamlit as st
from streamlit_folium import folium_static, st_folium
import pandas as pd

def generar_mapa():
    attr = (
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> '
        'contributors, &copy; <a href="https://cartodb.com/attributions">CartoDB</a>'
    )
    
    tiles = 'https://wms.ign.gob.ar/geoserver/gwc/service/tms/1.0.0/capabaseargenmap@EPSG%3A3857@png/{z}/{x}/{-y}.png'
    m = folium.Map(
        location=(-33.457606, -65.346857),
        control_scale=True,
        zoom_start=5,
        name='es',
        tiles=tiles,
        attr=attr
    )
    return m


felinos = pd.read_csv('felinos.csv')
st.title("Mapa")
mapa = generar_mapa()

st.write("En esta sección se puede visualizar un mapa en el cual se puede seleccionar qué tipo de felino se quiere ver en dicho mapa.")
st.write("Curiosamente, se puede observar que solo en Misiones se avistaron panteras, mientras que en el resto de las provincias se registraron más avistamientos de pumas que de leopardos.")

def agregar_marca_aerop(row):
    
    #st.write(color)
    folium.Marker(
        [row['lat'], row['lng']],
        popup=row['species'],
        icon=folium.Icon()
        ).add_to(mapa)

ac1,ac2 = st.columns([0.3, 0.7])

pumas = ac1.checkbox("Puma")
if pumas:
    a_larg = felinos[felinos['genus']=='Puma']
    a_larg.apply(agregar_marca_aerop, axis=1)

Panthera = ac1.checkbox("Panthera")
if Panthera:
    a_larg = felinos[felinos['genus']=='Panthera']
    a_larg.apply(agregar_marca_aerop, axis=1)

Leopardus = ac1.checkbox("Leopardus")
if Leopardus:
    a_larg = felinos[felinos['genus']=='Leopardus']
    a_larg.apply(agregar_marca_aerop, axis=1)





with ac2:
    st_folium(mapa, key='lagos')
