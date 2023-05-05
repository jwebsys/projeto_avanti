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
st.write( '## Experimentação clínica, controle, duplo-cego, aleatório com Nacetilcisteína e bromexina para COVID-19' )

st.markdown(
    """Vários agentes terapêuticos têm sido avaliados para o tratamento da COVID-19, mas somente um, o fármaco antiviral denominado remdesivir administrado por via endovenosa, mostrou eficácia em abreviar o tempo de duração da doença em 26,7% nos pacientes gravemente enfermos. Esta proposta tem como objetivo primário (1) determinar o efeito da N-acetilcisteína (NAC; substância redutora e ação complementar interceptora viral) e combinação da NAC + bromexina (BMX; inibidor de protease viral), na duração clínica da COVID-19 avaliado no 7o. dia de acompanhamento ambulatorial, observando o escore dos sinais e sintomas clínicos da doença. O estudo tem como objetivos secundários: (2) avaliar a mudança na carga viral por RT-qPCR do SARS-CoV-2 entre o 1o., 7o., e 14o. dias do protocolo experimental; (3) determinar a ação da NAC e BMX + NAC na resposta imune utilizando o teste rápido de ELISA (IgM / IgG) que será realizado no 14o. Dia do acompanhamento do protocolo experimental; e (4) Avaliar o efeito da NAC e BMX + NAC na mudança no nível sérico de biomarcadores de inflamação e substâncias redutoras (IL-6, MCP-3, D-dímero, IL1-RA, IL-10, GCSF, TNF-α, MCP-1, IL-2R, MIP-1 alpha, IP-10, IL-8, NT-proBNP, Troponina I, PCR e procalcitonina; glutationa peroxidase-GPx; superóxido dismutase-SOD e catalase-CAT) dos pacientes coletados no 1o. e 14 o. dias do estudo. O estudo será de ensaio clínico prospectivo, duplo-cego, placebo controle e aleatório de um total de 219 pacientes, 73 por cada grupo de tratamento, com doença leve a moderada, igual ou acima de 18 anos de idade, com sinais e sintomas clínicos da COVID-19 e certificados pelo teste de RT-qPCR para detecção da carga viral do SARS-CoV-2. O estudo será realizado utilizando a Rede de Vigilância, Atendimento e Pesquisa - REVAP-C19, NUBIMED, FAMED, UFC, Fortaleza, CE no sentido de facilitar a eficiência de entrada dos pacientes no estudo. Os grupos aleatórios de tratamentos serão: (1) Placebo controle (Vitamina C ? 500 mg / dia, durante 10 dias); (3) N-acetilcisteína (NAC; 1800 mg / dia, durante 10 dias); e (4) NAC (1800 mg / dia, durante 10 dias) + Cloridrato de Bromexina (BMX; 32 mg / dia, durante 10 dias). O estudo tem a perspectiva de avaliar a eficácia da NAC isolado ou combinado com BMX na duração do escore clínico dos casos leve a moderado da COVID-19. O estudo também irá avaliar parâmetros secundários como o efeito dos fármacos na mudança da carga viral, resposta imune, e na mudança da reação inflamatória e de substâncias redutoras no plasma dos pacientes do estudo. Neste sentido, o ensaio projeta minimizar a evolução da doença para casos graves, aliviando assim o colapso do sistema de saúde e minimizando os transtornos sociais, econômicos e sanitários da pandemia pelo SARS-CoV-2.
    
    - Coordenador do Projeto:
        Prof. Dr. Aldo Ângelo Moreira Lima [alima@ufc.br]
            
    
    """ )




