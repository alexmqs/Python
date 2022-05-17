'''
A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: Mirim
- Até 14 anos: Infantil
- Até 19 anos: Junior
- Até 20 anos: Sênior
- Acima: Master
'''
from datetime import date


an = int(input('Digite o ano de nascimento: '))
calId = date.today().year - an
m = 9
i = 14
j = 19
s = 20

if calId <= m:
    print('Mirim')
elif calId <= i:
    print('Infantil')
elif calId <= j:
    print('Junior')
elif calId <= s:
    print('Sênior')
else:
    print('Master')
