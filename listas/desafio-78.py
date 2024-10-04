# Faça um programa que leia  5 valores e armazene em uma lista. No final mostre qual foi o maior valor digitado 
# e o menor valor e as suas respectivas posições

lista = []

for i in range(0,5):
    lista.append(int(input('Digite um valor: ')))

maior = max(lista)
menor = min(lista)

posicao_maior = [i for i, v in enumerate(lista) if v == maior] 

posicao_menor = [i for i, v in enumerate(lista) if v == menor]


print(f'{lista}')
print(f'O maior valor digitado foi {maior} e está na posição {posicao_maior}')
print(f'O menor valor digitado foi {menor} e está na posição {posicao_menor}')



