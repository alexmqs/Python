'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- À vista dinheiro/cheque: 10% de desconto
- À vista cartão: 5% de desconto
- em até 2x no cartão: Preço normal
- 3x ou mais no cartão: 20% de juros
'''
v = float(input('Digite o valor do produto: '))
print('Opções de pagamento:')
print('1 - À vista dinheiro/cheque: 10% de desconto\n2 - À vista cartão: 5% de desconton\n3 - em até 2x no cartão: Preço normal\n4 - 3x ou mais no cartão: 20% de juros')
o = int(input('Digite a opção de pagamento: '))
ad = v - (v * (10/100))
ac = v - (v * (5/100))
j = v + (v * (20/100))
d = v / 2
t = j / 3

if o == 1:
    print(f'Valor a pagar será R${ad}')
elif o == 2:
    print(f'Valor a pagar será R${ac}')
elif o == 3:
    print(f'Valor a pagar será R${v} em 2x de R${d}')
elif o == 4:
    print(f'Valor a pagar será R${j} em 3x de R${t}')
else:
    print('Opção de pagamento não existe')
