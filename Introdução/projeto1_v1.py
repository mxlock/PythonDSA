# Projeto 1 - Desenvolvimento de Game em linguagem em Python - V1

# Import
import random
from os import system,name

#Funçao para limar a tela da cada execuçao
def limpa_tela():

        # Windows
        if name == 'nt' : 
            _ = system('cls')

        # Mac ou Linux
        else: 
              _ = system('clear')

# Função
def game():
      
      limpa_tela()

      print("\nBem-vindo(a) ao jogo da forca!")
      print("Adivinha a palavra abaixo: \n")

      # Lista de palavras para o jogo
      palavras = ['banana' , 'abacate' , 'uva' , 'morango' , 'laranja' ]

      # Escolhe randomicamente uma das palavras
      palavra = random.choice(palavras)

# List comprehension
letras_descobertas = ['_' for letra in palavra]

# Número de chances
chances = 6

# Lista para as letras erradas
letras_erradas = []

# Loop enquanto número de chances for maior do que zero
while chances > 0:
      
    # Print
    print(" ".join(letras_descobertas))
    print("\nChances restantes: ", chances)
    print("Letras erradas:", " ".join(letras_erradas))

    # Tentativa
    tentativa = input ("\nDigite uma letra: ").lower()

    #Condicional
    if tentativa in palavra:
          index = 0
          for letra in palavra:
                if tentativa == letra:
                      letras_descobertas[index] = letra
                index += 1
    else:
        chances -= 1
        letras_erradas.append(tentativa)

    # Condicional
    if "_" not in letras_descobertas:
      print("\nVocê venceu, a palavra era: ", palavra)
      break

    # Condicional
    if "_" not in letras_descobertas:
      print("\nVocê perdeu, a palavra era: ", palavra)

# Bloco main
if __name__ == "__main__":
      game()
      print("\nParabéns, vc está aprendento python na DSA. ")
  