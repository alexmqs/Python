'''
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas. 
'''

# código
dis = float(input('Distância da viagem? '))
print(f'Km da viagem: {dis}Km')
precoMin = 0.50 * dis
precoMax = 0.45 * dis

if dis <= 200:
    print(f'Valor da passagem R${precoMin:.2f}')
else:
    print(f'Valor da passagem R${precoMax:.2f}')