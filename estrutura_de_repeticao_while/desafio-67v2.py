# escreva um programa que calcule a tabuada de determinado número


while True:  
    numero = int(input('Digite um número: '))
    if numero < 0:
        break
    for i in range (1,11):
        resultado = numero*i
        print(f'{i} X {numero} = {resultado}' )

    