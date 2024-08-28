# Crie um programa q leia o nome completo de uma pessoa e mostre: 
# o nome com todas as letras maisculas

# comando para comentar em bloco crtl k + crtl c
# nome = input('Digite o seu nome: ')     
# print(nome.upper())

# o nome com todas as letras minusculas

# nome = input('Digite o seu nome: ')
# resultado = nome.lower()
# print('{}'.format(resultado))

# quantas letras ao todo sem considerar os espaços

# nome = input('Digite o seu nome: ')
# resultado = nome.split() # split faz a divisao da string apartir dos espaços ele cria uma lista com cada objeto divido por espaços
# #resultado = ''.join(resultado) # join faz a junção de elementos
# print(len(resultado))

# quantas letras tem o primeiro nome
nome = input('digite seu nome: ')
nome = nome.split()
resultado = len(nome[0])
print(resultado)


