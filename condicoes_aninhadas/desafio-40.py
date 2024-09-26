# crie um programa que receba duas notas do aluno e calcule a sua média. 
# media abaixo de 5 é reprovado, entre 5 e 6,9 recuperação e acima de 6.9 aprovado
import math

nota_1 = float(input('digite a primeira nota: '))
nota_2 = float(input('digite a segunda nota: '))

media = (nota_1 + nota_2) / 2 

if media < 5:
    print('sua nota foi {:.2f} você foi reprovado'.format(media))
elif media >= 5 and media < 6.9: 
    print('sua nota é {:.2f} você está em recuperacao'.format(media))
else:
    print('sua nota é {:.2f} parabens! você foi aprovado'.format(media))
