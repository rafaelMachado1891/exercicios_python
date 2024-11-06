# Faça um programa que receba uma função chamada maior, que receba varios parametros com valores inteiros.
# seu programa tem que analisar todos os valores e dizer qual deles é o maior
from time import sleep


def analisar_lista_de_valores(l):
    if l[-1] == 999:
        tam = len(l)-1
        print(f'Você digitou {tam} valores')    
        pos=0
        for i in (l[0:-1]):
            print(f'{l[pos]}', end=' ', flush=True)
            sleep(0.5)
            pos+=1
        print()     
        maior = max(l[0:-1])
        print(f'O maior valor digitado foi {maior}')


lista=[]


valor = 0
while valor != 999:
    valor = int(input('Digite um valor [999 para encerrar]: '))
    lista.append(valor)


analisar_lista_de_valores(lista)
