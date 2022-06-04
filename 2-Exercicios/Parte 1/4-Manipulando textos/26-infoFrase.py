'''
Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra "A".
- Em que posição ela aparece a primeiravez.
- Em que posição ela aparece a última vez.
'''

'''código fonte'''
frase = str(input('Digite a frase: ')).strip().upper()
letra = 'A'
quantasX = frase.count(letra)
posicaoInicio = frase.find(letra)
posicaoFinal = frase.rfind(letra)

'''exindo resultado'''
print(f'Quantas letras {letra}: {quantasX}')
print(f'Posição inicial da letra {letra}: {posicaoInicio}')
print(f'Posição final da letra {letra}: {posicaoFinal}')
