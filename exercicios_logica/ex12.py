"""
12) Soma de números
Peça ao usuário para inserir números até que ele digite -1. No final, exiba a soma de todos os números digitados.

"""
soma = 0  

while True:  # inicia um loop infinito
        try:
            numero = int(input("Digite um número (-1 para sair): "))  # Solicita ao usuário um número
            if numero == -1:  # se o número for -1, sai do loop
                break
            soma += numero  # adiciona o número à soma total
        except ValueError:  # trata o erro caso o usuário não digite um número válido
            print("Por favor, insira um número válido.")
print(f"A soma dos números digitados é: {soma}")  # exibe a soma total dos números digitados
    