'''
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
'''

fichaAlunos = []
principal = []
alunos = []
notas = []

print('-='*40)
print(f"{'BOLETIM':^40}")
print('-='*40)

while True:
    n = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    m = (n1 + n2) / 2

    fichaAlunos.append([n, [n1, n2], m])
    '''alunos.append(n)
    notas.append(n1)
    notas.append(n2)
    alunos.append(notas[:])
    alunos.append(m)
    principal.append(alunos[:])
    notas.clear()
    alunos.clear()
    print(principal)'''

    while True:
        p = str(input('Quer continuar, sim ou não? ')).strip().upper()[0]

        if p in 'SN':
            break
        else:
            print('Digite sim ou não')

    if p == 'N':
        print('Saindo do cadastro...')
        print(f'-='*40)
        break
    else:
        print('Continuando...')

print(fichaAlunos)
print(f'{"Nº":<4}{"NOME":<10}{"MEDIA":>8}')
for i in fichaAlunos:
    print(f'{fichaAlunos.index(i):<4}{i[0]:<10}{i[2]:>8.1f}')

print(f'-='*40)

while True:
    p2 = int(input(f'Mostrar notas de qual aluno? (999 interrompe)'))
    if p2 == 999:
        print('Saindo...')
        break
    if p2 <= len(fichaAlunos) - 1:
        print(f'Notas de {fichaAlunos[p2][0]} são {fichaAlunos[p2][1]}.')
        print(f'-='*40)
print(f'-='*5, 'VOLTE SEMPRE', '-='*5)
