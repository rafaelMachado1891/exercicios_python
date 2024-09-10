# crie um program que receba dois numeros e crie um menu em que 1 = soma 2 = multilicação 3 = divisao 4 = maior valor e 5 encerra o programa

n1 = float(input('Digite o 1º valor: '))
n2 = float(input('Digite o 2º valor: '))
i = 0
operacao = int(input('[1]somar\n[2]multiplicar\n[3]dividir\n[4]maior\n[5]sair '))
while operacao != 5:
    n1 = float(input('Digite o 1º valor: '))
    n2 = float(input('Digite o 2º valor: '))
    operacao = int(input('[1]somar\n[2]multiplicar\n[3]dividir\n[4]maior \n[5]sair '))
    if operacao == 1:
        soma =n1 + n2
        print(f' a soma de {n1} + {n2} é =  {soma}')
    elif operacao ==2:
        multiplicacao = n1 * n2
        print(f'a multiplicação de {n1} X {n2} é = {multiplicacao}')
    elif operacao ==3:
        divisao = n1 // n2
        print(f'a divisão de {n1} / {n2} é = {divisao}')
    elif operacao ==4:
        maior= max(n1,n2)
        print(f'o maior valor entre {n1} e {n2} é = {maior}')
print('você encerrou o progama')        
 