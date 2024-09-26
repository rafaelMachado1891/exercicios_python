# faça um programa que tenha uma tupla com diversas palavras, Depois mostre para cada palavra quais são suas vogais

p = ('Feijao', 'arroz', 'cafe')

for i in p:
    print(f'\n na palavra {i} temos as vogais ', end=' ')
    for letra in i:
        if letra in ('aeiou'):
            print(f'{letra}',end=' ')

    