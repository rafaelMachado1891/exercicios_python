# escreva um programa que avalie um emprestimo ao usuário, a condição é que o valor da parcela não exceda 30% da sua renda.
# para avaliar o emprestimo deve-se levar em conta o valor de emprestimo e o numero de parcelas.

valor = float(input('qual o valor que você deseja? ')) 
periodo = int(input('em quanto tempo você deseja pagar? ')) * 12 
salario = float(input('qual é o valor da sua renda? '))
parcela = float(valor / periodo )
p = float(parcela / salario)

if p <= 0.30: 
    print('seu emprestimo foi aprovado! sua percela ficou no valor de R${:.2f}'.format(parcela))

else:
    print('seu emprestimo foi negado! o valor da parcela R${:.2f} ultrapassou o limite ficando em {:.2f}% sobre sua renda'.format(parcela, p))

#print('pagando em {} meses o valor da sua parcela é R${:.2f} e compromente {:.2f}% da sua renda'.format(periodo, parcela, p))