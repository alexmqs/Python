'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- À vista dinheiro/cheque: 10% de desconto
- À vista cartão: 5% de desconto
- em até 2x no cartão: Preço normal
- 3x ou mais no cartão: 20% de juros
'''
v = float(input('Digite o valor do produto: R$'))
print('Opções de pagamento:')
print('''
1 - À vista dinheiro/cheque: 10% de desconto
2 - À vista cartão: 5% de desconton
3 - 2x no cartão: Preço normal
4 - 3x ou mais no cartão: 20% de juros''')

o = int(input('Digite a opção de pagamento: '))
ad = v - (v * (10/100))
ac = v - (v * (5/100))
j = v + (v * (20/100))
d = v / 2

if o == 1:
    print(
        f'Sua conta no valor de R${v:.2f} teve desconto aplicado e o valor atualizado é R${ad:.2f}')
elif o == 2:
    print(
        f'Sua conta no valor de R${v:.2f} teve desconto aplicado e o valor atualizado é R${ac:.2f}')
elif o == 3:
    print(f'Valor a pagar será R${v:.2f} em 2x de R${d:.2f}, sem juros.')
elif o == 4:
    parc = int(input('Digite o valor das parcelas: '))
    if parc < 3:
        print('O mínimo de parcelas é em 3x')
    else:
        print(
            f'Sua conta no valor de R${v:.2f} teve acréscimo aplicado e o valor atualizado é R${j:.2f} em {parc}x de R${(j/parc):.2f}, com juros.')
else:
    print('Opção de pagamento que foi digitado não existe')
