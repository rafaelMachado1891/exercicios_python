# Faça um programa que leia varios números e coloque-os em uma lista. Deposi disso mostre: 
# Quantos numeros foram digitados, a lista de valores ordenadas de forma decrescente. 
# Se o valor 5 foi digitado e está ou não na lista. 
lista = []
v= int(input('Digite um valor: '))
lista.append(v)

while True:
    r=str(input('Desaja adicionar mais valores[S/N]: ')).upper().strip()[0]
    while r not in ('SN'):
      r=str(input('Desaja adicionar mais valores[S/N]: ')).upper().strip()[0]
    if r=='S':
        v= int(input('Digite um valor: '))
        lista.insert(0,v)
    else:
        break

c = len(lista) # comprimento da lista

o = lista.sort(reverse=True)

p = lista.index(5) + 1

print('-'*30)
print(f'você digitou {c} valores')
print(f'Os valores digitados foram {lista}')


if 5 in lista:
    print(f'o valor 5 foi encontrado na lista na posição {p}')
else:
    print('O valor 5 não foi encontrado na lista')


