# crie um programa que leia a idade e o sexo de varias pessoas. A cada pessoa cadastrada o programa 
# deve perguntar ao usuário se ele quer continuar. No final mostre, quantas pessoas tem mais de 18 anos, quantos homens 
# foram cadastrados e quantas mulheres tem menos de 20 anos.

m = f = idade = feminino = 0
soma = m + f
resposta = 'S'

while resposta == 'S':
    i = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()[0]
    while sexo not in 'MF':
       sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()[0]
    resposta = str(input('Você desejas continuar o cadastro? [S/N]: ')).upper().strip()[0]
    while resposta not in 'SN':
       resposta = str(input('Você desejas continuar o cadastro? [S/N]: ')).upper().strip()[0]
    if sexo in 'M':
       m+=1
    else:
       f+=1
    soma+=1
    if i >= 18:
       idade+=1
    if i < 18 and sexo in 'F':
       feminino+=1

print(f'foram cadastrados {soma} pessoas sendo {m} homens, {idade} pessoas maiores de 18 anos e {feminino} mulheres menores que 18 anos')
    