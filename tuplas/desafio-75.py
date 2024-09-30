# escreva um programa que receba 4 numeros pelo teclado. Ao final o programa deve mostrar: 
# quantas vezes o numero 9 foi digitado, em qual posição foi digitado o valor 3 quantos foram os numero pares! 
tupla = ()
c = 0 
variavel = 0
for i in range (4):
    i = int(input('Digite um numero [0/10]: '))     
    if  i % 2 == 0: 
        c +=1         
    tupla += (i,)
    
    if i == 3: 
       posicao = tupla.index(3) + 1 
       
    else:
        pass
    
    
print(tupla)

digito_9 = tupla.count(9)


print(f'o numero 9 foi digitado {digito_9} vezes, já o numero 3 foi encontrado na posição {posicao}, foram digitados {c} números pares')