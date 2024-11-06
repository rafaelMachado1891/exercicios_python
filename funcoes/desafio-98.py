# faça um programa que tenha uma função chamada contador, a função deve exibir receber tres parametros.
# inicio, fim, e passo. A funcção deve retornar 3 resultados, 1º 1 a 10 de 1 em 1, de 10 a 1 de 2 a 2 
# e um resultado onde o usuário digite inicio fim e passo! 
from time import sleep


def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(1)
    if p < 0:
        p *= -1
    if p ==0:
        p= 1
    if i < f:
        cont=i
        while cont <= f:
            print(f'{cont} ', end='',flush=True)
            sleep(0.5)
            cont+=p
        print('Fim!')
    else:
        cont = i
        while cont>=f:
            print(f'{cont} ', end='',flush=True)
            sleep(0.5)
            cont-=p
        print('Fim!')


contador(1,10,1)
contador(10,0,2)
print('=-'*20)
print('Adicione os elementos para realizar a contagem')
print('=-'*20)
inicio = int(input('Adicione um valor para o inicio da contagem: '))
fim= int(input('Adicione um valor para o fim da contagem: '))
passo= int(input('Adicione o valor do passo: '))
contador(inicio, fim, passo)


