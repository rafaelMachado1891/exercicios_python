# faça um programa que leia um numero qualquer e mostre sua porcao inteira

import math

n = float(input('digite um numero: '))
resultado = math.floor(n)
print('a porcao inteira do numero {} equivale a {}'.format(n, resultado))