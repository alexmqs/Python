frase = 'Curso em Video Python'
print(frase[:5])
print(frase[15:])
print(len(frase)) # quantos caracteres
print(frase.count('o')) # quantas letras tem a palavra requisitada
print(frase.count('o', 0, 13)) 
print(frase.find('deo')) # posição/índice inicial da palavra pesquisada se a palavra que não existe, é retornado -1
print('Curso' in frase)
print(frase.replace('Python', 'Android'))
print(frase.upper())  # transforma todas letras ficam em maiúsculas
print(frase.lower())  # transforma todas letras ficam em minúsculas
print(frase.capitalize())  # transforma a 1ª letra em maiúscula
print(frase.title())  # transforma em maiúsculas as primeiras letras das palavras
print(frase.strip()) # remove os espaços iniciais e finais/extremidades
print(frase.rstrip()) # remove os espaços finais/direita
print(frase.lstrip()) # remove os espaços iniciais/esquerda
print(frase.split()) # cria uma nova lista, os espaços são eliminados
dividido = frase.split() # criando um obj
print(dividido[2][3]) #retorna a terceira letra do 2º índice dividido
inserindoCaracter = '-'.join(frase)
print(inserindoCaracter)
