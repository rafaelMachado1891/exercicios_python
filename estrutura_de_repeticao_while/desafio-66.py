#faça um programa que receba os numeros do usuarios e ao final calcule a soma e a contagem dos valores. 
# 

n = c = s = 0
while True:
    n= int(input('digite um numero: [999 para interromper]: '))
    if n == 999:
        break
    c +=1
    s +=n
print(f'você digitou {c} valores e a soma é {s}')