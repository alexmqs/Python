'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai servir ao serviço militar
- Se é hora de se alistar
- Se já passou do tempo do alistamento
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
from datetime import date

anoNasc = int(input('Digite seu ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - anoNasc
idadeAlistamento = 18
falta = idadeAlistamento - idade
anoAli = anoNasc + idadeAlistamento
jaFoi = anoAtual - anoAli
print(f'Quem nasceu em {anoNasc} tem {idade} anos em {anoAtual}')

if idade < idadeAlistamento:
    if falta == 1:
        print(f'Falta {falta} ano para ele servir no quartel.')
        print(f'Você deve se alistar em {anoAli}')
    else:
        print(f'Falta {falta} anos para ele servir no quartel.')
        print(f'Você deve se alistar em {anoAli}')
elif idade == idadeAlistamento:
    print(f'Este ano de {anoAtual} ele terá que ir no quartel.')
else:
    print('Você não tem idade para o alistamento.')
    print(f'Seu alistamento foi há {jaFoi} anos, ou seja em {anoAli}')
