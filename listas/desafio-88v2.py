# Faça um programa que ajude o usário a criar palpites de jogos para a megasena.
# o programa deve armazenar os resultados em uma lista composta. 

from random import randint

lista = []
temp = []
cont = 0
jogos = 0
qtde = int(input('Quantos jogos você deseja gerar? '))
print(qtde)

  
while True:
    num = randint(1,60)
    if num not in lista:
        lista.append(num)
        cont+=1
        lista.sort()
    if cont >= 6:
        break

        
print(lista)


    


