# Crie um programa que simule um caixa eletronico! o programa deve liberar notas de 50, 20 10 e 1 Real

print('='*30)
print('{:^30}'.format('Banco CEV'))
print('='*30)

valor = int(input('Qual valor você deseja sacar? R$'))
Total = valor
ced50 = 50
c = 0

while True:
    if Total >= ced50:
        Total -= ced50
        c +=1
    else:
        if c > 0:
            print(f'Total de {c} cédulas de R$ {ced50:.2f}')
        if ced50 == 50:
            ced50 = 20
        elif ced50 ==20:
            ced50 = 10
        elif ced50 == 10:
            ced50 = 1
        c = 0
        if Total == 0:
         break




#exercicios_python/estrutura_de_repeticao_while


      
