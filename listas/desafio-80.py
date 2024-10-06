# Cri(e um programa que permita o usuário digita 5 valores. Os Valores devem ser adicionado a lista já na ordem correta sem usar o sort

lista = []

for i in range(0,5):
    v = int(input('digite um valor: '))
    if i == 0:
        lista.append(v)
    elif v > lista[-1]:
        lista.append(v)
    else:
        pos = 0 
        while pos < len(lista):
            if v <= lista[pos]:
                lista.insert(pos,v)
                break
            pos+= 1


print(f'{lista}')
    