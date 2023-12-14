nome = str(input("qual teu nome, minha patroa? "))
idade = int(input("qual é a tua idade, minha nobre? "))
altura = float(input("como anda a vista ai embaixo? qual é tua altura? "))
peso = float(input("e esse buxinho ai? tu pesa quanto? "))
imc = peso / (altura ** 2) 

if imc <= 18.5 : {
    print ("O nome da pessoa é {}, possui {} anos, tem cerca de {} de altura e pesa {}kg. O imc dela é de {} Essa pessoa está querendo sumir do mapa de tão magra".format(nome,idade,altura,peso, imc))
}

elif imc >= 18.5 and imc <= 24.9 :{
    print ("O nome da pessoa é {}, possui {} anos, tem cerca de {} de altura e pesa {}kg. O imc dela é de {} Essa pessoa está no peso normal".format(nome,idade,altura,peso, imc))
}

elif imc >= 25 and imc <= 29.9 :{
    print ("O nome da pessoa é {}, possui {} anos, tem cerca de {} de altura e pesa {}kg. O imc dela é de {} Essa pessoa está rechuchunda".format(nome,idade,altura,peso, imc))
}

else: {
    print ("O nome da pessoa é {}, possui {} anos, tem cerca de {} de altura e pesa {}kg. O imc dela é de {} Essa pessoa é a thais carla".format(nome,idade,altura,peso, imc))
}




