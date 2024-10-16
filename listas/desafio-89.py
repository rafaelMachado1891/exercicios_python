# Crie um programa que leia o nome e duas notas de vários alunos e guarde tudo em uma lista composta
# No final, mostre um boletim contendo a média de cada um e permita que o usário possa mostrar
# as notas de cada aluno individualmente

lista = []
temp = []
notas = []

while True:
        nome =  str(input('Digite o nome do aluno: ')).upper()
        nota1 = float(input('Digite a primeira nota: '))
        nota2 = float(input('Digite a segunda nota: '))
        lista.append([nome,[nota1,nota2],(nota1 + nota2)/2]) 
        r=str(input('Deseja continua [S/N]: ')).upper().strip()[0]
        if r == 'N':
            break

print('-='*30)
print(lista)
print(f'{"Nº":<5}{"Aluno":<10}{"Media":>10}')
for i, l in enumerate(lista):
    print(f'{i:<5}',end=' ')
    print(f'{l[0]:<10}',end=' ')
    print(f'{l[2]:>8.2f} ')
    
p = int(input('Qual aluno você quer avaliar? '))
print('-='*30)

print(f'O aluno {lista[p][0]} conseguiu as notas{lista[p][1]} atingindo a media de {lista[p][2]}')