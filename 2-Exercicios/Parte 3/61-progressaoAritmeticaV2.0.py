'''
Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
'''

'''
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))

for c in range(0, 10):
    if c == 0:
        print(f'{p}', end='->')
    else:
        p += r
        print(f'{p}', end='->')
'''
print('-'*10, 'Progressão aritmética V.2.0', '-'*10)
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))
c = p
decimo = p + (10 - 1) * r
print(decimo)
while c != decimo + r:
    print(f'{p} -> ', end='')
    c += r
    p += r

print(f'Acabou.')
