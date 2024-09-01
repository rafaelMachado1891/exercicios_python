# Crie um programa que leia um numero na tela e diga se ele é impar ou par
n = int(input('Digite um número: '))
r = n % 2 
if r == 0:
    print('O numero é par')
else:
    print('O numero é impar')