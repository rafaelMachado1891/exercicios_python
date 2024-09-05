# faça um programa que leia 6 numero inteiros e realize a soma somente dos numeros pares! 

soma = 0
count = 0

for i in range(1,7):
    numero = int(input(f'Digite o {i} valor: '))
    if numero % 2 ==0:
        soma += numero # soma dos elementos
        count += 1 # contador 
print(f'você informou {count} numeros pares e a soma desses numeros é {soma}')

