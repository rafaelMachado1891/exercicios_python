#crie um programa que pense em um numero de 0 a 5, receba um numero do usuário e retorne ao usuário se ele acertou o numero escolhido. 

import random

v = random.randint(0,5)
escolha = int(input('digite um  numero 0 a 5: '))

if escolha == v:
    print('você acertou! o numero em que pensei foi exatamente o {}'.format(v))
else: 
    print('você está errado, o número em que pensei foi {}'.format(v))



