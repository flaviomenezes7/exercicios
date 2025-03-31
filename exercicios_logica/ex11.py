"""
11) Faça um programa que solicite um número e faça uma contagem regressiva até 0.

"""

def contagem_regressiva(numero):
    while numero >= 0:
        print(numero)
        numero -= 1
    print("A contagem regressiva terminou!")
    
    
if __name__ == "__main__":
    try:
        numero = int(input("Digite um número para iniciar a contagem regressiva: "))
        contagem_regressiva(numero)
    except ValueError:
        print("Por favor, insira um número inteiro válido.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        
        