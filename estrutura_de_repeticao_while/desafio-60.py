<<<<<<< HEAD
# faça um programa que leia um numero e mostre na tela o seu fatorial

numero = int(input('digite um numero: '))

fator = 0

while numero > 0:
    fator = numero - 1
    numero * fator
print(fator)
=======
# faca um programa que leia um numero e mostre o seu fatorial 

numero = int(input('Digite um numero para retornar o seu factorial: '))
variavel = numero
fator = 1 

while variavel > 0:
    print(f'{variavel}',end='')
    print(' x ' if variavel > 1 else ' = ', end='') 
    fator *= variavel
    variavel -= 1    
    
print(f'o factorial de {numero} é {fator}')
    
>>>>>>> 70338f7df9251fd2b133a83c63be15041afd9af7
