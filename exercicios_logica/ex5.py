"""
1) Escreva um programa contendo uma função que tenha como parâmetros de
entrada dois números inteiros.
- A função deve executar a multiplicação dos dois números.
- A função deve ter type hints nas variáveis de entrada e no retorno.
- A função deve converter os números em inteiros caso não sejam.
- A função deve ter tratativa de erros caso os parâmetros não sejam números.
- A função deve retornar o resultado.
- Use if __name__ == "__main__" para executar a função.

"""

def funcao_parametros(num1: int, num2: int) -> int:
    try:
        resultado = int(num1) * int(num2)
        print(resultado)
    except:
        print('String')
        
if __name__ == "__main__":
    funcao_parametros(2, 5)
    funcao_parametros('a', 'b')
    funcao_parametros(2.5, 10)