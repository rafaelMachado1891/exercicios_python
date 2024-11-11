# Crie um programa que contenha uma função chamada voto que vai receber como parametro o ano de nascimento.
# retornando o valor literal indicando se a pessoa tem voto obrigatório,  negado ou opcional. 



def mostrar_condicao_do_voto(ano):
    from datetime import date
    data = date.today().year
    idade = data - ano
    if idade < 16:
        return f'Com {idade} anos você não tem idade para votar!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos o voto é opcional!'
    else:
        return f'Com {idade} anos o voto obrigatório!'



print(mostrar_condicao_do_voto(int(input('Em que ano você nasceu: '))))


