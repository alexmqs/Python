'''
Melhore o desafio 61, perguntando para o user se ele quer mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.
'''
print('-'*10, 'Progressão aritmética V.3.0', '-'*10)
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))
termo = p
cont = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} ->', end='')
        termo += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais?'))
print('FIM')
print(f'Progressão finalizada com {total} termos mostrados')
