# Faça um programa que gerencie o rendimento de um atleta. O programa vai ler o nome do jogador e quantas
# partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. 
# No final, tudo isso será guardado em um dicionario, incluindo o total de gols feitos durante o campeonato.

lista = []
total = 0
dicionario = {}

jogador = str(input('Jogador: '))
partidas = int(input('Nº de paritdas: '))
for i in range(partidas):
    lista.append(int(input(f'jogo {i+1}: ')))

for i, v in enumerate(lista):
    total+=v

print('-='*30) 

dicionario ['Jogador'] = jogador
dicionario ['Gols'] = lista
dicionario ['Total'] = total

print(dicionario)

print('-='*30) 

for k, v in dicionario.items():
    print(f'{k:<15} {v}')

print('-='*30) 

print(f'O jogador {dicionario["Jogador"]} tem {partidas} partidas.')

for k, v in enumerate(dicionario['Gols']):
    print(f'Na partida {k+1} marcou {v} gols')

print('-='*30) 


