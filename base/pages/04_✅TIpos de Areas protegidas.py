import folium
import streamlit as st
from streamlit_folium import folium_static, st_folium
import pandas as pd

areas = pd.read_csv('area_protegida.csv')

ac1,ac2 = st.columns([0.3, 0.7])
r_areas = ac1.checkbox("Parque")
if r_areas:
    a_larg = areas[areas['tap']=='1']
r_parques = ac1.checkbox("Reserva")
if r_parques:
    a_med = areas[areas['tap']=='2']
r_monu = ac1.checkbox("Monumento Natural")
if r_monu:
    a_small = areas[areas['tap']=='3']