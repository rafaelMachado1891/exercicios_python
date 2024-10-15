# Crie um programa que leia o nome e duas notas de vários alunos e guarde tudo em uma lista composta
# No final, mostre um boletim contendo a média de cada um e permita que o usário possa mostrar
# as notas de cada aluno individualmente

lista = []
temp = []
notas = []

r= 'S'
while True:
    if r == 'S':
        nome =  temp.append(str(input('Digite o nome do aluno: ')))
        nota1 = notas.append(float(input('Digite a primeira nota: ')))
        nota2 = notas.append(float(input('Digite a segunda nota: ')))
        temp.append(notas[:])
        notas.clear()
        lista.append(temp[:])  
        temp.clear()
        r=str(input('Deseja continua [S/N]: ')).upper().strip()[0]
    else:
        break

print(lista)

for i, l in enumerate(lista):
    print(f'{i}',end=' ')
    print(l[0])
    for a, b in enumerate(lista[1][1]):
        print(b)
        
     #   print(l)
#for i, l in enumerate(lista):
#   soma = (l[1] + l[2]) / 2
#   print(f'O aluno {l[0]} atingiu a média {soma}')

