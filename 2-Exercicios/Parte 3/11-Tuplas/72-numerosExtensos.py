'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,
de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''

tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
         'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    indice = int(input('Digite um número entre 0 e 20: '))
    if indice < 0 or indice > 20:
        print(f'Tente novamente.', end=' ')
    else:
        print(f'Você digitou o número {tupla[indice]}')
        continuar = str(input('Deseja continuar? ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'Saindo do programa...')
