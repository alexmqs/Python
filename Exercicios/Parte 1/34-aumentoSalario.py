'''
Escreva um programa que pergunte o sálario de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
'''

sal = float(input('Digite o salário: '))
salSup = sal + (sal * 10 / 100)
salInf = sal + (sal * 15 / 100)

if sal > 1250:
    print(f'O seu novo salário é R${salSup:.2f}, já com 10% de aumento.')
else:
    print(f'O seu novo salário é R${salInf:.2f}, já com 15% de aumento.')
