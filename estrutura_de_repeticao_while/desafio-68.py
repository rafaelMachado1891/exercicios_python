#faça um programa que jogue par ou impar com o computador, o programa só deve parar quando o usário vencer! 
import random as rd
print('vamos jogar par ou impar?')
print('-'*40)

v = ''

while True:
    n = int(input('escolha um numero: '))
    escolha = str(input('você quer [Par/Impar]? ')).lower().strip()
    while escolha not in 'par/impar':
     escolha = str(input('você quer [Par/Impar]? ')).lower().strip()
    maq = int(rd.randint(0,10))
    resultado = (n + maq)
    resto = resultado % 2
    soma = n+maq
    if escolha == 'par' and resto == 0:
       print(f'minha escolha foi {maq}, o resultado é {soma}. Você venceu')
       break

    elif escolha =='impar' and resto != 0:
       print(f'minha escolha foi {maq}, o resultado é {soma}. Você venceu')
       break
    else:
      print(f'minha escolha foi {maq}, o resultado é {soma}. Mais sorte da próxima vez!')
    
print('Fim')      






