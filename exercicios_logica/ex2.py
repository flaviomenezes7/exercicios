""""
2) Escreva um programa contendo uma função que receba uma lista de inteiros.
Exemplo de entrada da função: [1, 2, 3, 4, 5, 6, 7, 8]
- A função deve mostrar todos os números pares da lista.
- A função deve ter type hints nas variáveis de entrada.
- A função deve ter tratativa de erros caso o valor nao seja um número inteiro.
- Use if __name__ == "__main__" para executar a função.
[expressão for variável in iterável if condição] 
"""

def lista_de_inteiros(lista: list) -> list:
    try:
        return [i for i in lista if i % 2 == 0]
    except:
        return 'Números devem ser inteiros'
    
if __name__ == "__main__":
    print(lista_de_inteiros([1,2.5,3,4,5,6,7,8,9,10,11,12]))
    print(lista_de_inteiros(['a',2,3,4,5,6,7,8,9,10,'b','a']))
    print(lista_de_inteiros(['a','b','c','d',5,1,2,3,4,5,]))