'''
Crie um programa que lei o nome de uma pessoa e diga se ela tem "Silva" no seu nome.
'''

'''código fonte'''
nomePessoa = str(input('Digite o nome: ')).replace(' ', '').upper()
testando = 'SILVA' in nomePessoa

'''exibindo resultado'''
print(f'{testando}')
