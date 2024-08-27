#faça um program que receba um angulo qualquer e calcule o seno, cosseno e tangente
import math

an = int(input('digite o angulo desejado: '))
s = math.sin(math.radians(an))
c = math.cos(math.radians(an))
t = math.tan(math.radians(an))

print('para o angulo de {} graus o seno é {:.2f}, o cosseno é {:.2f} e a tanjente é {:.2f}'.format(an,s,c,t))