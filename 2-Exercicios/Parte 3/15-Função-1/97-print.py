'''
Faça um programa que tenha uma função chamada escreva(),
que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
Ex:
escreva('Olá, Mundo!')
Saída:
~~~~~~~~~~~
Olá, Mundo!
~~~~~~~~~~~
'''


def escreva(frase):
    tam = len(frase)+4
    print(f'~'*tam)
    print(f'{frase:^{tam}} ')
    print(f'~'*tam)


f = str(input('Digite uma frase: '))
escreva(f)
