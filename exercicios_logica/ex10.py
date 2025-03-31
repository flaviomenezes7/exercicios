"""
Algoritmos de Ordenação
Implemente o algoritmo de ordenação Bubble Sort sem usar métodos prontos como sort().

Implemente uma busca binária para encontrar um número em uma lista ordenada.

"""

def BubleSort(lista): # Função que recebe uma lista como parâmetro
    n = len(lista) # Armazena o tamanho da lista em uma variável n
    for i in range(n): # Faz um loop para iterar sobre a lista
        for j in range(0, n-i-1): # Faz um loop para iterar sobre a lista novamente, mas não inclui o último elemento já ordenado
            if lista[j] > lista[j+1]: # Se o elemento atual for maior que o próximo
                lista[j], lista[j+1] = lista[j+1], lista[j] # Troca os elementos de lugar
    return lista # Retorna a lista ordenada


