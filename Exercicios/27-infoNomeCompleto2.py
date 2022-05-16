'''
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o útimo nome separadamente.
Exemplo:
Digite um nome: Ana Maria de Souza
Primeiro: Ana
Último: Souza
'''

'''código fonte'''
nomePessoa = str(input('Digite um nome: ')).strip()
dividindo = nomePessoa.split()
primeiroNome = dividindo[0]
segundoNome = dividindo[len(dividindo)-1]

'''exibindo resultados'''
print(f'Primeiro Nome: {primeiroNome}')
print(f'Segundo Nome: {segundoNome}')
print(dividindo)
