# faça um programa que solicite o sexo do usuario, o programa deve aceitar somente M ou F.

nome = str(input('digite o sexo do usuario [M/F]: ')).upper().strip()[0]

while nome not in 'MF':    
    nome = str(input('você digitou o valor incorreto, digite novamente [M/F]: ')).upper().strip()[0]
print(f'sexo do usuario insrido com sucesso {nome}')