"""

3. Algoritmos Numéricos
Escreva uma função que receba um número inteiro e retorne True se for primo e False caso contrário.

"""

def numero_primo(num: int) -> int:
    if num <= 1:
        return False
    
    for i in range(2, num): # Verifica se o número é divisivel por qualquer outro número, começando do 2 até X
        if num % i == 0: # Se o resto da divisão do numero inserido pelo usuário der 0
            return False # Retorna falso
        
    return True # Retorna TRUE se não encontrar nenhum divisor.

print(numero_primo(1))
print(numero_primo(2))
print(numero_primo(11))