import forca
import adivinhacao

print("*********************************")
print("*******Escolha o teu jogo********")
print("*********************************")



print("(1) forca (2) adivinhação")

jogo = int(input("Escolha o jogo "))

if(jogo == 1) :
    print("Você escolheu o jogo da forca. ")
    print("Iniciando...") 
    forca.jogar()    

elif(jogo == 2) :
    print("Você escolheu o jogo da Adivinhação ")
    print("Iniciando...")  
    adivinhacao.jogar()



print("Fim do jogo")