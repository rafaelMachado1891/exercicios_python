# Crie um modulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro(), metade(). 
# Faça também um programa que importe esse modulo e utilize algumas dessas funções 

import moeda
from time import sleep

num = int(input('Digite um numero: '))
sleep(0.5)
print(f'O dobro de {num} é {moeda.dobro(num)}')
sleep(0.5)
print(f'A metade de {num} é {moeda.metade(num)}')
sleep(0.5)
print(f'Com o acréscimo informado temos, {moeda.aumentar(num)}')
sleep(0.5)
print(f'Com a redução informada temos,  {moeda.diminuir(num)}')
 