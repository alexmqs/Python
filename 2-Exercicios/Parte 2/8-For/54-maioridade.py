'''
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''
from datetime import date


anoAtual = date.today().year
maioridade = 21
anoMaioridade = 0
atingiram = 0
natingiram = 0

for c in range(1, 8):
    anoNascimento = int(input('Digite o ano de nascimento: '))
    idade = anoAtual - anoNascimento
    if idade >= maioridade:
        atingiram += 1
    else:
        natingiram += 1

# Maiores de idade
if atingiram == 0:
    print(f'{atingiram} Nenhuma pessoa atingiu a maioridade')
elif atingiram == 1:
    print(f'{atingiram} pessoa atingiu a maioridade')
else:
    print(f'{atingiram} pessoas atingiram a maioridade')

# Menores de idade
if natingiram == 0:
    print(f'{natingiram} Nenhuma pessoa não atingiu a maioridade')
elif natingiram == 1:
    print(f'{natingiram} pessoa não atingiu a maioridade')
else:
    print(f'{natingiram} pessoas não atingiram a maioridade')
