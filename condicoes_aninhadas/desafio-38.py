# escreva um programa que leia dois numeros e retorne ao usuário se o primeiro numero é o maior, o segundo valor é o maior ou os valores são iguais.

num_1 = int(input('digite o primeiro valor: '))
num_2 = int(input('digite o segundo valor: '))

if num_1 > num_2: 
    print('o primeiro valor {} é maior que o segundo valor {}'.format(num_1, num_2))
elif num_2 > num_1:
    print('o segundo valor {} é maior que o primeiro valor {}'.format(num_2, num_1))
else:
    print('os valores digitados são iguais')
