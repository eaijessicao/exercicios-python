nome = input("qual seu nome, meu nobre?")
idade = input("e a idade?")

if nome and idade :
    print (f'seu nome é {nome} e ele invertido  {nome[::-1]} e tem {len(nome)} letras. Além disso, a primeira letra do seu nome é {nome[0]} enquanto a ultima é {nome[-1]}')
    