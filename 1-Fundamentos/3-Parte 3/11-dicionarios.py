'''
Os dicionários são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura,
acessíveis por chaves literais.
'''
# declarando as variáveis
dicionario = {}
# ou
dicionario = dict()

# inicializando as variáveis
dicionario = {'nome': 'Alex', 'sexo': 'M', 'idade': 22}

# exibindo todo o dicionário
print(dicionario)

# exibindo determinado valores do dicionário
print(f"O {dicionario['nome']} tem {dicionario['idade']} anos de idade.")

# exibindo as chaves
print(dicionario.keys())

# exibindo os valore
print(dicionario.values())

# exibindo os itens
print(dicionario.items())

for chaves in dicionario.keys():
    print(chaves)

for valores in dicionario.values():
    print(valores)

for items in dicionario.items():
    print(items)

for chaves, valores in dicionario.items():
    print(f'{chaves} = {valores}')

#deletando determinado valor
del dicionario['sexo']

print(dicionario)

# alterando determinado valor
dicionario['nome'] = 'Bruno'

print(dicionario)

# adicionando items(chave, valor)
dicionario['peso'] = 78

print(dicionario)

# outro exemplo
brasil = []
estado1 = {'uf': 'Rio Grande do Sul', 'sigla': 'RS'}
estado2 = {'uf': 'Santa Catarina', 'sigla': 'SC'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil)
print(brasil[0])
print(brasil[0]['sigla'])

# outro exemplo
listaEstados = []
dicEstado = {}

for c in range(0, 3):
    dicEstado['uf'] = str(input('Unidade Federativa:'))
    dicEstado['sigla'] = str(input('Sigla do Estado:'))
    listaEstados.append(dicEstado.copy())

for lista in listaEstados:
    for valores in lista.values():
        print(valores)
    for chaves, valores in lista.items():
        print(f'{chaves} = {valores}')
