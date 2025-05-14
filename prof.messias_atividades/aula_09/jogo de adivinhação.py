import random

def jogo_adivinhacao_simples():
    """
    Jogo de adivinhação onde o computador escolhe um número entre 1 e 100,
    e o usuário tenta adivinhar com dicas de "maior" ou "menor".
    """
    LIMITE_INFERIOR = 1
    LIMITE_SUPERIOR = 100

    numero_secreto = random.randint(LIMITE_INFERIOR, LIMITE_SUPERIOR)
    tentativas = 0
    acertou = False

    print("--- Bem-vindo ao Jogo de Adivinhação! ---")
    print(f"Eu pensei em um número entre {LIMITE_INFERIOR} e {LIMITE_SUPERIOR}. Tente adivinhar!")

    while not acertou:
        try:
            palpite_str = input("Qual o seu palpite? ")
            palpite = int(palpite_str)
            tentativas += 1

            if palpite < LIMITE_INFERIOR or palpite > LIMITE_SUPERIOR:
                print(f"Por favor, digite um número entre {LIMITE_INFERIOR} e {LIMITE_SUPERIOR}.")
                continue

            if palpite < numero_secreto:
                print("Muito baixo! Tente um número maior.")
            elif palpite > numero_secreto:
                print("Muito alto! Tente um número menor.")
            else:
                acertou = True
                print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas!")

        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}") # Para outros erros não previstos

if __name__ == "__main__":
    jogo_adivinhacao_simples()
