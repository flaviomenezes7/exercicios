"""
Manipulação de Strings
Escreva uma função que receba uma string e retorne a mesma string invertida, sem usar funções prontas como [::-1].

Verifique se uma palavra é um palíndromo (ex: "radar" → True, "python" → False).

"""

def verificar_palindromo(texto):
    resultado = "" # Inicia uma variavel para armezenar
    for caractere in texto: # Faz um loop para iterar sobre cada caracter no texto
        resultado = caractere + resultado # Guarda o resultado (1 iteração: p  - 2 iteração: yp - 3 iteração: typ ....)
    if resultado == texto:
        return 'É um palindromo'
    else:
        return 'Não é um palindromo'


print(verificar_palindromo("radar"))
print(verificar_palindromo("flávio"))
print(verificar_palindromo("arara"))


