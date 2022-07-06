'''
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
'''
# declarando
mediaAlunos = {}

# inicializando variáveis
mediaAlunos['nome'] = str(input('Nome:'))
mediaAlunos['media'] = float(input(f'Média de {mediaAlunos["nome"]}: '))
if mediaAlunos['media'] >= 7:
    mediaAlunos['situacao'] = 'Aprovado'
elif mediaAlunos['media'] >= 5:
    mediaAlunos['situacao'] = 'Recuperação'
else:
    mediaAlunos['situacao'] = 'Reprovado'
# fim inicializando variáveis

print('-=-'*10)

# exibindo
for k, v in mediaAlunos.items():
    print(f'{k} é igual a {v}')
# fim exibindo
