# Libraries
import altair as alt
import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image

from haversine import haversine
import plotly.express as px
import plotly.graph_objects as go
import folium
from streamlit_folium import st_folium, folium_static


# --- Criar o dataframe
df = pd.read_csv('./datasets/dbavanti.csv', sep=';')
fortaleza = pd.read_csv("./datasets/dados.csv")

# =========================================================
# Barra Lateral
# =========================================================

#image_path = 'logo.png'
#image = Image.open( 'logo.png' )
#st.sidebar.image( image, width=120 )


st.set_page_config(
    page_title='Nubimed - Projeto Avanti ',
    page_icon='chart_with_upwards_trend',
    layout='wide',
    initial_sidebar_state='expanded',
    
)


##### PADRÕES #########
cor_grafico = '#9DD1F1'
altura_grafico = 250


### PÁGINA PRINCIPAL ###

#st.map(fortaleza)


st.header('Projeto AVANTI - Visão Geográfica - Mapa de Fortaleza')

fig = px.scatter_mapbox(fortaleza, lat="lat", lon="lon", hover_name='ID',zoom=11)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
st.plotly_chart(fig)

    
st.markdown("---")

