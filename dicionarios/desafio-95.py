# Faça um programa que gerencie o rendimento de um atleta. O programa vai ler o nome do jogador e quantas
# partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. 
# No final, tudo isso será guardado em um dicionario, incluindo o total de gols feitos durante o campeonato.
lista = []
jogador = {}
time = []

while True:
    jogador.clear()
    jogador['Nome'] = str(input('Jogador: ')).upper()
    partidas = int(input('Nº de paritdas: '))
    lista.clear()
    for i in range(partidas):
        lista.append(int(input(f'{i+1}º partida: ')))
    jogador['Gols'] = lista[:]
    jogador['total'] = sum(lista)
    time.append(jogador.copy())
    while True:
        r=str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
        if r in ('NS'):
            break
        print('Digite uma opção valida S ou N')
    if r == 'N':
        break   

print('-='*30)

print('cod ', end='')

for i in jogador.keys():
    print(f'{i:<15}',end='')

print()

print('-='*30)

for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')    
    print()

print('-='*30)

while True:
    busca=int(input('De qual jogador você deseja mostrar os dados? digite[999] para encerrar: '))
    if busca == 999:
        break
    if busca > len(time):
        print('digite um valor válido para o jogador:')
    else:
        print(f'Levantamento dos dados do  jogador {time[busca]['Nome']}: ')
        for i, v in enumerate(time[busca]['Gols']):
            print(f'  No jogo {i+1} fez {v} gols')
    print('-='*30)

    