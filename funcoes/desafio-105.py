# Faça um programa que tenha uma função notas() que pode receber varias notas de alunos e vai retornar um dicionario
# com as seguintes informações: 
# Quantidade de notas
# A maior nota
# A menor nota
# A média da turma
# A situação 

def notas(*p, sit=False):      # 
    v = {
        'total notas': len(p),
        'maior nota': max(p),
        'menor nota': min(p),
        'media': sum(p) / len(p)
    }
    if sit:
        if v['media'] >=7:
            v['situação'] = 'BOA'
        elif v['media'] >= 5:
            v['situação'] = 'RAZOAVEL'
        else:
            v['situação'] = 'RUIM'
    
    return v


n = notas(5.5, 6, 4.3, 2, 7, 8.8, 10, 9.75, 3.2, 7.4, 10, sit=True)

print(n)