'''
enquanto não '':
    se ''
        condição
    se ''
        condição
    se ''
        condição
condição sim

while not '':
    if ''
        condicao
    if ''
        condicao
    if ''
        condicao
true
'''

'''
for c in range(1, 10):
    print(c)
'''
c = 1
while c < 10:
    print(c)
    c += 1
print('Fim')

n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]')).upper()
print('Fim')

n = 1
p = i = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            p += 1
        else:
            i += 1
print(f'Você digitou {p} números pares e {i} números ímpares.')
