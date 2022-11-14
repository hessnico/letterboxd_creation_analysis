# Letterboxd data creation and extraction 

## Ideia norteadora	
Em sintexe, a ideia do projeto é automatizar a extração, limpeza e exploração de dados de filmes assistidos.
O projeto consiste na extração de dados utilizando a API do TMDB a partir de filmes cadastrados na rede social Letterboxd, na criação automática de hashmaps com dados dos datasets gratuitos disponibilizados pelo IMDb e ,por fim, na limpeza dos dados utilizando, majoritamente, a biblioteca Pandas do Python.
Para rodar o programa completo rode o script index.py

## Outputs
Durante o programa é gerado várias tabelas, entre elas tabela com id's não encontrados, hashmaps com nomes dos diretores e escritores para facilitar na análise descritiva dos dados, e por fim, a tabela final, limpa e pronta para ser utilizada em análises, tanto, inferencias quanto descritivas.
A tabela final gerada está dentro da pasta "./data/clean/clean_watched.csv".

## Algumas conclusões
A ideia inicial de automatizar a extração de dados foi concluída por completo, como também, a limpeza dos dados.
Por fim, no final do projeto tomei a liberdade para tentar analisar e encontrar padrões nas notas que atribuo, processei o dados e utilizei o algoritmo de regressão RandomForestRegressor, e assim, no final do teste consegui uma pontuação acima de 50% com um R squared baixo, contudo, positivo, algo que não esperava durante a criação da aplicação. 
