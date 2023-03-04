import random

print("Bem vindo ao jogo de adivinhação!")

numero_secreto = random.randrange(101)
print("Número secreto é:", numero_secreto)
total_de_tentativas = 0
rodada = 1
pontos = 1000

print("Qual o nível de dificuldade?")
print("Nível 1 = Fácil, Nível 2 = Médio, Nível 3 = Difícil")

nivel = int(input("Defina o nível:"))

if(nivel == 1):
    total_de_tentativas = 20
elif (nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 3

while (rodada <= total_de_tentativas):
    print("Tentativa {} de {}".format(rodada,total_de_tentativas))
    chute = input("Digite o seu número entre 1 e 100:")
    if(int(chute) < 1 or int(chute) > 100):
        print("Digite o seu número entre 1 e 100:")
        continue
    acertou = numero_secreto == int(chute)
    maior = int(chute) > numero_secreto
    menor = int(chute) < numero_secreto
    rodada = rodada + 1
    pontos_perdidos = numero_secreto - int(chute)
    pontos = pontos - pontos_perdidos
    if (acertou):
        print("Você acertou! Você fez {} pontos!!!".format(pontos))
        break
    else:
        if (maior):
            print("Você errou! O número digitado é maior do que o número secreto.")
            print("Você fez {} pontos!!!".format(pontos))
        elif (menor):
            print("Você errou! O número digitado é menor do que o número secreto.")
            print("Você fez {} pontos!!!".format(pontos))

print("Fim do jogo!")


