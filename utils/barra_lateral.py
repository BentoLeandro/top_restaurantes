import streamlit as st
from PIL import Image
from st_pages import Page, show_pages, add_page_title, Section, add_indentation

class Menu:
    def __init__(self):
        self.filtro_paises = None
        self.dados = None

def mostra_filtro_pais_sessao():
    st.write(st.session_state['filtro_paises'])        

#===================================================================================================
#========================================== Barra Lateral ==========================================
#===================================================================================================

def carrega_barra_lateral(dados, pmostra_filtro_paises, pmostra_filtro_restaurante,
                          pmostra_filtro_culinaria, pmostra_download):
    menu = Menu()
    image_path = "logo_restaurante.png"
    image = Image.open(image_path)
    #st.sidebar.image(image, width=200)

    col1, col2 = st.sidebar.columns([1, 3], gap="small")
    col1.image(image, width=70)
    col2.markdown("# Top Restaurantes")    
    st.sidebar.markdown('___')

    st.sidebar.page_link("Home.py", label="Home", icon="🏠")
    st.sidebar.page_link("pages/visao_paises.py", label="Visão Países", icon="🌎")
    st.sidebar.page_link("pages/visao_cidades.py", label="Visão Cidades", icon="🏙️")
    st.sidebar.page_link('pages/visao_culinaria.py', label="Visão Culinária", icon="🍽️")
    st.sidebar.markdown('___')
   
    st.sidebar.markdown('### Filtros')

    filtro_paises = []
    if pmostra_filtro_paises:
        default_paises = ['Brazil', 'Canada', 'Australia', 'Indonesia']
        default_sel_todos_paises = False
                   
        if 'filtro_paises' in st.session_state:
            if st.session_state['filtro_paises'] != None:
                default_paises = st.session_state['filtro_paises'] 

        if 'sel_todos_paises' in st.session_state:            
            if st.session_state['sel_todos_paises']:
                default_sel_todos_paises = st.session_state['sel_todos_paises']
                default_paises = dados['country_name'].unique()        

        filtro_paises = st.sidebar.multiselect(
            'Escolha os paises que deseja visualizar os Restaurantes:',
            dados['country_name'].unique(),
            default=default_paises,
            key='filtro_paises'
        )

        if len(filtro_paises) == dados['country_name'].nunique():
            default_sel_todos_paises = True
            desab_checkbox = True
        else:
            default_sel_todos_paises = False
            desab_checkbox = False            
        st.sidebar.checkbox('Todos os Países', value=default_sel_todos_paises, 
                                             disabled=desab_checkbox, key='sel_todos_paises')
        
    if pmostra_filtro_restaurante:
        qtde_rest = st.sidebar.slider('Selecione a quantidade de Restaurantes que deseja visualizar:',
                                      min_value=1, max_value=20, value=10, key='qtde_rest')

    filtro_culinaria = []
    if pmostra_filtro_culinaria:
        default_culinaria = ['Italian','American','Arabian','Japanese','Brazilian']
        if 'filtro_culinaria' in st.session_state:
            default_culinaria = st.session_state['filtro_culinaria']        

        filtro_culinaria = st.sidebar.multiselect(
            'Escolha os Tipos de Culinária:',
             sorted(list(dados['cuisines'].unique())),
             default=default_culinaria,
             key='filtro_culinaria'   
        )    
        
    #somente da pagina principal
    if pmostra_download:
        st.sidebar.markdown('### Dados Tratados')
        st.sidebar.markdown('###### Add Botão para download')

    
    if pmostra_filtro_paises:
        indices_selecionados = dados['country_name'].isin(filtro_paises)                                
        dados = dados.loc[indices_selecionados, :]

    if pmostra_filtro_culinaria:
        indices_selecionados = dados['cuisines'].isin(filtro_culinaria)
        dados = dados.loc[indices_selecionados, :]
    
    menu.dados = dados
    menu.filtro_paises = filtro_paises
    #st.session_state['filtro_paises'] = filtro_paises             

    return menu    

#===================================================================================================    