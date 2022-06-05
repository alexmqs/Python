'''
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.
'''

times = ('Internacional', 'Palmeiras', 'Cruz Alta', 'Brasíla', 'Chapecoense', 'Criciúma',
         'Curitiba', 'Caxias', 'Juventude', 'Vasco',  'Bragantino', 'Remo', 'Cruzeiro', 'Avaí', 'São Luiz', 'Novo Hamburgo', 'Santos', 'Vitória', 'Figueirense', 'Grêmio')
posicao = times.index('Chapecoense') + 1
print('='*30)
print(f'5 primeiros times: {times[0:5]}')
print('='*30)
print(f'Últimos 4 colocados: {times[-4:]}')
print('='*30)
print(f'Times em ordem alfabética: {sorted(times)}')
print('='*30)
print(f'Em que posição está o time da Chapecoense? {posicao}º lugar')
print('='*30)
