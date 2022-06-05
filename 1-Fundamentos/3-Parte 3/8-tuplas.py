# tupla, mantém valores na variável, esses valores não podem ser trocados, ou seja, são imutáveis
lanche = ('hambúrguer', 'suco', 'pizza', 'pudim', 'batata frita')

# exibindo todos elementos da variável
print(lanche)

# exibindo todos elementos da variável, ordenados alfabeticamente
print(sorted(lanche))

# exibindo o índice 1
print(lanche[1])

# exibindo índice 1 e o 2
print(lanche[1:3])

# exibindo índice 2 até o último índice
print(lanche[2:])

# exibindo índice 0 até o índice 1
print(lanche[:2])

# exibindo índice 2 até o último índice
print(lanche[-2:])

# exibindo índice 1 até o último índice
print(lanche[-3:])

# exibindo em um for modo 1
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Eu comi pra caramba!')

# exibindo em um for modo 2, com posição dos lanches
for contador in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[contador]} na posição {contador}')
print('Eu comi pra caramba!')

# exibindo em um for modo 3, com posição dos lanches
for posicao, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {posicao}')
print('Eu comi pra caramba!')

# simulando erro, não é possível adicionar um valor para a tupla
lanche[1] = 'refrigerante'

# juntado tuplas
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)

# exibindo quantas vezes aparece um determinado elemento
print(c.count(5))

# exibindo o índice do elemento
print(c.index(5))

# exibindo o índice do elemento, escolhendo a partir de qual índice
print(c.index(5, 1))

# adicionando dados de tipos diferentes
pessoa = ('Alex Marques', 27, 'Masculino', 1.80)

# exibindo pessoa
print(pessoa)

# deletando a tupla
del(pessoa)

# simulando erro, não e possível deletar determindo índice
del(pessoa[0])
