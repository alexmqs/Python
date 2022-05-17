'''
Desenvolva uma lógica que leia peso e a altura de uma pessoa, calcule seu IMC e mostre se status, de acordo com a tabela abaixo:
- Abaixo de 18.55: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida
'''

p = float(input('Peso:'))
a = float(input('Altura:'))
imc = p/(a * a)

if imc < 18.55:
    print(f'Abaixo do peso, seu IMC: {imc}')
elif imc <= 25:
    print(f'Peso ideal, seu IMC: {imc}')
elif imc <= 30:
    print(f'Sobrepeso, seu IMC: {imc}')
elif imc <= 40:
    print(f'Obesidade mórbida, seu IMC: {imc}')
