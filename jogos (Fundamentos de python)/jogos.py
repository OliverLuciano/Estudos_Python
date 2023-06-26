import forca
import adivinhacao

print("**********************************************************")
print("*****************Escolha um jogo**************************")
print("**********************************************************")
print("Forca (1) Adivinhação (2)")
jogo = int(input("Dgite o código do jogo: "))

if (jogo == 1):
    forca.jogar()
elif(jogo == 2):
    adivinhacao.jogar()
else:
    print("Opção invalida!")