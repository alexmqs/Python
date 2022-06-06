'''
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''
tupla = ('Circo', 'Caderno', 'Letra', 'Vida',
         'Amor', 'Dia', 'Noite', 'Passaro')

for item in tupla:
    print(f'\nA palavra {item.upper()}, tem as seguintes vogais: ', end='')
    for letra in item.upper():
        if letra in 'AEIOU':
            print(f'{letra} ', end='')
