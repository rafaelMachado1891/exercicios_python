#faça um programa que leia varios numeros! ao final calcule a média, o menor e o maior valor dos numeros digitados

import math

# n = int(input('digite um numero: '))
n = 0 
c = 0
soma = 0
media = 0
maior = 0
menor = 0

# media = n/c

resposta = 'S'

while resposta != 'N':
    n = int(input('digite um numero: '))
    c += 1
    soma+= n 
    if c ==1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resposta = str(input('você deseja digitar mais numeros? [S/N]: ')).upper().strip()[0]
media = soma / c 
print(f'você digitou {c} numeros, a soma desses numeros é {soma} e a média é {media} o maior é {maior} e o menor é {menor}')






       