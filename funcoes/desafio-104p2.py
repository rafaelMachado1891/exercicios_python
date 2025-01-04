# crie um programa que tenha uma funcao chamada leiaint(), o programa deve validar se o valor digitado é um número.

def leiaint(i):
    while True:
        i = input('Digite um número: ')
        if i.isnumeric():
            return i
        else:
            print('Digite um valor númerico!')

    

n = leiaint('digite um numero: ')
print(f'você acabou de digitar o numero {n}')


