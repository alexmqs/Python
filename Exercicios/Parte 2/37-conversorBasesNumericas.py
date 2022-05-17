'''
Escreva um prograna que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
- 1 para binário
- 2 para octal
- 3 para hexadecimal
'''
print('Menu de escolha:')
e = int(input('1 - para binário\n2 - para octal\n3 - para hexadecimal\nSua opção? '))
n = int(input('Digite um numero: '))
b = bin(n).replace('0b', '')
o = oct(n).replace('0o', '')
h = hex(n).replace('0x', '')

if e == 1:
    print(f'{n} em binário é {b}')
elif e == 2:
    print(f'{n} em octal é {o}')
elif e == 3:
    print(f'{n} em hexadecimal é {h}')
else:
    print('O número digitado no menu de escolha não existe!!!')
