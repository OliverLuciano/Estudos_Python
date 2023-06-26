import random

def jogar(): 
    
    print("**********************************")
    print("*******Jogo de adivinhação********")
    print("**********************************")

    numero_selecionado = random.randrange(0,101)

    print("Selecione a dificuldade")
    dificuldade = int(input("(1) Fácil (2) Medio (3) Dificil: "))
    if(dificuldade == 1):
        numero_tentativas = 100
    elif(dificuldade == 2):
        numero_tentativas: 50
    elif(dificuldade == 3):
        numero_tentativas = 10

    for tentativas in range(numero_tentativas + 1):                    
        if(numero_tentativas == tentativas):
            print(f"Você perdeu o jogo, o número secreto era {numero_selecionado}")
            break

        valor = int(input("Digite um valor entre 0 e 100: "))
        if(valor > 100 or valor < 0):
            print("Número invalido!!")
            continue

        if(valor > numero_selecionado):
            print("O número escolhido é maior que o número secreto")
            print(f"Restam apenas {numero_tentativas - (tentativas + 1)}")
        elif(valor < numero_selecionado):
            print("O número escolhido é menor que o número secreto")
            print(f"Restam apenas {numero_tentativas - (tentativas + 1)}")
        elif(valor == numero_selecionado):
            print(f"Você acertou o numero secreto com apenas {tentativas}")
            break

if (__name__ == "__main__"):
    jogar()