# escreva um programa que leia o primeiro termo e crie uma PA. No final mostre os 10 primeiros termos dessa progressao

numero = int(input('digite o primeiro termo: '))
razao = int(input('razao: '))
termo = numero
decimo = 1
while decimo <= 10:
    print(f'{termo} ->', end=' ')
    termo += razao
    decimo +=1    
print('fim')