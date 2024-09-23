# Faça um programa que tenha uma tupla preenchida de 0 a 20. quando o usuario digitar pelo teclado o 
# programa deve retornar o numero por extenso

numero = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 
          'treze', 'quatorze', 'quinze', 'dezesseis','dezessete', 'dezoito', 'dezenove', 'vinte')

tecl = int(input('digite um numero entre 0 e 20: '))
while True:
    if tecl > 20 or tecl < 0:
     tecl = int(input('digite um numero válido entre 0 e 20: '))
    else:
       break

print(f'você digitou {numero[tecl]}')
