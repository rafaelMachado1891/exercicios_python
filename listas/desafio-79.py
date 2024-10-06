# Crie um programa onde o usuário possa digita varios valores numericos e cadastre-os em uma lista
# Caso o numero já exista lá dentro ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados em ordem crescente

r = 'S'
lista = []
v = 0

while True:
    if r == 'N':
        break
    else:
        v = int(input('Digite um número: '))
        if v in lista:
         pass
        else:
         lista.append(v)

    r = str(input('Deseja adcionar mais valores [S/N]: ')).upper().strip()[0]
lista.sort()
print(f'{lista}')