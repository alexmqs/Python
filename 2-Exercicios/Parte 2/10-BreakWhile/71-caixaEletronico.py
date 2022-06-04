'''Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao user qual será o valor sacado (int) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10, R$1.'''
from operator import truediv
from pickle import TRUE


while True:
    print('-'*20, 'Banco Virtual', '-'*20)
    valor = int(input('Qual o valor do saque: R$'))
    # notas de 50
    nota50 = valor // 50
    # valor que falta
    faltaValor = valor-(nota50 * 50)
    # notas de 20
    nota20 = faltaValor // 20
    # valor que falta
    faltaValor = faltaValor - (nota20 * 20)
    # notas de 10
    nota10 = faltaValor // 10
    # valor que falta
    faltaValor = faltaValor - (nota10 * 10)
    # notas de 1
    nota1 = faltaValor // 1
    # valor que falta
    faltaValor = faltaValor - (nota1 * 1)
    # saindo do programa
    if faltaValor == 0:
        break
print(f'-'*20, 'Saindo do Banco', '-'*20)
if nota50 != 0:
    print(f'{nota50} cédulas de R$50,00')
if nota20 != 0:
    print(f'{nota20} cédulas de R$20,00')
if nota10 != 0:
    print(f'{nota10} cédulas de R$10,00')
if nota1 != 0:
    print(f'{nota1} cédulas de R$1,00')
print(f'Você sacou R${valor:.2f}')

# outro modo
print('-'*20, 'Banco Virtual', '-'*20)
valorSaque = int(input('Qual o valor do saque: R$'))
valorCed = 50
totCedSacadas = 0

while True:
    # retirando cédulas
    if valorSaque >= valorCed:
        valorSaque -= valorCed
        totCedSacadas += 1
    # alternando cédulas
    else:
        if totCedSacadas > 0:
            print(f'Total de {totCedSacadas} cédulas de R${valorCed}')
        if valorCed == 50:
            valorCed = 20
        elif valorCed == 20:
            valorCed = 10
        elif valorCed == 10:
            valorCed = 1
        totCedSacadas = 0
        if valorSaque == 0:
            break
print(f'-'*20, 'Saindo do Banco', '-'*20)
print(f'Você sacou R${valorSaque:.2f}')
