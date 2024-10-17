#faça um programa que leia o nome, ano de nascimento e carteira de trabalho e cadastre-os em um dicionário.
# se ´pr acasp a ctps for diferente de zero, o dicionário recenera também o ano de contratação e o salário.
# calcule e acrescente, alem da idade, com quantos anos a pessoa vai se aposentar. 

from datetime import datetime
dados={}

nome = str(input('Nome: ')).upper()
nascimento = int(input('Ano Nascimento: '))
carteira_trabalho = int(input('Possui_carteira: [0] não/ [1] sim: '))
idade =  datetime.today().year - nascimento # - nascimento 

dados ['Nome'] = nome,
dados ['Nascimento']= nascimento,
dados ['Carteira_trabalho']= carteira_trabalho,
dados ['Idade']=idade

if carteira_trabalho != 0:
    dados ['Contratacao'] = int(input('Digite o ano de contratacao: '))
    dados ['Salario'] = float(input('Digite o salário base: ')) 
 
tempo = 35 - (datetime.today().year - dados['Contratacao'])
dados ['Tempo_aposentadoria'] = tempo

print(dados)