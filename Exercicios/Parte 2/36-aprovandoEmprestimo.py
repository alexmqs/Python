'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
'''
valCasa = float(input('Qual o valor da casa? R$'))
salCom = float(input('Qual o salário do comprador? R$'))
anos = int(input('Em quantos anos deseja pagar? '))
valPrest = valCasa / (anos * 12)
minSal = salCom * 30 / 100
print(valPrest)
print(minSal)
print(f'Para pagar uma casa de R${valCasa:.2f} em {anos} ano(s)', end='')
print(f'a prestação será de R${valPrest:.2f}')

if valPrest <= minSal:
    print(
        f'Empréstimo aprovado!!! Você terá que pagar mensalmente R${valPrest:.2f}, durante {anos}, até completar o valor total do pagamento.')
else:
    print('Infelizmente o empréstimo não foi aprovado.')
