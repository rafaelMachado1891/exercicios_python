# escreva um programa que leia o primeiro termo e crie uma PA. No final mostre os 10 primeiros termos dessa progressao

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
decimo = primeiro + (10+1) * razao
for i in range(primeiro,decimo + razao, razao):    
    print(f'{i}')