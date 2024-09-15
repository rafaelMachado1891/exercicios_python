# escreva um programa que leia o primeiro termo e crie uma PA. No final mostre os 10 primeiros termos dessa progressao

numero = int(input('digite o primeiro termo: '))
razao = int(input('razao: '))
termo = numero
decimo = 1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while decimo <= total:
        print(f'{termo} ->', end=' ')
        termo += razao
        decimo +=1    
    print('Pausa')
    mais = int(input('quanto termos você deseja adicionar a mais?' ))
print('progresso')