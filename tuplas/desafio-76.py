# Crie um programa que tenha uma unica tupla com os produtos e seus respectivos preços. 
# No Final mostre uma listagem de preços organizadas em formato tabular

produtos = ('Pão', 2.99, 'Frango', 19.90, 'Café', 14.90, 'Leite', 3.95)
print('-'*40)
print(f'{'Listagem de Preços':^40}')
print('-'*40)

for i in range(0 , len(produtos)):
    if i % 2 == 0:
        print(f'{produtos[i]:.<30}', end='')
    else:
        print(f'R${produtos[i]:>7.2f}')
print('-'*40)