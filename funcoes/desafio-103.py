# escreva um programa que tenha uma função chamada ficha(), que receba dois parametros opcionais:
# o nome de um jogador e quantos gols ele marcou. 
# o progama deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente

def ficha(jog='<desconhecido>', gol=0):    # parametro opcional para declarar podemos informar valor como 0
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato')
    
    
j=str(input('Jogador: '))
g=str(input('numero de gols: '))
if g.isnumeric():
   g = int(g)
else:
   g = 0
if j.strip()=='':
   ficha(gol=g)
else:
   ficha(j,g)









