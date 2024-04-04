import streamlit as st
import plotly.express as px

#3.1 - Qual o nome da cidade que possui mais restaurantes registrados?
def gera_grafico_top_cidades(dados):
    df_aux = (dados[['country_name','city','restaurant_id']]
              .groupby(['country_name','city']).
              agg(Qtde_restaurantes=('restaurant_id', 'count')).
              sort_values('Qtde_restaurantes', ascending=False).reset_index())
    df_aux = df_aux.loc[0:9, :]

    fig = px.bar(df_aux, x='city', y='Qtde_restaurantes', color='country_name', text='Qtde_restaurantes',
                 labels={'city': 'Cidades',
                         'Qtde_restaurantes': 'Quantidade de Restaurantes',
                         'country_name': 'País'})
    
    fig.update_layout(title={'text': 'Top 10 Cidades com mais Restaurantes na Base de Dados',
                             'xanchor': 'center',
                             'x': 0.5},
                      title_font_size=20)

    st.plotly_chart(fig, use_container_width=True)

#3.2 - Qual o nome da cidade que possui mais restaurantes com nota média acima de 4?
def gera_grafico_cidades_rest_aval_maior(dados):
    df_aux = (dados[['country_name', 'city', 'aggregate_rating']].
              groupby(['country_name','city']).agg(Media_nota=('aggregate_rating', 'mean')).
              round(2).sort_values('Media_nota', ascending=False).reset_index())

    df_aux = df_aux[df_aux['Media_nota'] >= 4]
    df_aux = df_aux.loc[0:6, :]

    fig = px.bar(df_aux, x='city', y='Media_nota', color='country_name', text='Media_nota',
                 labels={'city': 'Cidades',
                         'Media_nota': 'Média dos Restaurantes',
                         'country_name': 'País'})
    
    fig.update_layout(title={'text': 'Restaurantes com avaliação acima de 4',
                             'xanchor': 'center',
                             'x': 0.5},
                      title_font_size=20)
    
    st.plotly_chart(fig, use_container_width=True)

#3.3 - Qual o nome da cidade que possui mais restaurantes com nota média abaixo de 3.5?
def gera_grafico_cidades_rest_aval_menor(dados):
    df_aux = (dados[['country_name','city','aggregate_rating']].
              groupby(['country_name','city']).agg(Media_nota=('aggregate_rating', 'mean')).
              round(2).sort_values('Media_nota').reset_index())
    df_aux = df_aux[df_aux['Media_nota'] <= 3.5]

    fig = px.bar(df_aux, x='city', y='Media_nota', color='country_name', text='Media_nota',
                 labels={'city': 'Cidades',
                         'Media_nota': 'Média de Notas dos Restaurantes',
                         'country_name': 'País'})

    fig.update_layout(title={'text': 'Restaurantes com avaliação abaixo de 3.5',
                             'xanchor': 'center',
                             'x': 0.5},
                      title_font_size=20)  

    st.plotly_chart(fig, use_container_width=True)

#3.5 - Qual o nome da cidade que possui a maior quantidade de tipos de culinária distintas?
def gera_grafico_cidades_qtde_culinaria(dados):
    df_aux = (dados[['country_name','city','cuisines']].
              groupby(['country_name','city']).
              agg(Qtde_culinaria=('cuisines', 'nunique')).
              sort_values('Qtde_culinaria', ascending=False).reset_index())
    df_aux = df_aux.loc[0:9, :]

    fig = px.bar(df_aux, x='city', y='Qtde_culinaria', color='country_name', text='Qtde_culinaria',
                 labels={'city': 'Cidades',
                         'Qtde_culinaria': 'Quantidade de Culinárias',
                         'country_name': 'País'})
    
    fig.update_layout(title={'text': 'Cidades com a Maior quantidade de tipos de Culinária',
                             'xanchor': 'center',
                             'x': 0.5},
                      title_font_size=20)
    
    st.plotly_chart(fig, use_container_width=True)