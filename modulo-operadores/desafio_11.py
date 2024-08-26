# faca um programa que calcule a area de uma parede e retorne a quantidade de tinta necessaria para pinta-la, sabendo q cada litro rende até 2m²
l = float(input('qual é a largura da sua parede? '))
a = float(input('qual é a altura da sua parede? '))
area = l * a 
necessidade = area / 2
print('a quantidade de tinta necessaria para pintar sua parede de {:.2f}m² é de {:.2f} litros'.format(area, necessidade))