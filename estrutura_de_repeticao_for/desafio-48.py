# faça um programa que calcule a soma de todos os multiplos de 3 do 1 ao 500! 


soma = 0

for i in range(1,501):
    if i % 3 ==0:
        soma += i
print('a soma dos numeros divisiveis por 3 entre 1 e 500 resulta em {}'.format(soma))

