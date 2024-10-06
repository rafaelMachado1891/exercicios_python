# Crie um programa que receba varios números e adicione-os em uma lista. 
# Crie mais duas listas extras que contenha apenas os numeros pares e outra apenas com os numeros impares

lista = []

lista_p = []

lista_i = []

v = int(input('Digite um valor: '))

lista.append(v)

while True:
    r = str(input('Deseja adicionar mais valores [S/N]: ')).upper().strip()[0]
    while r not in ('SN'):
        r = str(input('Digite uma condição válida [S/N]: ')).upper().strip()[0]
    if r == ('S'):
        v = int(input('Digite um valor: '))
        lista.insert(0,v)
    else:
        break

print('=-'*30)

print(f'Os valores digitados foram {lista}')

for i in lista:
    if i % 2==0:
        lista_p.insert(0,i)
    else:
        lista_i.insert(0,i)
print(f'os valores pares da lista são {lista_p}')
print(f'os valores impares da lista são {lista_i}')