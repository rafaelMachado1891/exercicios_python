# faça um programa que leia o ano de nascimento do usuário e indique se ele está no periodo de alistamento, se já passou o periodo
# ou então quanto tempo falta para o alistamento
from datetime import date

nascimento = int(input('digite o ano do seu nascimento: '))
ano_atual = date.today().year
variavel = ano_atual - nascimento
var = 18 - variavel
if variavel > 18:
    print('Você já passou do período de alistamento')
elif variavel < 18:
    print('Você não está no período de alistamento, faltam {} anos para você se alistar'. format(var))
else:
    print('você completa {} anos esse ano, está no período de alistamento'.format(variavel))

