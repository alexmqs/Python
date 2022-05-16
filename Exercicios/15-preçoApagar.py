# 15
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias que ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

kmPerc = float(input('Qual a quantidade de Km percorridos? '))
quantDiasAlug = float(input('Quantos dias o veículo foi alugado? '))
custoKm = float(input('Qual o valor do custo por Km? R$'))
custoTotalKm = kmPerc * custoKm
custoDia = float(input('Qual a diária do veículo? R$'))
custoTotalDia = custoDia * quantDiasAlug
valTotal = custoTotalKm + custoTotalDia

print(f'Você percorreu {kmPerc}Km por {quantDiasAlug:.2f} dia(s).')
print(
    f'O custo fixo por Km rodado é R${custoKm:.2f}, o custo total por Km é R${custoTotalKm:.2f}')
print(
    f'O custo fixo da diária é R${custoDia:.2f}, o custo total da diária é R${custoTotalDia:.2f}')
print(f'O valor total a ser pago é {valTotal:.2f}')
