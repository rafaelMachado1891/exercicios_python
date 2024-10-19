# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário 
# e todos os dicionários em uma lista. No final, mostre: Quantas pessoas foram cadastradas, e média de idade do grupo.
# uma lista com todas as mulheres, uma lista com todas as pessoas com idade acima da média. 
lista = []
r= 'S'

while r == 'S':
    dicionario = {}
    dicionario ["Nome"] = str(input('nome: '))
    dicionario ["Sexo"] = str(input('sexo [M/F]: ')).upper().strip()[0]
    dicionario ["idade"] = int(input('idade: '))
    lista.append(dicionario)
    r=str(input('deseja continuar?: ')).upper().strip()[0]
    
print(lista)
    
    

    