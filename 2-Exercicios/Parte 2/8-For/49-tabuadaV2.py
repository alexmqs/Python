'''
Refaça o desafio 09, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
'''
n = int(input('Digite um valor: '))
for c in range(1, 11):
    print(f'{n} X {c:2} = {(c*n)}')
