import random
import os

NIVEL_FACIL = 1
NIVEL_MEDIO = 2
NIVEL_DIFICIL = 3

def jogar():
    mensagem_boas_vindas()
    escolher_nivel_do_jogo()

def inicializa_tabuleiro(numero_de_linhas, numero_de_colunas):
    tabuleiro = [['#' for _ in range(numero_de_colunas)] for _ in range(numero_de_linhas)]
    total_posicoes = numero_de_linhas * numero_de_colunas

    print(f"A posição vai de 0 até {total_posicoes - 1}")

    posicoes_das_minas = sorted(posicionando_as_minas_no_tabuleiro(numero_de_linhas, numero_de_colunas, total_posicoes))
    print(f"Posições das minas: {posicoes_das_minas}")
    quantidade_de_minas = len(posicoes_das_minas)

    for linha in tabuleiro:
        for i in range(len(linha)):
            linha[i] = "#"
    mostrar_tabuleiro(tabuleiro)

    descobre_posicao_da_mina(numero_de_colunas, posicoes_das_minas, quantidade_de_minas, tabuleiro, total_posicoes)

def descobre_posicao_da_mina(numero_de_colunas, posicoes_das_minas, quantidade_de_minas, tabuleiro, total_posicoes):
    while quantidade_de_minas != 0:
        posicao_chutada = int(input("Digite o número da posição que você gostaria de descobrir: "))

        if posicao_chutada > total_posicoes:
            print("Por favor, informe uma posição válida.")
            continue
        elif posicao_chutada in posicoes_das_minas:
            print(f"Posição {posicao_chutada} é uma mina! Fim de jogo.")
            break
        else:
            linha, coluna = divmod(posicao_chutada, numero_de_colunas)
            tabuleiro[linha][coluna] = "M"
            mostrar_tabuleiro(tabuleiro)
            quantidade_de_minas -= 1

    if quantidade_de_minas == 0:
        print("Parabéns! Você ganhou o jogo.")
    else:
        if quantidade_de_minas > 1:
            print(f"Ainda faltam {quantidade_de_minas} minas.")
        else:
            print("Ainda falta 1 mina.")

def mostrar_tabuleiro(tabuleiro):
    print("Tabuleiro:")
    for linha in tabuleiro:
        print(" ".join(map(str, linha)))
    print()

def mensagem_boas_vindas():
    print("******************************")
    print("Bem-vindo ao jogo Campo Minado")
    print("******************************")

def escolher_nivel_do_jogo():
    print("Qual nível de dificuldade?")
    print(f"({NIVEL_FACIL}) Fácil  ({NIVEL_MEDIO}) Médio  ({NIVEL_DIFICIL}) Difícil")
    nivel = int(input("Digite o número escolhido: "))

    if nivel == 1:
        inicializa_tabuleiro(5, 5)
    elif nivel == 2:
        inicializa_tabuleiro(6, 6)
    elif nivel == 3:
        inicializa_tabuleiro(7, 7)
    else:
        print("Essa opção não é válida.")

def posicionando_as_minas_no_tabuleiro(numero_de_linhas, numero_de_colunas, total_posicoes):
    numero_de_posicoes_selecionadas = int(0.2 * total_posicoes)
    posicoes_selecionadas = random.sample(range(numero_de_linhas * numero_de_colunas), numero_de_posicoes_selecionadas)
    return posicoes_selecionadas

if __name__ == "__main__":
    jogar()
