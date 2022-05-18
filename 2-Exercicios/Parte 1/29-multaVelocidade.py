'''
Escreva um programa que leia a velocidade de um carro.
se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
a multa vai custar R$7,00 por cada Km acima do limite.
'''
# Código
vel = float(input('Velocidade do carro: '))
limite = 80
custo = 7
velAcima = vel - limite
multa = velAcima * custo

if vel > limite:
    print(f'Multado! Você vai pagar R${multa:.2f}')
else:
    print('Tenha um bom dia, dirija com cuidado!')

