'''
A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: Mirim
- Até 14 anos: Infantil
- Até 19 anos: Junior
- Até 20 anos: Sênior
- Acima: Master
'''
from datetime import date


ano = int(input('Digite o ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - ano
m = 9
i = 14
j = 19
s = 20
print(f'O atleta tem {idade} ano(s)')
if idade <= m:
    print('Mirim')
elif idade <= i:
    print('Infantil')
elif idade <= j:
    print('Junior')
elif idade <= s:
    print('Sênior')
else:
    print('Master')
