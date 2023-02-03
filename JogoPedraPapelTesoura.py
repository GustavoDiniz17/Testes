#Jogo Pedra, Papel ou Tesoura
#Criado por : Gustavo Diniz 

import random 

print(" JOOGO PEDRA, PAPEL OU TESOURA")

a1 = "Pedra"
a2 ="Papel" 
a3 ="Tesoura"

escolhas_oponente = ["Pedra", "Papel", "Tesoura"]

oponente = random.choice(escolhas_oponente)

escolha = input("Digite 1 para Pedra, 2 para papel e 3 para tesoura")

if escolha == '1':
    print("Você escolheu", a1)

elif escolha == '2':
    print("Você escolheu", a2)

elif escolha == '3':
    print("Você escolheu", a3)

else:
    print("Você escolheu um numero invalido, por favor tente novamente.")

print("Seu oponente escolheu", oponente)

if escolha == '1' and oponente == "Pedra":
    print("Houve um empate")

elif escolha == '1' and oponente == "Papel":
    print("Você Perdeu !!!")

elif escolha == '1' and oponente == "Tesoura":
    print("Você ganhou !!!")

elif escolha == '2' and oponente == "Pedra":
    print("Você ganhou !!!")

elif escolha == '2' and oponente == "Papel":
    print("Houve um empate")

elif escolha == '2' and oponente == "Tesoura":
    print("Você perdeu !!!")

elif escolha == '3' and oponente == "Pedra":
    print("Você perdeu !!!")

elif escolha == '3' and oponente == "Papel":
    print("Você ganhou !!!")

elif escolha == '3' and oponente == "Tesoura":
    print("Houve um empate")

