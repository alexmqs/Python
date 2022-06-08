'''
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
'''
# inicializando a variáveis
l = []
# add elemento na variável
ex = str(input('Digite uma expressão: ')).strip()
# estrutura de verificação
for s in ex:
    if s == '(':
        l.append('(')
    elif s == ')':
        if len(l) > 0:
            l.pop()
        else:
            l.append(')')
            break

# comparando elementos e retornando a resposta
if len(l) == 0:
    print('A expressão está correta!')
else:
    print('A expressão está incorreta!')
