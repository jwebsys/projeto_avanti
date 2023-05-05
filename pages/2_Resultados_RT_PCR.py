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

#RESULTADOS -> T1, T2, T3 
var_auxt1 = df[(df.grupo == 'T1')]
var_auxt1 = var_auxt1['grupo'].count()

var_auxt2 = df[(df.grupo == 'T2')]
var_auxt2 = var_auxt2['grupo'].count()

var_auxt3 = df[(df.grupo == 'T3')]
var_auxt3 = var_auxt3['grupo'].count()


# SAÍDA PREMATURA RT-PCR -> SAIDA PREMATURA / RECRUTADOS
var_saida_prematura_rt_pcr = round((var_saida_prematura / var_recrutados) * 100, 2)


# Resultados RT-PCR Lacen 

var_pcr_resultado_all = df['ava_pcr_resultado']
var_pcr_resultado_all = var_pcr_resultado_all.count()

var_pcr_resultado = df[(df.ava_pcr_resultado == 1)]
var_pcr_resultado = var_pcr_resultado['ava_pcr_resultado'].count()

var_pcr_percentual = (var_pcr_resultado / var_pcr_resultado_all) * 100


### PÁGINA PRINCIPAL ###

col1, col2, col3 = st.columns([1.2, .5, .5])

with col1:
    
    st.write('**Projeto AVANTI - RESULTADOS RT-PCR LACEN (N/+)**')
   
    
with col2:
    st.info(f"{var_pcr_resultado_all} / {var_pcr_resultado}")

with col3:
    st.info(f"{round(var_pcr_percentual,2)}" + "%") 
        
st.markdown("---")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.write('**GRUPO TRATAMENTO 1:**')
    st.info(f"{var_auxt1}")

with col2:
    st.write('**GRUPO TRATAMENTO 2:**')
    st.info(f"{var_auxt2}")

with col3:
    st.write('**GRUPO TRATAMENTO 3:**')
    st.info(f"{var_auxt3}")


st.markdown("---")

