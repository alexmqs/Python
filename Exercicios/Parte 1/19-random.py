'''
19
Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
faça um programa que ajude ele, lendo o nomes deles e escrevendo o nome do escolhido.
'''

from random import choice

aluno1 = str(input('Qual o nome do 1º aluno? '))
aluno2 = str(input('Qual o nome do 2º aluno? '))
aluno3 = str(input('Qual o nome do 3º aluno? '))
aluno4 = str(input('Qual o nome do 4º aluno? '))
lista = [aluno1, aluno2, aluno3, aluno4]
resultado = choice(lista)

print(f'O aluno do aluno escolhido foi {resultado}')
