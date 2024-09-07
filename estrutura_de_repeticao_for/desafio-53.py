# faça um programa que leia um frase e diga se ela é um palindromo

frase = str(input('digite uma frase: '))
frase_sem_espacos = frase.replace(" ", "")
inverso = frase_sem_espacos[::-1]

if inverso == frase_sem_espacos:
    print(f'a frase digitada {frase} é um palindromo')

else:
    print(f'a frase digitada não forma um palindromo {inverso}')
