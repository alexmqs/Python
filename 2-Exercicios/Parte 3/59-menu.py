'''
Crie um programa que leia dois valores e mostre um menu na tela:
[1]Somar
[2]Multiplicar
[3]Maior
[4]Novos números
[5]Sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
'''
from time import sleep

v1 = float(input('Digite o 1º valor: '))
v2 = float(input('Digite o 2º valor: '))

opcao = 0


while opcao != 5:
    print('''
    ---Menu---
    [1]Somar
    [2]Multiplicar
    [3]Maior
    [4]Novos números
    [5]Sair do programa
    ''')
    opcao = int(input('Digite a opção do menu: '))

    if opcao == 1:
        s = v1 + v2
        print(f'A soma dos valores {v1} e {v2} é igual a {s}.')
    elif opcao == 2:
        x = v1 * v2
        print(f'A multiplicação dos valores {v1} e {v2} é igual a {x}.')
    elif opcao == 3:
        if v1 > v2:
            print(f'O maior valor entre {v1} e {v2} é o {v1}.')
        elif v1 == v2:
            print(f'Os valores {v1} e {v2} são iguais.')
        else:
            print(f'O maior valor entre {v1} e {v2} é o {v2}.')
    elif opcao == 4:
        v1 = float(input('Digite o novo 1º valor: '))
        v2 = float(input('Digite o novo 2º valor: '))
    elif opcao == 5:
        print('Finalizando')
    else:
        print('Opção incorreta, digite novamente')
    print('='*30)
    sleep(2)

print('Você escolheu sair do programa!')
