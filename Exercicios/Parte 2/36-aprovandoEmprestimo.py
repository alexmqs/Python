'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
'''
valCasa = float(input('Qual o valor da casa? '))
salCom = float(input('Qual o salário do comprador? '))
anos = int(input('Em quantos anos deseja pagar?'))
valPrest = valCasa / anos
minSal = salCom * 30 / 100

if valPrest < minSal:
    print(
        f'Empréstimo aprovado!!! Você terá que pagar mensalmente R${valPrest:.2f}, durante {anos}, até completar o valor total do pagamento.')
else:
    print('Infelizmente o empréstimo não foi aprovado.')
