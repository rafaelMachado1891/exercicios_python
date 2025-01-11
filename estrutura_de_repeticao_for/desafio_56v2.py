# faça um programa que leia 6 numero inteiros e realize a soma somente dos numeros pares! 

from random import randint

lista = []
par = 0

for i in range(1,7):
    a = randint(1,60)
    lista.append(a)
    if a % 2 == 0:
        par+=a
    

print(f' os numeros gerados foram {lista}')
print(f' a soma dos números pares da lista é {par}')