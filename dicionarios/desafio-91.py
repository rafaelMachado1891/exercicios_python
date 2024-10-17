# Crie um programa onde 4 jogadores jogam um dado. Armazene esses jogos dentro de um dicionario!
#  No final mostre os dados ordendos!

from random import randint
from operator import itemgetter
from time import sleep
dic = {}
for i in range(1,5):
    dic [f'jogador {i}'] = randint(1,6)

print('-='*30)

for i, c in dic.items():
    print(f'{i} = {c}')
    sleep(1)

print('-='*30)

ordenado = {}
ordenado = sorted(dic.items(), key=itemgetter(1), reverse=True)

for k, v in enumerate(ordenado):
    print(f'{k+1}º lugar {v[0]} com numero {v[1]}')
    sleep(1)
