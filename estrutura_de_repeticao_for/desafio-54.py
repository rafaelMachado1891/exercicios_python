# crie um programa que leia o nome de sete pessoas. 
# no final mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores
from datetime import date

menor = 0
maior = 0
ano = date.today().year

for i in range(1,8):
    nasc = int(input('Digite o ano de nascimento dos sete usuários: '))
    if ano - nasc < 18:
     menor += 1
     
    else:
     maior += 1 



print(f'{menor} pessoas são menores de idade e {maior} são maiores de idade')

        
