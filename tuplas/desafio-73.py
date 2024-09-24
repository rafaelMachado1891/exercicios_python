# faça um programa com o nome dos 20 primeiros colocados do brasileirão! 
# Depois mostre apenas os 5 primeiros colocados, os ultimos 4 colocados
# uma lista com os times em ordem alfabética em que posição da tabela está a Vasco

classificacao = ('Palmeiras', 'Gremio', 'Atletico Mineiro', 'Flamengo', 'Botafogo', 'Bragantino', 'Fluminense', 'Atletico Paranaense',
                 'Internacional', 'Fortaleza', 'São Paulo', 'Cuiba', 'Corinthians', 'Cruzeiro', 'Vasco', 'Bahia', 'Santos',
                 'Goias', 'Coritiba', 'America Mineiro')

Top5 = print(f'Os top 5 times da classificação são: {classificacao[0:5]}')

ultimos_colocados = print(f'Os 4 ultimos colocados da tabela são: {classificacao[-4:]}')

order = print(sorted(classificacao)) # metodo para ordenar uma tupla

tabela = classificacao.index('Vasco') + 1 

posicao = print(f' o Time Vasco esta em {tabela}º colocado')


