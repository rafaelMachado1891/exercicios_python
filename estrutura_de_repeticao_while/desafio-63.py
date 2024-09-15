# escreva um program que leia um numero inteiro e mostre os n termos da sequencia de fibonnati exercicios_python/estrutura_de_repeticao_while 

n = int(input('digite o numero de termos: '))
print('-'*30)
t0 =0
t1 =1
c =0
print(f'{t0} -> {t1} ->',end=' ')
while c < n:
 t3 =t0+t1
 t0 = t1
 t1 = t3
 c+=1
 print(f'{t3} -> ', end=' ')
print('fim')
