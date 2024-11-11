# Crie um programa que contenha uma função chamada voto que vai receber como parametro o ano de nascimento.
# retornando o valor literal indicando se a pessoa tem voto obrigatório,  negado ou opcional. 

from datetime import datetime

def mostrar_condicao_do_voto(v):
    data = datetime.now()
    ano = data.year
    idade = ano - v
    if idade < 18:
        return 'Você não tem idade para votar!'
    elif idade >= 65:
        return 'O voto é opcional!'
    else:
        return 'Voto obrigatório!'



print(mostrar_condicao_do_voto(int(input('Em que ano você nasceu: '))))


