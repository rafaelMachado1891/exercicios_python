# faça um programa que leia um numero e diga se ele é um numero primo

numero = int(input('digite um numero: '))

for i in range(1 , numero +1):
    if numero % i == 0:
        print('\033[34m', end=' ')
    else:
        print('\033[m', end=' ')
    print(f'{i}',end=' ')