# print("*********************************")
# print("bem vindo ao jogo de adivinhação!")
# print("*********************************")

# numero_secreto = 23

# while True:
#     chute = input("Digite o seu número: ")
#     print("Você digitou", chute)

#     if int(chute) == numero_secreto:
#         print("Parabéns, você acertou!")
#     else:
#         print("Você errou, tente novamente!")

#     continuar = input("Deseja continuar jogando? (s/n): ")
#     if continuar.lower() != "s":
#         break

# print("Fim do jogo")
import random

def jogar():
    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    rodada = 1
    pontos = 100

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Escolha o nivel de dificuldade: "))
    if (nivel == 1):
        total_de_tentativas = 4
    elif (nivel == 2):
        total_de_tentativas = 3
    else:
        total_de_tentativas = 2

    nivel = int(input("Defina o nível: "))

    while(rodada <= total_de_tentativas):
        print("tentativa {} de {}".format (rodada,total_de_tentativas))
        chute= int(input("Qual é o seu numero?"))
        print("você digitou", chute)

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Parabens, está correto!")
            break
        else:
            if(maior):
                print("Você errou, o numero digitado é maior que o número secreto")
            elif(menor):
                print("Você errou, o numero digitado é menor que o número secreto")
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos

        rodada = rodada + 1

    print ("O numero correto era {}, você fez {} pontos. Fim do jogo".format(numero_secreto, pontos))

if(__name__ == "__main__"):
    jogar()