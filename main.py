import random
def jogar():

        print("#############################")
        print("      Bem vindo ao jogo      ")
        print("#############################")
        arquivo = open("palavras.txt", "r")
        palavras = []
        for linha in arquivo:
            palavras.append(linha.strip())

        arquivo.close()

        numero_lista = random.randrange(0, len(palavras))

        palavra_secreta = palavras[numero_lista]
        lista_acertadas = ["_" for letra in palavra_secreta ]


        enforcou = False
        acertou = False
        erros = 0

        print(lista_acertadas)
        while not enforcou and not acertou:
            chute = input("Qual letra?").lower().strip()


            if chute in palavra_secreta:
                index = 0
                for letra in palavra_secreta:
                    if chute == letra:
                        print('encontrei a letra {} na posicao {}'.format(letra, index))
                        lista_acertadas[index] = chute
                    index = index +1

            else:
                erros += 1
            enforcou = erros == 6
            acertou = "_" not in lista_acertadas
            print(lista_acertadas)

        if(acertou):
            print("Você ganhou!")
        else:
            print("você perdeu")
        print("Fim do jogo.")


if __name__ == "__main__":
    jogar()


