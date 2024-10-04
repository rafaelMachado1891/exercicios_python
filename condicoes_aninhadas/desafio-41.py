# a confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e enquadre ele dentro das categorias.
# até 9 anos mirim
# até 14 anos infantil
# ate 19 anos junior
# até 20 anos senior
# acima de 20 anos master
from datetime import date

nascimento = int(input('digite seu ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - nascimento

if idade <= 9:
    print('sua idade é {} anos, sua categoria é mirim'.format(idade))
elif idade <= 14:
    print('sua idade é {} anos, sua categoria é infantil'.format(idade))
elif idade <= 19:
    print('sua idade é {} anos, sua categoria é junior'.format(idade))
elif idade <= 20:
    print('sua idade é {} anos, sua categoria é senior'.format(idade))
else:
    print('sua idade é {} anos, sua categoria é master'.format(idade))

