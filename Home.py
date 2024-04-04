import streamlit as st
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static
from PIL import Image 

import utils.limpeza_tratamento_dados as etl
import utils.barra_lateral as menu
import utils.home_dados as hdt 


dados = etl.import_limpeza_trat_dados()

qtde_rest_cad = dados['restaurant_id'].nunique()
qtde_pais_cad = dados['country_code'].nunique()
qtde_cid_cad = dados['city'].nunique()
total_aval_feitas = dados['votes'].sum()
qtde_tipo_cozinha = dados['cuisines'].nunique()


st.set_page_config(page_title='Home',layout='wide')

inf_barra = menu.carrega_barra_lateral(dados, pmostra_filtro_paises=True,
                                       pmostra_filtro_restaurante=False,
                                       pmostra_filtro_culinaria=False, 
                                       pmostra_download=True)

st.header('Top Restaurantes!')
st.subheader('O Melhor lugar para encontrar seu mais novo restaurante favorito!')

st.markdown('___')
st.markdown('#### Temos as seguintes informações dentro da nossa plataforma:')

col1, col2, col3, col4, col5 = st.columns(5, gap='large')

#1.1 - Quantos restaurantes únicos estão registrados?
with col1:
    col1.metric('Restaurantes Cadastrados', value=qtde_rest_cad)

#1.2 - Quantos países únicos estão registrados?
with col2:
    col2.metric('Países Cadastrados', value=qtde_pais_cad)

#1.3 - Quantas cidades únicas estão registradas?
with col3:
    col3.metric('Cidades Cadastradas', value=qtde_cid_cad)

#1.4 - Qual o total de avaliações feitas?
with col4:
    col4.metric('Avaliações na Plataforma', value=total_aval_feitas)

#1.5 - Qual o total de tipos de culinária registrados?
with col5:
    col5.metric('Culinárias Oferecidas', value=qtde_tipo_cozinha)
st.markdown('___')

#1.6 - Mapa
with st.container():
    hdt.gera_grafico_mapa(inf_barra.dados)   
