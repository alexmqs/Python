# 11
# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta, pinta uma área de 2m².

larg = float(input('Valor da largura da parede: '))
alt = float(input('Valor da altura da parede: '))
area = larg * alt
quantTinta = area / 2

print(
    f'Sua parede tem dimensão de {larg}x{alt} e a área do local é {area}m² e a quantidade de tinta é {quantTinta}l para cada m²')
