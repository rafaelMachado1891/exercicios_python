# faça um programa que ajude um professor a sortear um dos 4 alunos
import random

lista = ['Pedro', 'João', 'Paulo', 'Davi']
aluno = random.choice(lista)
print('O aluno escolhido é o {}'.format(aluno))