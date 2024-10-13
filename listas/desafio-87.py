# Faça um programa que crie uma matriz de 3X3 com os valores digitados. 

lista = [[0,0,0],[0,0,0],[0,0,0]]
soma = coluna = linha = 0

for i in range(0,3):
    for c in range(0,3):
        lista [i][c] = int(input(f'Digite um valor para [{i}]:[{c}]: '))
print('-='*30)
for i in range(0,3):
    for c in range(0,3):
     print(f'[{lista[i][c]:^5}]',end=' ')
     if lista[i][c] % 2 == 0:
        soma+=lista[i][c]
    print()

for i in range(0,3):
   coluna+=lista[i][2]   # faz uma iteração com os elementos 1,2 e 3 da coluna 2

for i in range(0,3):     # faz uma iteração com a linha onde o primeiro range sempre será o maior valor, logo o maior recebe o valor range
   if i == 0:            # depois do primeiro range eu comparo o range atual com a variável "maior" que recebeu o valor do primeiro range.  
      linha = lista[1][c]  # se for maior altero o valor da variavel. 
   elif lista[1][c] > linha:
      linha = lista[1][c]
    

 

print(f' a soma dos valores pares é {soma}')
print(f'a soma dos elementos da 3º coluna é {coluna}')
print(f'o maior valor encontrado na segunda linha é {linha}')