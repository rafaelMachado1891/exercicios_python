#faça um mini-sistema que utilize o interactive help do python. o usuário vai digitar o comando e o manual vai aparecer.
# Quando o usário digitar a palavra 'FIM', o programa se encerrará. 
# obs: use cores

def analisar_funcao(a):
    print(f'Funcao {a} ',30)
    print('-='*30)
    help(a)


funcao = ''
while True:
    funcao = str(input('Digite uma funcao: '))
    if funcao.upper() == 'FIM':
        break 
    else:
        analisar_funcao(funcao)

