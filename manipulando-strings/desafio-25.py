# crie um programa que diga ao usuario se nome digitado pertence a familia silva

nome = str(input('Digite seu nome completo: '))
minusculo = nome.lower()
resultado = 'silva' in minusculo
print(resultado)