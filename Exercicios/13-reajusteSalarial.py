# 13
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Valor salário: '))
valQuantAum = float(input('Quantos % de aumento: '))
aumento = salario * valQuantAum / 100
salarioFinal = salario + aumento

print(
    f'Um funcionário que ganhava R${salario:.2f}.\nA partir de agora com o aumento de {valQuantAum}%(R${aumento:.2f}) seu novo sálario será: R${salarioFinal:,.2f}')
