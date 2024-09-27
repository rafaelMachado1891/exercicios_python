import random

# crie um programa que gere 6 numeros aleatórios e armazene esses numero em um tupla
tupla = ()

for i in range(1,7):
    ale = random.randint(1,100)
    tupla += (ale,)
print(tupla)

maior = max(tupla)
 
print(f'O maior valor gerado foi {maior}')

menor = min(tupla)

print(f'O menor valor gerado foi {menor}')

