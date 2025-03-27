"""
2. Estruturas de Dados
Dado um dicionário { "a": 1, "b": 2, "c": 3 }, escreva uma função que retorne um novo dicionário invertido { 1: "a", 2: "b", 3: "c" }.

"""

dicionario = {"a": 1, "b": 2, "c": 3}

print(dicionario.items()) # É utilizado o items para produzir uma lista que seja possível iterar sobre utilizando o for
dicionario = {v: k for k, v in dicionario.items()}# Lendo ficaria assim: Valor e chave para chave e valor, ou seja, invertendo a chave pelo valor e o valor pela chave.   ( K = KEY | V =  VALUE )
print(dicionario)



