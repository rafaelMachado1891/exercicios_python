# Faça um programa que ajude o usário a criar palpites de jogos para a megasena.
# o programa deve armazenar os resultados em uma lista composta. 

import random
from time import sleep

lista = []
temp = []

num = int(input('Quantos jogos você deseja gerar: '))

for i in range(num):
    # for i in range(0,6):
    temp.append(random.sample(range(1,61),6))
    temp.sort()
    lista.append(temp[:])
    temp.clear() 

print(f'{lista}')  
print('-='*30)    

for i, l in enumerate(lista):
    print(l)
    sleep(2)