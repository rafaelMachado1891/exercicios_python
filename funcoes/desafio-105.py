# Faça um programa que tenha uma função notas() que pode receber varias notas de alunos e vai retornar um dicionario
# com as seguintes informações: 
# Quantidade de notas
# A maior nota
# A menor nota
# A média da turma
# A situação 

def notas(*p):
    v = {
        'total notas': len(p),
        'maior nota': max(p),
        'menor nota': min(p),
        'media': sum(p) / len(p)
    }
    
    return v


n = notas(5.5, 6, 4.3, 2)

print(n)