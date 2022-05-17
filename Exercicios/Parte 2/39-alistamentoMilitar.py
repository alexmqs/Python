'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai servir ao serviço militar
- Se é hora de se alistar
- Se já passou do tempo do alistamento
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
from datetime import date, datetime
an = int(input('Digite seu ano de nascimento: '))
calIdade = date.today().year - an
idadeAlis = 18
falta = idadeAlis - calIdade

if calIdade < idadeAlis:
    if falta == 1:
        print(f'Falta {falta} ano para você servir no quartel.')
    else:
        print(f'Falta {falta} anos para você servir no quartel.')
elif calIdade == idadeAlis:
    print(f'Este ano você terá que ir no quartel.')
else:
    print('Você não tem idade para o alistamento.')
