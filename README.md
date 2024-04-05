# Top Restaurantes
Este projeto foi desenvolvido com o objetivo de adquirir mais experiência em ciência de dados, com um problema de negócio fictício da empresa Top Restaurantes. 
A base de dados utilizada é do site Kaggle.

https://www.kaggle.com/datasets/akashram/zomato-restaurants-autoupdated-dataset?resource=download&select=zomato.csv

Painel está online, hospedado no Streamlit Cloud e pode ser acessado através desse link: https://bentoleandro-toprestaurantes.streamlit.app/

# 1. Problema de negócio
A empresa Top Restaurantes é uma marketplace de restaurantes. Ou seja, seu core business é facilitar o encontro e negociações de clientes e restaurantes. Os
restaurantes fazem o cadastro dentro da plataforma da Top Restaurantes, que disponibiliza informações como endereço, tipo de culinária servida, 
se possui reservas, se faz entregas e também uma nota de avaliação dos serviços e produtos do restaurante, dentre outras informações.

O CEO precisa entender melhor o negócio para conseguir tomar as melhores decisões estratégicas e alavancar ainda mais a Top Restaurantes, e para isso, 
ele precisa que seja feita uma análise nos dados da empresa e que sejam gerados dashboards.

## Visão dos Países:
1. Quantidade de restaurantes registrados por País.
2. Quantidade de cidades registradas por País.
3. Média de Avaliações feitas por País.
4. Preço Médio do prato para duas pessoas por País.

## Visão das Cidades:
1. Top 10 Cidades com mais Restaurantes na Base de Dados.
2. Restaurantes com avaliação acima de 4.
3. Restaurantes com avaliação abaixo de 3.5.
4. Cidades com a Maior quantidade de tipos de Culinária.
   
## Visão dos tipos de Culinária:
1. Melhores Restaurantes dos Principais tipos Culinários.
2. Top 10 Restaurantes por País.
3. Top 10 Melhores Tipos de Culinárias.
4. Top 10 Piores Tipos de Culinárias

O objetivo desse projeto é criar um conjunto de gráficos e/ou tabelas
que exibam essas métricas da melhor forma possível para o CEO.


# 4. Top 3 Insights de dados
1. A sazonalidade da quantidade de pedidos é diária. Há uma variação de aproximadamente 10% do número de pedidos em dia sequenciais.
2. As cidades do tipo Semi-Urban não possuem condições baixas de trânsito.
3. As maiores variações no tempo de entrega, acontecem durante o clima ensolado.

# 7. Próximo passos
1. Reduzir o número de métricas.
2. Criar novos filtros.
3. Adicionar novas visões de negócio.
