# crie um programa que leia o nome de sete pessoas. 
# no final mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores
from datetime import date

lista =[]
lista_2 = []
ano = date.today().year

for i in range(1,8):
    nasc = int(input('Digite o ano de nascimento dos sete usuários: '))
    if ano - nasc < 18:
     lista.append(nasc)
     
    else:
     lista_2.append(nasc)  

menor = len(lista)  
maior = len(lista_2)

print(f'{menor} pessoas são menores de idade e {maior} são maiores de idade')

        
