# Crie um program que receba uma frase qualquer, diga quantas vezes a letra a aparece
# qual é a posição da primeira aparição da letra a e a posição da ultima aparição

frase = str(input('Digite uma frase qualquer: ')).strip().lower()
numero = frase.count('a')
posicao = frase.find('a') + 1
ultima_posicao = frase.rfind('a') + 1
comprimento = len(frase)
print('a letra "a" aparece {} vezes na frase'.format(numero))
print('a primeira posição em que a letra "a" aparece é {}'.format(posicao))
print('a ultima posição em que a letra "a" aparece é {}'.format(ultima_posicao))
print('o comprimento total da frase é {}'.format(comprimento))
