# faça um programa que leia um numero de 1 a 9999 e mostre na tela cada um dos digitos separados
num = int(input('digite um numero entre 1 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(' unidade: {}\n dezena: {}\n centena: {}\n milhar: {}'.format(u,d,c,m))