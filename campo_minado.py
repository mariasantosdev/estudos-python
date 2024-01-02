import random


def jogar():
    mensagem_boas_vindas()
    escolher_nivel_do_jogo()


def inicializa_tabuleiro(numero_de_linhas, numero_de_colunas):
    tabuleiro = [[0 for _ in range(numero_de_colunas)] for _ in range(numero_de_linhas)]

    total_posicoes = numero_de_linhas * numero_de_colunas

    print("A posição vai de 0 até " + str(total_posicoes))

    posicoes_das_minas = posicionando_as_minas_no_tabuleiro(numero_de_linhas, numero_de_colunas, total_posicoes)

    print("posicoes das minas " + str(posicoes_das_minas))
    quantidade_de_minas = len(posicoes_das_minas)

    for linha in tabuleiro:
        for i in range(len(linha)):
            linha[i] = "#"
    print("tabuleiro " + str(tabuleiro))

    while quantidade_de_minas != 0:
        posicao_chutada = int(input("Digite o número da posição que você gostaria de descobrir"))

        if posicao_chutada > total_posicoes:
            print("Por favor informe uma posição válida")
            continue
        elif posicao_chutada in posicoes_das_minas:
            print("posicao " + str(posicao_chutada) + " é uma mina! Fim de jogo")
        else:
            linha, coluna = divmod(posicao_chutada, numero_de_colunas)
            tabuleiro[linha][coluna] = "M"
            quantidade_de_minas -= 1
            print("posicao das minas " + str(quantidade_de_minas))
            print(tabuleiro)

def mensagem_boas_vindas():
    print("******************************")
    print("Bem vindo ao jogo Campo minado")
    print("******************************")


def escolher_nivel_do_jogo():
    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3)Difícil")
    nivel = int(input("Digite o número escolhido"))

    if nivel == 1:
        inicializa_tabuleiro(5, 5)
    elif nivel == 2:
        inicializa_tabuleiro(6, 6)
    elif nivel == 3:
        inicializa_tabuleiro(7, 7)
    else:
        print("Essa opção não é válida")


def posicionando_as_minas_no_tabuleiro(numero_de_linhas, numero_de_colunas, total_posicoes):
    numero_de_posicoes_selecionadas = int(0.2 * total_posicoes)
    posicoes_selecionadas = random.sample(range(numero_de_linhas * numero_de_colunas), numero_de_posicoes_selecionadas)
    return posicoes_selecionadas


if __name__ == "__main__":
    jogar()
