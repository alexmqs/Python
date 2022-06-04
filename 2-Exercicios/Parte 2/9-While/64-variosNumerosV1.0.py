'''
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o user digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
'''
n = c = soma = 0
n = int(input('Digite um número: '))

while n != 999:
    soma += n
    c += 1
    n = int(input('Digite um número: '))


print('Acabou!')
print(f'Foram digitados {c} números e a soma é {soma}')
