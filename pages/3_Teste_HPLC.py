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


# VARIÁVEIS 

# TESTES DE HPLC ->  Contar [ava_hplc_data] na tabela Enrolled
var_testes_hplc = df[df.columns[9]].count()



### PÁGINA PRINCIPAL ###


with st.container():
    
    st.write('**PROJETO AVANTI**')
    st.write('**Teste HPLC**')

    st.markdown("---")
            
    col1, col2, col3 = st.columns([1,2,4])
    
    with col1:
        st.write('**Quantidade**')        
        st.info(f"{var_testes_hplc}")

         
    st.markdown("---")

