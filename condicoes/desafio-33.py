# Faça um programa em que o usuario digite 3 numeros e mostre na tela o maior numero e o menor numero
import math

n = int(input('digite 3 numeros: '))
n2 = int(input())
n3 = int(input())

lista = [n, n2, n3]
max = max(lista)
min = min(lista)

print('dos números que vc digitou o maior é {:.2f} e o menor numero é {:.2f}'.format(max, min))


