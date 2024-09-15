# melhore o desafio 61 perguntando ao usuario se ele quer adicionar mais algum termo: 

numero = int(input('digite o primeiro termo: '))
razao = int(input('razao: '))
decimo = 0
while decimo < razao:
    decimo += 1
    pa = decimo * razao
    print(pa, end=' ')
print('deseja adicionar mais um termo?')
resposta = str(input()).lower()
if resposta == 'sim':
    nova_razao = int(input('digite o termo: '))
    decimo += 1
    new_pa = pa * nova_razao
    print(new_pa, end= ' ')
else: 
    print('vc encerrou o programa')
# print(pa)