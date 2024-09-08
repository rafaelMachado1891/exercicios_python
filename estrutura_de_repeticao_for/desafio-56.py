# desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. Mostre na tela a media de idade o homem mais velho
# e quantas mulheres tem menos de 20 anos
soma_idade = 0
maior_idade = 0
nome_maior_idade = ''
totalmulher20 = 0

for i in range(1,5):
    nome = str(input(f'{i}º pessoa: '))
    idade = int(input('idade: '))
    sexo = str(input('sexo - (M/F): '))
    soma_idade += idade
    if i == 1 and sexo in 'mM':
     maior_idade = idade
     nome_maior_idade = nome
    if sexo in 'mM' and idade > maior_idade:
       maior_idade = idade
       nome_maior_idade = nome
    if sexo in 'fF' and idade < 20:
       totalmulher20 += 1
    print('-----------')

media = soma_idade /4
print(f'a media de idade das 4 pessoas é {media}')
print(f'o nome do homem mais velho é {nome_maior_idade} e ele possui {maior_idade} anos')
print(f'o numero de mulheres abaixo de 20 anos é {totalmulher20}')

 