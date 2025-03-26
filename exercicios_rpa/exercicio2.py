"""
🚀 Desafio 1 - Números Múltiplos
Escreva um programa que receba um número inteiro N e calcule a soma de todos os múltiplos de 3 ou 5 menores que N.

"""

num1 = int(input("Digite um número inteiro N: "))
soma = 0 
for i in range(1, num1): # Para cada número de 1 até N
    if i % 3 == 0 or i % 5 == 0: # Se o número for múltiplo de 3 ou 5
        soma += i # Soma o número à variável 'soma' e passa para o próximo número
print(soma)



