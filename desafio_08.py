# escreva um programa que recebe uma medida em metros e converta para centimetros e milimitros 
m = float(input('digite uma medida em metros: '))
c = m * 100
mi = c * 100
print('a conversao de {} para centimetros é: {} e para milimetros é {}'.format(m, c, mi))