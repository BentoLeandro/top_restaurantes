import pandas as pd
import streamlit as st
import plotly.express as px

#5.16 - Melhores Restaurantes dos Principais tipos Culinários
def retorna_inf_culinaria(dados, pculinarias):    
    colunas = ['restaurant_id', 'restaurant_name','country_name','city','cuisines','average_cost_for_two','currency','aggregate_rating','votes']
    
    inf_comida = {}
    for culinaria in pculinarias:
        indice_culinaria = dados['cuisines'] == culinaria
        if dados[indice_culinaria]['restaurant_id'].count() > 0:
            inf_comida[culinaria] = (dados.loc[indice_culinaria, colunas].
                                     sort_values(["aggregate_rating", "restaurant_id"], 
                                                 ascending=[False, True]).
                                     iloc[0, :].to_dict())
    
    return inf_comida

def gera_coluna_tipo_culinaria(col, inf, pdesc_culinaria, pculinaria):
    if pculinaria in inf.keys():
        col.metric(label=f"{pdesc_culinaria}: {inf[pculinaria]['restaurant_name']}",
                   value=f"{inf[pculinaria]['aggregate_rating']}/5.0",
                   help=f"""
                         País.: {inf[pculinaria]['country_name']}\n
                         Cidade.: {inf[pculinaria]['city']}\n
                         Restaurante.: {inf[pculinaria]['restaurant_name']}\n
                         Média Prato para dois.: {inf[pculinaria]['average_cost_for_two']} ({inf[pculinaria]['currency']})
                        """)
    else:
        col.metric(label=f"{pdesc_culinaria}: Nenhum Restaurante encontrado!",
                   value="Não Encontrado!")    

#5.15 - Top Restaurantes
def gera_dataframe_top_restaurantes(dados, pqtde_rest):
    colunas = ['restaurant_id', 'restaurant_name','country_name','city','cuisines',
               'average_cost_for_two','currency','aggregate_rating','votes']
    paises = dados['country_name'].unique()

    lista_restaurantes = []
    for pais in paises:
        indice_pais = dados['country_name'] == pais
        df_aux = (dados.loc[indice_pais, colunas].
                  sort_values(["aggregate_rating", "restaurant_id"], 
                              ascending=[False, True]).head(pqtde_rest))
        
        lista = list(df_aux['restaurant_id'].index.values)
        lista_restaurantes.extend(lista)

    df_aux = (dados.loc[lista_restaurantes, colunas].
              sort_values(["country_name", "aggregate_rating", "restaurant_id"], 
                          ascending=[True, False, True]))
    
    df_aux.columns = ['ID Restaurante', 'Nome Restaurante',' País','Cidade','Culinária',
                      'Custo Médio para dois','Moeda','Classificação','Votos']
    
    st.markdown(f'### Top {pqtde_rest} Restaurantes por País')    
    st.dataframe(df_aux, use_container_width=True)

#5.12 - Top 10 Melhores Tipos de Culinárias
def gera_grafico_tops_culinarias(dados):
    df_aux = (dados[['cuisines', 'aggregate_rating']].groupby(['cuisines']).
              agg(Media_nota=('aggregate_rating', 'mean')).
              round(2).sort_values('Media_nota', ascending=False).reset_index())
    df_aux = df_aux.head(10)

    fig = px.bar(df_aux, x='cuisines', y='Media_nota', text='Media_nota',
                 labels={'cuisines': 'Tipo de Culinária',
                         'Media_nota': 'Média de Avaliações'})

    fig.update_layout(title={'text': 'Top 10 Melhores Tipos de Culinárias',
                             'xanchor': 'center',
                             'x': 0.5},
                      title_font_size=20)

    st.plotly_chart(fig, use_container_width=True)

#5.14 - Top 10 Piores Tipos de Culinárias
def gera_grafico_piores_culinarias(dados):
    indice_culinaria = dados['aggregate_rating'] > 0
    df_aux = (dados[indice_culinaria][['cuisines', 'aggregate_rating']].groupby(['cuisines']).
              agg(Media_nota=('aggregate_rating', 'mean')).
              round(2).sort_values('Media_nota', ascending=True).reset_index())
    df_aux = df_aux.head(10)

    fig = px.bar(df_aux, x='cuisines', y='Media_nota', text='Media_nota',
                 labels={'cuisines': 'Tipo de Culinária',
                         'Media_nota': 'Média de Avaliações'})

    fig.update_layout(title={'text': 'Top 10 Piores Tipos de Culinárias',
                             'xanchor': 'center',
                             'x': 0.5},
                      title_font_size=20) 

    st.plotly_chart(fig, use_container_width=True)   