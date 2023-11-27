print("*********************************")
print("bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 23

while True:
    chute = input("Digite o seu número: ")
    print("Você digitou", chute)

    if int(chute) == numero_secreto:
        print("Parabéns, você acertou!")
    else:
        print("Você errou, tente novamente!")

    continuar = input("Deseja continuar jogando? (s/n): ")
    if continuar.lower() != "s":
        break

print("Fim do jogo")
