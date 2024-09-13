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
    
