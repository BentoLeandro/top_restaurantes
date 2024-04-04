import streamlit as st
import Home as home
import utils.barra_lateral as menu
import utils.culinaria_dados as cdt

st.set_page_config(page_title='Visão Culinária', layout='wide')

inf_barra = menu.carrega_barra_lateral(home.dados, pmostra_filtro_paises=True,
                                       pmostra_filtro_restaurante=True,
                                       pmostra_filtro_culinaria=True,
                                       pmostra_download=False)

dados = inf_barra.dados

st.header('🍽️ Visão Tipos de Culinária')
st.markdown('___')

with st.container():
    st.markdown('### Melhores Restaurantes dos Principais tipos Culinários')
    col1, col2, col3, col4, col5 = st.columns(5, gap='large')

    #5.16 - Melhores Restaurantes dos Principais tipos Culinários
    culinarias = ['Italian','American','Arabian','Japanese','Brazilian']     
    inf = cdt.retorna_inf_culinaria(dados, pculinarias=culinarias)  

    #Culinária Italiana            
    with col1: 
        cdt.gera_coluna_tipo_culinaria(col1, inf, 'Italiana', 'Italian')       
    
    #Culinária Americana
    with col2:       
        cdt.gera_coluna_tipo_culinaria(col2, inf, 'Americana', 'American')
        
    #Culinária Árabe
    with col3:
        cdt.gera_coluna_tipo_culinaria(col3, inf, 'Árabe', 'Arabian')

    #Culinária Japonesa
    with col4:
        cdt.gera_coluna_tipo_culinaria(col4, inf, 'Japonesa', 'Japanese')

    #Culinária Brasileira
    with col5:
        cdt.gera_coluna_tipo_culinaria(col5, inf, 'Brasileira', 'Brazilian')

st.markdown('___')
#5.15 - Top Restaurantes
with st.container():
    qtde_restaurantes = 10
    if 'qtde_rest' in st.session_state:
        qtde_restaurantes = st.session_state['qtde_rest']
    cdt.gera_dataframe_top_restaurantes(dados, pqtde_rest=qtde_restaurantes)

st.markdown('___')
with st.container():
    col1, col2 = st.columns(2, gap='large')

    #5.12 - Top 10 Melhores Tipos de Culinárias
    with col1:
        cdt.gera_grafico_tops_culinarias(dados)           

    #5.14 - Top 10 Piores Tipos de Culinárias
    with col2:
        cdt.gera_grafico_piores_culinarias(dados)            

             


   





