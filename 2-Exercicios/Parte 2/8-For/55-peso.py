'''
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e menor peso lidos.
'''
maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(f'Peso da {c}ª pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior}Kg')
print(f'O maior peso lido foi de {menor}Kg')

'''
for c in range(1, 6):
    if c == 1:
        aa = float(input(f'Digite o {c}º peso: '))
    elif c == 2:
        bb = float(input(f'Digite o {c}º peso: '))
    elif c == 3:
        cc = float(input(f'Digite o {c}º peso: '))
    elif c == 4:
        dd = float(input(f'Digite o {c}º peso: '))
    else:
        ee = float(input(f'Digite o {c}º peso: '))

if aa == bb == cc == dd == ee:
    print('Todos os pesos são iguais')
else:
    # Maior
    # aa
    if aa >= bb and aa >= cc and aa >= dd and aa >= ee:
        print(f'O 1º peso é o maior que é {aa}Kg')
    # bb
    elif bb >= aa and bb >= cc and bb >= dd and bb >= ee:
        print(f'O 2º peso é o maior que é {bb}Kg')
    #   cc
    elif cc >= aa and cc >= bb and cc >= dd and bb >= ee:
        print(f'O 3º peso é o maior que é {cc}Kg')
    # dd
    elif dd >= aa and dd >= bb and dd >= cc and bb >= ee:
        print(f'O 4º peso é o maior que é {dd}Kg')
    # ee
    elif ee >= aa and ee >= bb and ee >= cc and ee >= dd:
        print(f'O 5º peso é o maior que é {ee}Kg')

    # Menor
    # aa
    if aa <= bb and aa <= cc and aa <= dd and aa <= ee:
        print(f'O 1º peso é o menor que é {aa}Kg')
    # bb
    elif bb <= aa and bb <= cc and bb <= dd and bb <= ee:
        print(f'O 2º peso é o menor que é {bb}Kg')
    # cc
    elif cc <= aa and cc <= bb and cc <= dd and cc <= ee:
        print(f'O 3º peso é o menor que é {cc}Kg')
    # dd
    elif dd <= aa and dd <= bb and dd <= cc and dd <= ee:
        print(f'O 4º peso é o menor que é {dd}Kg')
    # ee
    elif ee <= aa and ee <= bb and ee <= cc and ee <= dd:
        print(f'O 5º peso é o menor {ee}Kg')
'''
