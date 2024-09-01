# Crie um programa que leia um ano e diga se ele é bissexto
ano = int(input('Digite um ano: '))
v1 = ano % 4
v2 = ano % 100
v3 = ano % 400

if v1 ==0 & v2 ==0 & v3 ==0:
 print('O ano que vc digitou é bissexto')

else:
 print('esse não é um ano bissexto')