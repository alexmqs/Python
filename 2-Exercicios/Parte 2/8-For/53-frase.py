'''
Crie um programa que leia uma frase qualquer e diga se ela é um políndrono, desconsiderando os espaços.
'''
f = str(input('Digite uma frase: ')).strip().upper()
palavras = f.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('É um palíndromo!')

else:
    print('A frase digitada não é um palíndromo!')


''' Modo mais fácil
f = str(input('Digite uma frase: ')).upper().replace(' ', '')
r = f[::-1]

print(f'A frase digitada foi {f} o inverso dela é {r}')

if f == r:
    print('A frase é um políndrono.')
else:
    print('A frase não é um políndrono.')
'''
