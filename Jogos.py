import Forca
import adivinhacao

def escolha_jogo():
    print("*********************************")
    print("Seja bem-vindo! Escolha seu jogo:")
    print("*********************************")

    print("(1) Forca, (2) adivinhação")

    jogo = int(input("Qual jogo?"))

    if (jogo == 1):
        print("Jogo da forca!")
        Forca.jogar()
    elif (jogo == 2):
        print("Jogo de adivinhaçao!")
        adivinhacao.jogar()
if(__name__ == "__main__"):
    escolha_jogo()