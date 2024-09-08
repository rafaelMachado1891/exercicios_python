# faça um programa que leia o peso de cinco pessoas e mostre qual foi o menor peso

lista = []

for i in range(1,6):
    peso = float(input(f'Digite o peso da {i}º pessoa: '))
    lista.append(peso)

contagem = len(lista)
resultado = min(lista)
maior = max(lista)
print(f'dos {contagem} pesos recebidos o menor é {resultado} e o maior é {maior}')  