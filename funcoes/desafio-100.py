# Faça uma programa que contenha uma lista chamada numeros e duas funções chamada sorteia e soma par
# a primeira função vai sortear 5 valores e coloca-los na lista e a segunda vai somar apenas os valores pares! 

from random import randint
from time import sleep

def somar_valores_pares(lista):
    valor = 0
    for i, v in enumerate(lista):
        if v % 2 ==0:
            valor+=v
    print()
    print('-='*20)     
    print(f'A soma dos valores pares é {valor}')


def sortear_valores_lista(lista):
    for i in range(0,6):
        n=randint(1, 60)
        lista.append(n)
        t=len(lista)
    print(f'Sorteando {t} valores....',end=' ',flush=True)
    sleep(0.5)
    for i in (lista):
        print(f'{i}', end=' ',flush=True)
        sleep(0.5)


lista = []

sortear_valores_lista(lista)
somar_valores_pares(lista)

