# faça um programa que receba o cateto oposto de um triangulo, o cateto adjacente e retorno o valor da hipotenusa
import math

co = float(input('digite o valor do cateto oposto: '))
ca = float(input('digite o valor do cateto adjascente: '))
resultado = math.hypot(co, ca)
print('o valor da hipotenusa para os catetos{} e {} é {:.2f}'.format(co,ca,resultado))