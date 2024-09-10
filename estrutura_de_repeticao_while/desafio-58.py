#crie um programa que pense em um numero de 0 a 10, receba um numero do usuário e retorne ao usuário se ele acertou o numero escolhido. 

import random

numero = 0
contagem = 0 
v = random.randint(0,10)
print(v)
escolha = int(input('digite um  numero 0 a 10: '))
while escolha != v:
    escolha = int(input('ops! você errou tente novamente: '))
    contagem +=1 

print(f'você acertou! o numero em que pensei foi exatamente o {v}, o número de tentativas foi {contagem}')
