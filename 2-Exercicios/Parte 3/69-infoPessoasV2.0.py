'''Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final mostre:
- Quantas pessoas tem mais de 18 anos.
- Quantos homens foram cadastrados.
- Quantas mulheres tem menos de 20 anos.'''

maior = hm = mlh = 0

while True:
    print('-'*10, 'Cadastro', '-'*10)

    i = int(input('Idade: '))

    while True:
        s = str(input('Sexo: [M/F] ')).upper().strip()[0]
        if s in ('MF'):
            break

    while True:
        cont = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        if cont in ('SN'):
            break

    if i > 18:
        maior += 1

    if s == 'M':
        hm += 1

    if s == 'F' and i < 20:
        mlh += 1

    if cont == 'N':
        break

print('-'*10, 'Fim do cadastro', '-'*10)
print(f'Foram cadastrados {maior} pessoas maiores de idade.')
print(f'Foram cadastrados {hm} homens')
print(f'Foram cadastradas {mlh} mulheres com menos de 20 anos')
