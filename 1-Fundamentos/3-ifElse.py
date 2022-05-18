# if carro.esquerda():
#   bloco verdadeiro
# else:
#   bloco negativo

# tempo=int(input('Quantos anos tem seu carro? '))
# if tempo <= 3:
#   print('carro novo')
# else:
#   print('carro velho')
# print('--FIM--')

# estrutura/condição simples
nome = str(input('Qual o seu nome? '))
if nome == 'Alex':
    print('Que lindo nome você tem!')
print(f'Bom dia, {nome}!')

# estrutura/condição composta
nome = str(input('Qual o seu nome? '))
if nome == 'Alex':
    print('Que lindo nome você tem!')
else:
    print('Seu nome é tão normal!')
print(f'Bom dia, {nome}!')

# outro exemplo
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print(f'A sua média foi: {m:.1f}')
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')

# estrutura simplificada
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print(f'A sua média foi: {m:.1f}')
print('PARABÉNS!' if m >= 6 else 'ESTUDE MAIS!')
