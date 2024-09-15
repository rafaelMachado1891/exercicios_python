# faça um programa que leia a tabuada enquanto o numero não seja negativo

n = c = r =0

while True:
    n = int(input('Qual numero você deseja ver a tabuada [digite um valor negativo para interromper]: '))
    if n <= 0:
        break
    for i in range(1,11):
        r = n * i 
        print(f'{n} x {i} = {r}')
print('Acabou')