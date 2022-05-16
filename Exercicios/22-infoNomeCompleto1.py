'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas
- O nome com todas letras minúsculas
- Quantas letras ao todo(sem considerar espaços)
- Quantas letras tem o primeiro nome
'''
'''código fonte'''
nomeCompleto = str(input('Digite o nome completo: ')) # capturando o nome
letraMaior = nomeCompleto.upper() #transformando para letra maiúscula
letraMenor = nomeCompleto.lower() #transformando para letra minúscula
removendoEspaco1 = nomeCompleto.replace(' ', '') #removendo os espaços
quantasLetras = len(removendoEspaco1) #armazenando na variável a quantidade de letras
nomeLista = nomeCompleto.split() #transformando o nome em lista
quantasLetrasPrimeiro = len(nomeLista[0]) #armazenando na variável a quantidade de letras

'''exibindo resultado'''
print(f'Nome em letras maiúsculas: {letraMaior}')
print(f'Nome em letras minúsculas: {letraMenor}')
print(f'Todo nome tem {quantasLetras} letras.')
print(len(nomeCompleto) - nomeCompleto.count(' ')) #outra maneira contar removendo espaços
print(f'O primeiro nome tem {quantasLetrasPrimeiro} letras.')