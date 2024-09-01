#escreva um programa que leia a velocidade de um carro e notifique o condutor caso ele tenha excedido 80km/h, a multa custa R$ 7.00 a cada km excedente
limite = int(80)
velocidade = int(input('qual foi a velocidade atingida: '))
excedente = velocidade - limite
multa = float(excedente *  7)
if velocidade > limite:
    print('Você excedeu o limite de velocidade de {}km/h em {}km/h.\nVocê será multado em R${:.2f}'.format(limite, excedente, multa))
else:
    print('você está dentro do limite de velocidade {}'.format(limite))    