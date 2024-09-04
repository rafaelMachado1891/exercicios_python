# faça um programa que calcule a tabuada de um número que o usuário digitar
from time import sleep

numero = int(input('Digite um numero qualquer: '))

for i in range(1, 11):
    num = numero * i
    print(f'{numero} X {i} = {num}')
    sleep(1)