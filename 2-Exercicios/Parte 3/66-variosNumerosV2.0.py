'''
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi o soma entre eles(Desconsiderando o flag)
'''
n = s = c = 0
while True:
    n = int(input('Digite um valor: (999 para parar )'))
    if n == 999:
        break
    else:
        s += n
        c += 1
print(f'Soma {s}')
print(f'Quantas números {c}')
