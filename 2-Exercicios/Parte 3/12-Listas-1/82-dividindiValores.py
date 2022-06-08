'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
'''
# iniciando variáveis
lc = []
lp = []
li = []

while True:
    # adicionando um elemento na lista
    lc.append(int(input('Digite um valor: ')))
    # estrutura da pergunta
    while True:
        p = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        # saindo
        if p in 'SN':
            break
        else:
            print('Somente Sim ou Não')
    # saindo
    if p == 'N':
        print('Saindo...')
        break
    # continuando
    else:
        print('Continuando...')
# estrutura de verificar e adicionar elementos par ou ímpar
for i in range(len(lc)):
    print(lc[i])
    if lc[i] % 2 == 0:
        lp.append(lc[i])
    else:
        li.append(lc[i])
# exibindo resultados
print(f'Lista completa é: {lc}')
print(f'Lista com números pares: {lp}')
print(f'Lista com números ímpares: {li}')
