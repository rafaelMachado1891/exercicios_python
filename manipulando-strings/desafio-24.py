# crie um programa que leia um nome e verifique se começa com santo
nome = input('Em qual cidade você nasceu?  ')
minusculo = nome.lower().strip()
resultado = minusculo[0:5] == 'santo'
print(resultado)