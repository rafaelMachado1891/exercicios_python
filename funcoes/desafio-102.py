# Faça um programa que tenha uma função fatorial() que receba dois parametros: o primeiro que receba o numero a ser calculado
# e o segundo chamado show que será um valor logico (opcional) indicando se será mostrado o calculo do fatorial.

def fatorial (a, show=False):
    """
    Calcula o fatorial de um número.

    Parâmetros:
    a (int): O número do qual será calculado o fatorial.
    show (bool): Se True, exibe o cálculo passo a passo.

    Retorna:
    int: O valor do fatorial de `a`.
    """
    v = 1
    for i in range(a, 0, -1):
        if show:
            print(i, end=' ')
            if i > 1:
                print(f' x ', end=' ')
            else:
                print(f' = ', end=' ')

        v*=i
    return v

print(fatorial(5,True))
help(fatorial)


