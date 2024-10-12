# Faça um programa que receba o nome e peso de varias pessoas e armazene-os em uma lista. #
# Depois disso monte uma lista com as pessoas mais pesadas e outra com as pessoas mais leves. 

temp = []
lista = []
maior = menor = 0
while True:
    temp.append(str(input('Digite um nome: ')).upper())
    temp.append(float(input('Digite o peso: ')))
    if len(lista) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            meior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    lista.append(temp[:])   # para adicionar um objeto dentro da lista usamos o fatiamento com : 
    temp.clear()            # limpa a lista temporaria para zerar os argumentos

    r=str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    if r in ('N'):
        break

print(lista)

print(f'Foram digitados {len(lista)} usuários')

print(f'O maior peso cadastrado foi de {maior} kg')

print(f'O menor peso cadastrado foi de {menor} kg')