# 12
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

valProd = float(input('Valor do produto: R$'))
valQuantDesc = float(input('Quantos % de desconto: '))
valdesc = valProd * valQuantDesc / 100
descTotal = valProd - valdesc

print(
    f'Valor do produto: R${valProd:.2f}\nTotal com o desconto de {valQuantDesc}%(R${valdesc:.2f}) aplicado: R${descTotal:.2f}')
