'''
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao user se ele quer ou não continuar a digitar valores.
'''
c = 0
p = 'S'
soma = 0
maior = 0
menor = 0

while p in ('S'):
    # contador
    c += 1
    # captando os números
    n = int(input('Digite um número: '))
    # atribuindo maior e menor
    #menor = maior
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < maior:
            menor = n
    # soma
    soma += n
    p = str(input('Deseja continuar: [S/N] ')).upper()
media = soma/c
print(f'Média {media}')
print(f'Maior {maior}')
print(f'Menor {menor}')
