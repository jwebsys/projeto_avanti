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


def grafico_grupos(df2):

    # 4. Comparação do volume de pedidos por cidade e tipo de tráfego
    df_aux = df.groupby(['grupo', 'ava_pcr_resultado'])['ava_pcr_resultado'].count()

    fig = px.scatter( df_aux, x='grupo', y='ava_pcr_resultado', color='ava_pcr_resultado' )
                
    return fig


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


with st.sidebar:
    
    st.header('Projeto AVANTI - Gráficos')
               
    st.sidebar.markdown( """___""" )
    
    var_Grupo = st.selectbox(
        "Selecione o Grupo:",
        options=df['grupo'].unique()
    )

    

# Tabela Grupo
tabela2_grupo = df.loc[(
    df['grupo'] == var_Grupo)
]



##### PADRÕES #########
cor_grafico = '#9DD1F1'
altura_grafico = 250


# VARIÁVEIS 


### PÁGINA PRINCIPAL ###

#st.altair_chart(graf1_qtde_resultado, use_container_width=True)


#fig = grafico_grupos(df)
#st.markdown('###### Grupos ######')
#st.plotly_chart( fig, use_container_width=True)


st.markdown("---")

