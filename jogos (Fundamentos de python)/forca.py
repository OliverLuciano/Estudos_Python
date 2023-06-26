import random


def jogar ():

    imprime_mensagem()
    palavra_secreta = gerador_palavra()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False 
    erros = 0

    while (not enforcou and not acertou):
        print(letras_acertadas)
        chute = input("Qual letra: ").strip().lower()
        
        if (chute not in palavra_secreta):
            print("errou tentei novamente")
            erros += 1
        else:
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = chute
                index += 1 

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas

    if(acertou):
        print(f"Você venceu e a palavra secreta é {palavra_secreta}")
    else:
        print(f"Você perdeu e a palavra secreta é {palavra_secreta}")
    print("Fim de jogo")

def imprime_mensagem():
    print("*************************************************")
    print("********Bem vindo ao jogo da Forca***************")
    print("*************************************************")

def gerador_palavra():

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()   
        palavras.append(linha) 

    arquivo.close()
    numero = random.randrange(0, len(palavras))

    palavra = palavras[numero]

    return palavra

if(__name__ == "__main__"):
    jogar()