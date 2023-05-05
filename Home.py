import streamlit as st
from PIL import Image

st.set_page_config(
    page_title='Nubimed - Projeto Avanti ',
    page_icon='chart_with_upwards_trend',
    layout='wide',
    initial_sidebar_state='expanded',
    
)

#image_path = 'logo.png'
#image = Image.open( 'logo.png' )
#st.sidebar.image( image, width=120 )

with st.sidebar:
    
    st.sidebar.markdown( '#### Início do estudo: 29/NOV/2021' )
    st.sidebar.markdown( '#### Tempo do estudo: 339 dias' )
    st.sidebar.markdown( '#### N. de Atendimentos última semana: 9' )
    
    st.sidebar.markdown( """___""" )

st.write( '## Projeto AVANTI' )

st.markdown(
    """
    Dashboard construído para acompanhar o recrutamento e seleção de Pacientes participantes do Projeto AVANTI.
    - Coordenador do Projeto:
        Prof. Dr. Aldo Ângelo Moreira Lima [alima@ufc.br]
        
    ## Como utilizar esse AVANTI Dashboard?
    
    - Resumo:
        - Acompanhamento dos selecionados, recusados, recrutados, saída prematura, em acompanhamento e pacientes que completaram o estudo.
    - Resultados RT_PCR:
        - Resultados semanais de RT_PCR.
    - Visão Geográfica:
        - Resultados semanais de pacientes selecionados mostrando sua localização em Fortaleza/Ceará.
        
    ### Suporte Técnico
    - Time de Data Science na Nubimed
        - suporte_ssgd@nubimed.ufc.br
    """ )




