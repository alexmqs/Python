'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
-A média de idade do grupo.
-Qual é o nome do homem mais velho.
-Quantas mulheres têm menos de 20 anos.
'''

somaIdade = 0
mediaIdade = 0
idadeVelho = 0
nomeVelho = ''
totMulher20 = 0
for c in range(1, 5):
    print(f'---Cadastro da {c}ª pessoa---')
    nome = str(input('Digite o nome da pessoa: '))
    idade = int(input('Digite a idade da pessoa: '))
    sexo = str(input('Digite o sexo da pessoa [M/F]: '))
    somaIdade += idade
    if c == 1 and sexo in 'Mm':
        idadeVelho = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > idadeVelho:
        idadeVelho = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        totMulher20 += 1

mediaIdade = somaIdade / 4
print(f'A média de idade é: {mediaIdade}')
print(f'O homem mais velho tem {idadeVelho} anos e se chama {nomeVelho}.')
print(f'Ao todo são {totMulher20} mulheres com menos de 20 anos')

'''
media = 0
menos20 = 0
for c in range(1, 6):
    if c == 1:
        print(f'---Cadastro da {c}ª pessoa---')
        nomea = str(input('Digite o nome da pessoa: '))
        idadea = int(input('Digite a idade da pessoa: '))
        print('No sexo da pessoa digite, F para Feminino e M para masculino.')
        sexoa = str(input('Digite o sexo da pessoa: '))
        if idadea < 20 and sexoa == 'f' or sexoa == 'F':
            menos20 += 1
            print(menos20)
    elif c == 2:
        print(f'---Cadastro da {c}ª pessoa---')
        nomeb = str(input('Digite o nome da pessoa: '))
        idadeb = int(input('Digite a idade da pessoa: '))
        print('No sexo da pessoa digite, F para Feminino e M para masculino.')
        sexob = str(input('Digite o sexo da pessoa: '))
        if idadeb < 20 and sexob == 'f' or sexoc == 'F':
            menos20 += 1
            print(menos20)
    elif c == 3:
        print(f'---Cadastro da {c}ª pessoa---')
        nomec = str(input('Digite o nome da pessoa: '))
        idadec = int(input('Digite a idade da pessoa: '))
        print('No sexo da pessoa digite, F para Feminino e M para masculino.')
        sexoc = str(input('Digite o sexo da pessoa: '))
        if idadec < 20 and sexoc == 'f' or sexoc == 'F':
            menos20 += 1
            print(menos20)
    elif c == 4:
        print(f'---Cadastro da {c}ª pessoa---')
        nomed = str(input('Digite o nome da pessoa: '))
        idaded = int(input('Digite a idade da pessoa: '))
        print('No sexo da pessoa digite, F para Feminino e M para masculino.')
        sexod = str(input('Digite o sexo da pessoa: '))
        if idaded < 20 and sexod == 'f' or sexod == 'F':
            menos20 += 1
            print(menos20)
    else:
        print(f'---Cadastro da {c}ª pessoa---')
        nomee = str(input('Digite o nome da pessoa: '))
        idadee = int(input('Digite a idade da pessoa: '))
        print('No sexo da pessoa digite, F para Feminino e M para masculino.')
        sexoe = str(input('Digite o sexo da pessoa: '))
        if idadee < 20 and sexoe == 'f' or sexoe == 'F':
            menos20 += 1
            print(menos20)


# Média de idade
media = (idadea + idadeb + idadec + idaded + idadee) / 5
print(f'A média de idade do grupo é {media}')

# Homem mais velho
if sexoa == 'm' or sexoa == 'M' and sexob == 'm' or sexob == 'M' and sexoc == 'm' or sexoc == 'M' and sexod == 'm' or sexod == 'M' and sexoe == 'm' or sexoe == 'M':
    # 1º
    if idadea > idadeb and idadea > idadec and idadea > idaded and idadea > idadee:
        print(
            f'O maior o homem mais velho é o {nomea}, ele tem {idadea}anos de idade.')
    # 2º
    elif idadeb > idadea and idadeb > idadec and idadeb > idaded and idadeb > idadee:
        print(
            f'O maior o homem mais velho é o {nomeb}, ele tem {idadeb}anos de idade.')
    # 3º
    elif idadec > idadea and idadec > idadeb and idadec > idaded and idadec > idadee:
        print(
            f'O maior o homem mais velho é o {nomec}, ele tem {idadec}anos de idade.')
    # 4º
    elif idaded > idadea and idaded > idadeb and idaded > idadec and idaded > idadee:
        print(
            f'O maior o homem mais velho é o {nomea}, ele tem {idadea}anos de idade.')
    # 5º
    elif idadee > idadea and idadee > idadeb and idadee > idadec and idadee > idaded:
        print(
            f'O maior o homem mais velho é o {nomea}, ele tem {idadea}anos de idade.')

else:
    if idadea < 20 or idadeb < 20 or idadec < 20 or idaded < 20 or idadee < 20:
        print(f'{menos20} ')
'''
