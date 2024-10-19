# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário 
# e todos os dicionários em uma lista. No final, mostre: Quantas pessoas foram cadastradas, e média de idade do grupo.
# uma lista com todas as mulheres, uma lista com todas as pessoas com idade acima da média. 
lista = []
listam = []
r= 'S'
total=0
maior = []

while r == 'S':
    dicionario = {}
    dicionario ["Nome"] = str(input('nome: ')).upper()
    dicionario ["Sexo"] = str(input('sexo [M/F]: ')).upper().strip()[0]
    dicionario ["idade"] = int(input('idade: '))
    lista.append(dicionario)
    r=str(input('deseja continuar?: ')).upper().strip()[0]
    while r not in ('SN'):
          r=str(input('deseja continuar?: ')).upper().strip()[0]

print('-='*30)
    
print(lista)

print('-='*30)

print(f'No total foram cadastradas {len(lista)} pessoas.')

for i in lista:
     if i['Sexo'] == 'M':
          listam.append(i)

print(f'As pessoas de sexo masculino cadastradas foram:')

for i in listam:
     print(i)

for i in lista:
     total+= i['idade']

media = total / len(lista)
     
print(f'a media de idade das pessoas cadastradas é {media}')

for i in lista:
     if i['idade'] > media:
          maior.append(i)

print(f'As pessoas com idade acima da média são {maior}')

    
    

    