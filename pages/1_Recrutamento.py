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


with st.sidebar:
    
            
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

var_outros = 66

# SELECIONADOS -> Contar ->  [ava_pid] e somar com -> Outros
var_selecionados = df[df.columns[3]].count() + var_outros


# RECRUTADOS -> (Somar [ava_pid] na tabela Enrolled)
var_recrutados = df[df.columns[3]].count()


# RECUSADOS -> SELECIONADOS - RECRUTADOS
var_recusados = var_selecionados - var_recrutados


# SAÍDA PREMATURA -> Contar [ava_saida_data] na tabela Enrolled
var_saida_prematura = df[df.columns[4]].count()


# COMPLETARAM ESTUDO ->  Contar [ava_v03_dtvisita] na tabela Enrolled
var_completaram_estudo = df[df.columns[7]].count()


# EM ACOMPANHAMENTO -> RECRUTADOS - SAÍDA PREMATURA - COMPLETARAM O ESTUDO
var_em_acompanhamento = var_recrutados - var_saida_prematura - var_completaram_estudo

# TESTES DE HPLC ->  Contar [ava_hplc_data] na tabela Enrolled
var_testes_hplc = df[df.columns[9]].count()


### PÁGINA PRINCIPAL ###

st.header('Projeto AVANTI - RECRUTAMENTO / ACOMPANHAMENTO')
            
col1, col2, col3 = st.columns([2, 1, 4])

col1.write('**SELECIONADOS:**')
col2.info(f"{var_selecionados}")


col1, col2, col3 = st.columns([2, 1, 4])

col1.write('**RECUSADOS:**')
col2.info(f"{var_recusados}")

col1, col2, col3 = st.columns([2, 1, 4])

col1.write('**RECRUTADOS:**')
col2.info(f"{var_recrutados}")

col1, col2, col3 = st.columns([2, 1, 4])

col1.write('**SAÍDA PREMATURA:**')
col2.info(f"{var_saida_prematura}")

col1, col2, col3 = st.columns([2, 1, 4])

col1.write('**EM ACOMPANHAMENTO:**')
col2.info(f"{var_em_acompanhamento}")

col1, col2, col3 = st.columns([2, 1, 4])

col1.write('**COMPLETARAM ESTUDO:**')
col2.info(f"{var_completaram_estudo}")

    
st.markdown("---")

