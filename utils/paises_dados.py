import streamlit as st
import plotly.express as px

#2.2 - Qual o nome do país que possui mais restaurantes registrados?
def gera_grafico_qtde_rest_pais(dados):
    df_aux = (dados[['country_name', 'restaurant_id']].groupby(['country_name']).
              count().sort_values('restaurant_id', ascending=False).reset_index())
    fig = px.bar(df_aux, x='country_name', y='restaurant_id', text='restaurant_id',
                 labels={'restaurant_id': 'Quantidade de Restaurantes', 
                         'country_name': 'Países'})
    
    fig.update_layout(title={'text':'Quantidade de Restaurantes Registrados por País',
                             'xanchor': 'center',
                             'x': 0.5},                             
                      title_font_size=20)
    
    st.plotly_chart(fig, use_container_width=True)


#2.1 - Qual o nome do país que possui mais cidades registradas?
def gera_grafico_qtde_cidades_pais(dados):
    df_aux = dados[['country_name','city']].groupby(['country_name']).nunique().sort_values('city', ascending=False).reset_index()    
    fig = px.bar(df_aux, x='country_name', y='city', text='city',
                 labels={'city': 'Quantidade de Cidades',
                         'country_name': 'Países'})

    fig.update_layout(title={'text': 'Quantidade de Cidades Registradas por País',
                             'xanchor': 'center',
                             'x': 0.5},
                      title_font_size=20)
    
    st.plotly_chart(fig, use_container_width=True)


#2.8 - Qual o nome do país que possui, na média, a maior quantidade de avaliações registrada?
def gera_grafico_media_aval_pais(dados):
    df_aux = (dados[['country_name','votes']].groupby(['country_name']).
              agg(Media_avaliacao=('votes', 'mean')).round(3).
              sort_values('Media_avaliacao', ascending=False).reset_index())
    
    fig = px.bar(df_aux, x='country_name', y='Media_avaliacao', text='Media_avaliacao',
                 labels={'Media_avaliacao': 'Quantidade de Avaliações',
                         'country_name': 'Países'})
        
    fig.update_layout(title={'text': 'Média de Avaliações feitas por País',
                             'xanchor': 'center',
                             'x': 0.5},
                      title_font_size=18)
        
    st.plotly_chart(fig, use_container_width=True)


#2.11 - Qual a média de preço de um prato para dois por país?
def gera_grafico_media_prato_pais(dados):
    df_aux = (dados[['country_name', 'average_cost_for_two']].groupby(['country_name']).
              agg(Media_preco_prato=('average_cost_for_two', 'mean')).round(2).
              sort_values('Media_preco_prato', ascending=False).reset_index())

    fig = px.bar(df_aux, x='country_name', y='Media_preco_prato', text='Media_preco_prato',
                 labels={'Media_preco_prato': 'Preço do Prato para duas Pessoas',
                         'country_name': 'Países'}) 
        
    fig.update_layout(title={'text': 'Preço Médio do prato para duas pessoas por País',
                             'xanchor': 'center',
                                 'x': 0.5},
                      title_font_size=18)

    st.plotly_chart(fig, use_container_width=True)  