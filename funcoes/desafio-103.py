# escreva um programa que tenha uma função chamada ficha(), que receba dois parametros opcionais:
# o nome de um jogador e quantos gols ele marcou. 
# o progama deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente

def ficha(a=0, b=0):    # parametro opcional para declarar podemos informar valor como 0
    a=str(input('Jogados: '))
    b=int(input('Gols: '))    
    print(f'Jogador: {a}')
    print(f'Numero de Gols: {b}')
    return a,b






