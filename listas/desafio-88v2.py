# Faça um programa que ajude o usário a criar palpites de jogos para a megasena.
# o programa deve armazenar os resultados em uma lista composta. 

from random import randint

lista = []
listaint = []
jogos = 1
qtde = int(input('Quantos jogos você deseja gerar? '))


while jogos <= qtde:
    cont = 0 
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont+=1
        if cont >= 6:
            break
    lista.sort()
    listaint.append(lista[:])
    lista.clear()
    jogos+=1

        
print(listaint)


    


