import streamlit as st
import pandas as pd
import plotly.express as px

import utils.barra_lateral as menu
import Home as home
import utils.paises_dados as pdt 

st.set_page_config(page_title='Visão Países', layout='wide')

inf_barra = menu.carrega_barra_lateral(home.dados, pmostra_filtro_paises=True,
                                       pmostra_filtro_restaurante=False, 
                                       pmostra_filtro_culinaria=False,
                                       pmostra_download=False)

dados = inf_barra.dados


st.header('🌎 Visão Países')
st.markdown('___')

#2.2 - Qual o nome do país que possui mais restaurantes registrados?
with st.container():
    pdt.gera_grafico_qtde_rest_pais(dados)   
st.markdown('___')    

#2.1 - Qual o nome do país que possui mais cidades registradas?
with st.container():  
    pdt.gera_grafico_qtde_cidades_pais(dados)  
st.markdown('___')    

with st.container():
    col1, col2 = st.columns(2, gap='large')

    #2.8 - Qual o nome do país que possui, na média, a maior quantidade de avaliações registrada?
    with col1:
        pdt.gera_grafico_media_aval_pais(dados)       

    #2.11 - Qual a média de preço de um prato para dois por país?
    with col2:
        pdt.gera_grafico_media_prato_pais(dados)
        



