# Faça um programa que crie uma matriz de 3X3 com os valores digitados. 

lista = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(0,3):
    for c in range(0,3):
        lista [i][c] = int(input(f'Digite um valor para [{i}]:[{c}]: '))
print('-='*30)
for i in range(0,3):
    for c in range(0,3):
     print(f'[{lista[i][c]:^5}]',end=' ')
    print()