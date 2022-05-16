# 10
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode compra.


valReal = float(input('Quanto dinheiro você tem na carteira R$: '))
valDolar = valReal / 4.96

print(f'Com R${valReal:.2f} você pode compra U${valDolar:.2f}')
