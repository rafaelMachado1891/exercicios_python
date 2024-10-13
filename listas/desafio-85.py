#faça um programa onde o usuário possa digitar sete valores numericos e cadastre-os em uma unica lista. 
# Mantenha separado os valores pares e impares. No final mostre as números em ordem crescente. 

lista_princ = [[],[]]


for i in range(0,7):
    i = int(input('Digite um valor: '))
    if i % 2 == 0:
        lista_princ[0].append(i)
        
    else:
        lista_princ[1].append(i)
        
    lista_princ[0].sort()
    lista_princ[1].sort()
    
print('-='*30)

print(f'Os numeros digitados foram{lista_princ}')

print(f'Os numeros pares são {lista_princ[0]}')

print(f'Os numeros Impares digitados são {lista_princ[1]}')


