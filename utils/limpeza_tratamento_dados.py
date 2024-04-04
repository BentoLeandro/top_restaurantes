import pandas as pd
import utils.funcoes_etl as etl 


#===================================================================================================
#============================ Importação, Limpeza e tratamento dos Dados ===========================
#===================================================================================================
def import_limpeza_trat_dados():
    '''Esta função é utilizada para importar, limpar e tratar o dataframe

        Tipos de limpeza:
        1. Remoção dos dados NaN
        2. Exclusão dos registros duplicados
        3. Exclusão da coluna.: switch_to_order_menu
        4. Alteração na nomenclatura das colunas
        5. Alteração nos registros da coluna.: cuisines
        6. Criação da coluna.: country_name 

        Input.: DataFrame
        Output.: DataFrame
    '''

    dados_principal = pd.read_csv('dataset\zomato.csv')
    dados = dados_principal.copy()

    #Renomear Colunas
    dados = etl.renomear_colunas(dados)

    #Deletando os registros NaN, somente a coluna Cuisines possuia esses registros.
    dados = dados[~dados.isna().any(axis=1)]

    #Deletando a Coluna.: Switch to order menu, ela possui somente o valor 0(zero) em todos os registros.
    dados.drop('switch_to_order_menu', axis=1, inplace=True)

    #Deletando os registros Duplicados.
    dados.drop_duplicates(inplace=True)

    dados["cuisines"] = dados.loc[:, "cuisines"].apply(lambda x: x.split(",")[0])

    #Resetando o indice
    dados.reset_index(drop=True, inplace=True)

    dados['country_name'] = dados['country_code'].apply(lambda x: etl.country_name(x))
    dados["color_name"] = dados.loc[:, "rating_color"].apply(lambda x: etl.color_name(x))

    return dados
#===================================================================================================
