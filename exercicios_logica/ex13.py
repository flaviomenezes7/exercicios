"""
12. Números palíndromos
Peça ao usuário um número e verifique se ele é um palíndromo (lido igual de trás para frente).

"""

numero = input("Digite um número: ")

if numero == numero[::-1]: # Verifica se o número é igual ao seu reverso. O [::-1] inverte a string.
    # O operador de fatiamento [::-1] inverte a string, permitindo comparar o número original com sua versão invertida.
    print(f"{numero} é um palíndromo!")
else:
    print(f"{numero} NÃO é um palíndromo.")
