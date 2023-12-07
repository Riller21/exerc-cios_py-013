# Importar reduce para aplicar a multiplicação entre os dados da lista
from functools import reduce

# Criar vetor
numeros = []

# Criar função para encontrar resultado multiplicação
def func_multiplicacao(x, y):
    return x * y

num_1 = int(input("Insira o primeiro número:"))
num_2 = int(input("Insira o segundo número:"))
num_3 = int(input("Insira o terceiro número:"))
num_4 = int(input("Insira o quarto número:"))
num_5 = int(input("Insira o quinto número:"))

numeros.extend([num_1, num_2, num_3, num_4, num_5])

soma = sum(numeros)
multiplicacao = reduce(func_multiplicacao, numeros)

print("Os número selecionados foram: ",numeros, "\n" "Soma: ", soma,"\n" "Multiplicação: ", multiplicacao)