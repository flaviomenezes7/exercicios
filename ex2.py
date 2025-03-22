"""
Escreva um programa contendo uma função que receba uma lista de inteiros. 
Exemplo de entrada da função: [1, 2, 3, 4, 5, 6, 7, 8] 
- A função deve mostrar todos os números pares da lista. -> OK
- A função deve ter type hints nas variáveis de entrada. -> OK
- A função deve ter tratativa de erros caso o valor nao seja um número inteiro. -> OK
- Use if __name__ == "__main__" para executar a função. -> OK

"""
def numeros_pares(lista: list) -> list: 
    try:
        return [i for i in lista if i % 2 == 0]
    except ValueError:
        return "Os números devem ser inteiros."
    except Exception as e:
        return f"Erro: {e}"
    
if __name__ == "__main__":
    print(numeros_pares([1, 2, 3, 4, 5, 6, 7, 8]))
    print(numeros_pares([1, 2, 3, 4, 5, 6, 'a', 8]))
    print(numeros_pares([1, 2, 3, 4, 5, 6, 7, 'b']))
    print(numeros_pares([1, 2, 3, 4, 5, 6, 'c', 'd']))