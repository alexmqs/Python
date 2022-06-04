'''
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
Exemplo:
Digitite um número:1834
Unidade:4
Dezena:
Centena:8
Milhar:1
'''

'''código Fonte'''
numero = int(input('Digite um número: ')) #capturando a variável
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

'''exibindo resultado'''
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')

'''código Fonte'''
#numero = str(input('Digite um número: ')) #capturando a variável
#capturando = numero.split()

'''exibindo resultado'''
#print(f'Unidade: {numero[0][0]}')
#print(f'Dezena: {capturando[0][1]}')
#print(f'Centena: {capturando[0][2]}')
#print(f'Milhar: {capturando[0][3]}')
