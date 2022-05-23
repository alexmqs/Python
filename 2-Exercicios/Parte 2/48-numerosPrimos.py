'''
Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
'''
r = 0
cont = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        r += c
        cont += 1


print(f'A soma dos {cont} números ímpares que são múltiplos de 3 é {r}')

n = int(input('Digite um número: '))

if n == 0 or n == 1:
    print('Erro! Digite um número maior que 1.')

elif n == 2 or n == 3:
    print('É um número primo')

else:
    if n % 2 == 0 or n % 3 == 0:
        print('Não é um número primo')
    else:
        print('É um número primo')
