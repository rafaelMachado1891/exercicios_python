# ordem de precedencia no python - 1º () 2º ** 3º * / // % 4º +- 
expressao_01 = 5 + 3 * 2

print(expressao_01)

expressao_02 = 3 * 5 + 4 ** 2 

print(expressao_02)

expressao_03 = 3 * ( 5 + 4) ** 2 
print(expressao_03)

n = int(input('digite um valor: '))
n2 = int(input('digite outro valor: '))
s = n+n2
m = n * n2
d = n / n2
p = n ** n2 
di = n // n2 
r = n % n2 
print('a soma dos valores è {}, \n a multiplicação dos valores é {} e a divisao é {}'.format(s, m ,d ), end='') # end= ' ' evita a quebra de linhas do programa
print('a divisao inteira dos valores é {} a potenciacao dos valores é {} o resto da divisao é {}'.format(di, p, r)) #\n efetua a quebra da linha