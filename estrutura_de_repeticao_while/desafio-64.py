# faça um program que leia diversos numero pelo teclado, o program só para quando o numero digitado for 999,
# ao final mostre quantos numeros foram digitado e qual a soma deles.

n= c= total= 0
n = int(input('digite um numero: [digite 999 para parar]'))

while n != 999:
    c +=1
    total +=n
    n = int(input('digite um numero: [digite 999 para parar]'))
print(f'foram digitados {c} numeros e a soma desses numeros é {total}')