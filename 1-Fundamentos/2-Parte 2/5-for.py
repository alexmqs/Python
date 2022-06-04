'''
Estrura de repetição for
'''

# oi 5x
for c in range(0, 6):
    print('oi')
print('fim ')

# 1 até 5
for c in range(0, 6):
    print(c)
print('fim ')

# regressivo
for c in range(6, 0, -1):
    print(c)
print('fim ')

# pulando 2 em 2
for c in range(0, 7, 2):
    print(c)
print('fim ')

# utilizando uma variável na contagem
n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('fim ')

# utilizando uma variável na contagem com algumas incrementações
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('Fim')

# lendo números 5x
for c in range(0, 6):
    n = int(input('Digite um número: '))
print('fim ')

# somando valores
s = 0
for c in range(0, 6):
    n = int(input('Digite um número: '))
    s += n
print(f'Soma dos números é {s}')
