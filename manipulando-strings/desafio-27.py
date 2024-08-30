# faça um programa que receba o nome completo de um usuário e mostre o primeiro e o ultimo nome]
nome = str(input('digite seu nome completo: ')).strip()
lista = nome.split()
primeiro_nome = lista[0]
ultimo_nome = lista[-1]
numero_elementos = len(lista)
ultimo_nomev2 = lista[numero_elementos - 1]
print(primeiro_nome)
print(ultimo_nome)
print(numero_elementos)
print(ultimo_nomev2)