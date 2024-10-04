# Faça um programa que pergunte o salário do funcionario e calcule o aumento.
# para salarios acima de 1250 haverá um aumento de 10% 
# para salarios abaixo de 1250 o aumento é de 15% 
s= float(input('Digite o seu salário: '))
aumento1 = float(s*1.1)
aumento2= float(s*1.15)
variavel = 1250

if s > variavel:
    print('seu novo salario com reajuste é de R${}'.format(aumento1))
else:
    print('seu novo salario com reajuste é R${}'.format(aumento2))