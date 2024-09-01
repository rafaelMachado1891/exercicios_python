# Crie um programa que pergunte a distancia de um voo para o usuário e calcule o preço da passagem. considere 0.50 para voos de até 200 km e 0.45 para voos mais longos

d = int(input('qual é a distância de sua viagem? '))
c = float(d*0.50)
l = float(d*0.45)

if d >= 200: 
    print('O valor da passagem é R${:.2f}'.format(l))
else:
    print('sua passagem custará {}')

