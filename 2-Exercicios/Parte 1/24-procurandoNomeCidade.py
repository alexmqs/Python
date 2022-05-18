'''
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".
'''

'''código fonte'''
nomeCidade = str(input('Digite o nome da cidade: ')
                 ).replace(' ', '').capitalize()
dividindo = nomeCidade.split()
testando = 'Santo' in dividindo[0]

'''exibindo resultado'''
print(f'{dividindo}')
print(testando)

'''Outro modo'''
cidade = str(input('Digite o nome da cidade: ')).strip()
print(cidade[:5].upper() == 'SANTO')
