'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''
from datetime import date

dicPrev = {}

# estrutura principal
dicPrev['nome'] = str(input('Nome:'))
anoNasc = int(input('Ano de Nascimento:'))
dicPrev['idade'] = date.today().year - anoNasc
dicPrev['ctps'] = int(input('Carteira de trabalho: (0 não tem)'))

if dicPrev['ctps'] != 0:
    dicPrev['contratacao'] = int(input('Ano de contratação:'))
    dicPrev['salario'] = float(input('Salário: R$'))
    dicPrev['aposentadoria'] = (dicPrev['contratacao'] - anoNasc) + 35
# fim estrutura principal

print('=-='*10)
for k, v in dicPrev.items():
    print(f'{k} tem o valor {v}')
