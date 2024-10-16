# faça um programa que leia nome e media de um aluno. guardando também a situação em um dicionario
# no final mostre o conteudo da estrutura na tela.
dicionario = {}
dicionario ['Nome'] = str(input('Nome: '))
dicionario ['media'] = float(input('media: '))
if dicionario['media']>= 7:
    dicionario ['situação'] = 'aprovado'
else:
    dicionario ['situação'] = 'reprovado'

for i, v in dicionario.items():
    print(f'{i} é igual a {v}')