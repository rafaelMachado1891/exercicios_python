def dobro (a):
    val = a*2
    return val

def metade (p):
    val = p / 2 
    return val

def aumentar(a=0):
    b=int(input('Quanto % você deseja aumentar: '))
    per = b / 100
    valor = a * (1+ per)
    return valor

def diminuir(a=0, b=0):
    b=int(input('Quanto % você deseja diminuir: '))
    per = b / 100
    valor = a *(1- per)
    return valor
