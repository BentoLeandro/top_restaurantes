import streamlit as st
import plotly.express as px

import utils.barra_lateral as menu
import Home as home
import utils.cidades_dados as cdt

st.set_page_config(page_title='Visão Cidades', layout='wide')

inf_barra = menu.carrega_barra_lateral(home.dados, pmostra_filtro_paises=True, 
                                       pmostra_filtro_restaurante=False,
                                       pmostra_filtro_culinaria=False,
                                       pmostra_download=False)

dados = inf_barra.dados

st.header('🏙️ Visão Cidades')
st.markdown('___')

#3.1 - Qual o nome da cidade que possui mais restaurantes registrados?
with st.container():
    cdt.gera_grafico_top_cidades(dados)


st.markdown('___')
st.subheader('Top Cidades')
with st.container():
    col1, col2 = st.columns(2, gap='large')

    #3.2 - Qual o nome da cidade que possui mais restaurantes com nota média acima de 4?
    with col1:
        cdt.gera_grafico_cidades_rest_aval_maior(dados)

    #3.3 - Qual o nome da cidade que possui mais restaurantes com nota média abaixo de 3.5?
    with col2:
        cdt.gera_grafico_cidades_rest_aval_menor(dados)

#3.5 - Qual o nome da cidade que possui a maior quantidade de tipos de culinária distintas?
with st.container():
    cdt.gera_grafico_cidades_qtde_culinaria(dados)
    
    

