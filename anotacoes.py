# Built-in em Python se refere a módulos e funções que já estão incluídos na linguagem Python, ou seja, não é necessário instalar nenhum pacote adicional para utilizá-los. Alguns exemplos de módulos e funções built-in em Python são: Math, random, len(), print("")

#  usamos o parâmetro sep="_" para definir um _ entre cada valor, por isso é impresso. Definimos através do end para imprimir uma exclamação (!), seguida pelo \n. exemplo:

nome = "jessica"
sobrenome = "oliveira"
idade =  21 

print(nome, sobrenome, "tem", idade, sep="_", end="!\n")

# atráves da função type, é possivel descobrir o tipo daquela variavel (int, float, str, boolean)

# Em Python, "elif" é uma palavra-chave usada para criar uma estrutura condicional mais complexa, juntamente com as palavras-chave "if" e "else".

# "elif" é uma abreviação de "else if" e é usado para testar condições adicionais quando a condição do "if" não é atendida.

idade = int(input("Digite sua idade: "))

if idade < 18:
    print("Você é menor de idade.")
elif idade >= 18 and idade < 65:
    print("Você é um adulto.")
else:
    print("Você é um idoso.")


# o método format() é usado para formatar uma string. Ele substitui qualquer campo de substituição na string com o valor correspondente fornecido. Os campos de substituição são representados por chaves {} na string e podem conter um índice ou um nome opcional para especificar qual valor usar.

nome = "evinho"
idade = 24
minha_string = "Meu nome é {} e eu tenho {} anos.".format(nome, idade)
print(minha_string)


# o range retorna uma sequencia numerica no python, exemplo, range(inicio, fim, passo). a última posição do range é não-inclusiva, então se você digitasse for in range (1,9), ele retornaria até o 8.

# Exemplo 1: range com um argumento (fim)
for i in range(5):
    print(i)
    
# Saída: 0 1 2 3 4

# Exemplo 2: range com dois argumentos (inicio e fim)
for i in range(2, 8):
    print(i)

# Saída: 2 3 4 5 6 7

# Exemplo 3: range com três argumentos (inicio, fim e passo)
for i in range(0, 10, 2):
    print(i)

# Saída: 0 2 4 6 8

#  break é usado para sair completamente de um loop, enquanto continue é usado para pular uma iteração do loop.

# Loop através de uma lista de números
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number == 3:
        # Se o número for igual a 3, saia do loop
        break
    print(number)

# Saída: 1 2


# Loop através de uma lista de números
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number == 3:
        # Se o número for igual a 3, pule para a próxima iteração do loop
        continue
    print(number)

# Saída: 1 2 4 5


import random
random.random() * 100
58.30742817094118


# import random é uma declaração em Python que permite que o programa utilize a biblioteca de funções random.

# random.randrange(10) é uma função da biblioteca random que gera um número inteiro aleatório entre 0 e 9 (pois o argumento passado é 10).

import random

aleatorio = random.randrange(10)
print(aleatorio)

# A função random.seed(100) define a semente (seed) para o gerador de números aleatórios. Ao definir uma semente específica, você garante que os números aleatórios gerados sejam os mesmos em diferentes execuções do programa.

random.seed(100)

# Gera um número aleatório entre 0 e 1
num_aleatorio = random.random()

# Imprime o número gerado
print(num_aleatorio)