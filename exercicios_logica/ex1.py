"""
1) Escreva um programa contendo uma função que tenha como parâmetros de entrada dois números inteiros.
- A função deve executar a multiplicação dos dois números. -> OK
- A função deve ter type hints nas variáveis de entrada e no retorno. -> OK
- A função deve converter os números em inteiros caso não sejam. -> OK
- A função deve ter tratativa de erros caso os parâmetros não sejam números. -> OK
- A função deve retornar o resultado. -> OK
- Use if __name__ == "__main__" para executar a função. -> OK
"""

def multiplicacao(num1: int, num2: int) -> int:
    try: 
        return int(num1) * int(num2) 
    except: 
        return "Os números devem ser inteiros." 


if __name__ == "__main__":
    print(multiplicacao(10, 9))
    print(multiplicacao(5.5, '2'))
    print(multiplicacao('6', '3'))
    print(multiplicacao('a', 'z'))
    