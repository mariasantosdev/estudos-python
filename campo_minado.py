import random


def jogar():
    mensagem_boas_vindas()
    escolher_nivel_do_jogo()


# TODO aqui rola usar o conceito de parametros opcionais e com valores defaults
def inicializa_tabuleiro(numero_de_linhas, numero_de_colunas):
    tabuleiro = [[0 for _ in range(numero_de_colunas)] for _ in range(numero_de_linhas)]

    total_posicoes = numero_de_linhas * numero_de_colunas

    print("A posição vai de 0 até " + str(total_posicoes))

    posicoes_das_minas = posicionando_as_minas_no_tabuleiro(numero_de_linhas, numero_de_colunas, total_posicoes)

    print("posicoes das minas " + str(posicoes_das_minas))

    # TODO talvez colocar em posição de tabuleiro certinho
    for linha in tabuleiro:
        for i in range(len(linha)):
            linha[i] = "#"
    print("tabuleiro " + str(tabuleiro))

    posicao_chutada = int(input("Digite o número da posição que você gostaria de descobrir"))

    if posicao_chutada > total_posicoes:
        print("Por favor informe uma posição válida")
    elif posicao_chutada in posicoes_das_minas:
        print("posicao " + str(posicao_chutada) + " é uma mina! Fim de jogo")
    else:
        print("Posição chutada não é uma mina")


def contar_minas_adjacentes(tabuleiro, linha, coluna):
    total_linhas = len(tabuleiro)
    print(total_linhas)
    total_colunas = len(tabuleiro[0])
    print(total_colunas)
    contagem = 0

    for i in range(max(0, linha - 1), min(total_linhas, linha + 2)):
        for j in range(max(0, coluna - 1), min(total_colunas, coluna + 2)):
            if tabuleiro[i][j] == "M":
                contagem += 1

    return contagem


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


def posicionando_as_minas_no_tabuleiro(numero_de_linhas, numero_de_colunas, total_posicoes):
    numero_de_posicoes_selecionadas = int(0.2 * total_posicoes)
    posicoes_selecionadas = random.sample(range(numero_de_linhas * numero_de_colunas), numero_de_posicoes_selecionadas)
    return posicoes_selecionadas


if __name__ == "__main__":
    jogar()
