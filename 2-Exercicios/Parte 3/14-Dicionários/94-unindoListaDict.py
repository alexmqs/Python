'''
Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
'''
# declarando variáveis
dictcad = {}
listcad = []
# media idade e media final
mi = mf = 0
# fim declarando variáveis

# estrutura principal
while True:

    dictcad.clear()
    dictcad['nome'] = str(input('Nome: '))

    # atribuindo o valor do sexo
    while True:
        dictcad['sexo'] = str(input('Sexo: [M/F]')).upper().strip()[0]
        if dictcad['sexo'] in 'MF':
            break
        else:
            print('Masculino ou feminino...')
    # fim atribuindo o valor do sexo

    dictcad['idade'] = int(input('Idade: '))
    listcad.append(dictcad.copy())

    # pergunta
    while True:
        p = str(input('Deseja continuar? [S/N]')).upper().strip()[0]

        if p in 'SN':
            break
        else:
            print('Sim ou não...')
    if p == 'S':
        print('continuando...')
    else:
        print('saindo...')
        break
    # fim pergunta
# fim estrutura principal

print('=-='*30)

# quantas pessoas foram cadastradas
print(f'A) O grupo tem {len(listcad)} pessoas.')

# atribuindo a média de idade
for e in listcad:
    mi += listcad[listcad.index(e)]['idade']
mf = mi / len(listcad)

# exibindo a média de idade
print(f'B) A média de idade é {mf} anos.')

# mulheres cadastradas
print('C) As mulheres cadastradas foram: ', end='')
for e in listcad:
    if e['sexo'] == 'F':
        print(e['nome'], end=' ')
print()
# fim mulheres cadastradas

# lista de pessoas acima da média
print('D) Lista das pessoas que estão acima da média: ')
# masculino
for e in listcad:
    if e['idade'] >= mf and e['sexo'] == 'M':
        print('Masculino:')
        for k, v in e.items():
            print(f' {k} = {v}; ', end='')
print()
# feminino
for e in listcad:
    if e['idade'] >= mf and e['sexo'] == 'F':
        print('Feminino:')
        for k, v in e.items():
            print(f' {k} = {v}; ', end='')
# fim lista de pessoas acima da média
