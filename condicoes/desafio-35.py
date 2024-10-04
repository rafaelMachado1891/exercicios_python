#Crie um program que leia tres retas inseridas pelo usuário e diga se elas podem formar um triangulo

r1 = int(input('insira o valor da primeira reta: '))
r2 = int(input('insira o valor da segunda reta: '))
r3 = int(input('insira o valor da terceira reta: '))

if (r1 + r2 > r3) and (r1 + r3 > r2) and (r2 + r3 > r1): 
   print('as retas podem formar um triangulo')
else:
   print('as retas não formam um triangulo')
