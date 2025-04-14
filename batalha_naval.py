from random import randint
import os

def limpar_tela():
   # para mac e linux (aqui, os.name é 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # para Windows
      _ = os.system('cls')

letras_para_numeros = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
print('Bem-vindo ao Batalha Naval')
print('Digite a letra r para reiniciar o jogo')
print('Digite a letra v para mostrar o seu tabuleiro')
print('Digite a letra m para mostrar o menu')

# porta-aviões ocupa 5 casas - 1
# navio tanque ocupa 4 - 2
# contra-torpedeiros ocupa 3 - 3
# submarinos ocupam 2 - 4

tamanhos_navios = {"NT": 4, "CT": 3, "SUB": 2, "PA": 5}

def imprimir_tabuleiro(tabuleiro):
    print('  A B C D E F G H')
    print('                 ')
    numero_linha = 1
    for linha in tabuleiro:
        print("%d %s" % (numero_linha, " ".join(linha)))
        numero_linha += 1

# verifica se uma posição e orientação é válida para um navio dado
# orientação 0 é horizontal
def verificar_posicao_valida(linha, coluna, tabuleiro, tamanho_navio, orientacao=0):
    for i in range(tamanho_navio):
        if(linha > 7 or coluna > 7):
            return False
        if (tabuleiro[linha][coluna] == "X"):
                return False
        if (orientacao == 0):
            coluna += 1
        if (orientacao == 1):
            linha += 1
    return True

def preencher_navio_no_tabuleiro(tabuleiro, linha, coluna, orientacao, tamanho_navio):
    for i in range(tamanho_navio):
        tabuleiro[linha][coluna] = "X"
        if orientacao == 0:
            coluna += 1
        else:
            linha += 1
    return tabuleiro

def criar_navios(tabuleiro, lista_navios):
    while lista_navios:
        linha_navio, coluna_navio = randint(0, 7), randint(0, 7)
        navio = lista_navios.pop()
        orientacao = randint(0, 1)
        while not verificar_posicao_valida(linha_navio, coluna_navio, tabuleiro, tamanhos_navios[navio], orientacao):
            linha_navio, coluna_navio = randint(0, 7), randint(0, 7)
        tabuleiro = preencher_navio_no_tabuleiro(tabuleiro, linha_navio, coluna_navio, orientacao, tamanhos_navios[navio])
    return tabuleiro

def iniciar_jogo():
    TABULEIRO_OCULTO = [['~'] * 8 for x in range(8)]  # marcações do jogador 1
    TABULEIRO_ADVINHA = [['~'] * 8 for x in range(8)]  # tentativas do jogador 2
    TABULEIRO_ADVINHA1 = [['~'] * 8 for x in range(8)]
    TABULEIRO_OCULTO1 = [['~'] * 8 for x in range(8)]
    acertos_jogadores = [0, 0]
    navios = ["PA"] * 1
    navios.extend(["NT"] * 2)
    navios.extend(["CT"] * 3)
    navios.extend(["SUB"] * 4)
    navios2 = navios.copy()
    TABULEIRO_OCULTO = criar_navios(TABULEIRO_OCULTO, navios)
    TABULEIRO_OCULTO1 = criar_navios(TABULEIRO_OCULTO1, navios2)
    TURNO_JOGADOR1 = True
    return acertos_jogadores, TURNO_JOGADOR1, [TABULEIRO_OCULTO, TABULEIRO_OCULTO1], [TABULEIRO_ADVINHA, TABULEIRO_ADVINHA1]

def contar_navios_atingidos(tabuleiro):
    contador = 0
    for linha in tabuleiro:
        for coluna in linha:
            if coluna == 'X':
                contador += 1
    return contador

def verificar_comando(entrada_usuario, comandos):
    if entrada_usuario.upper() in comandos:
        return True
    
def receber_entrada(comandos):
    is_comando = False
    linha = input('Digite uma linha do navio (1-8): ')
    is_comando = verificar_comando(linha, comandos)
    if is_comando:
        return is_comando, linha.upper(), "-"
    while linha not in '12345678':
        print('Digite uma linha válida')
        linha = input('Digite uma linha do navio (1-8): ')
        is_comando = verificar_comando(linha, comandos)
        if is_comando:
            return is_comando, linha.upper(), "-"
    coluna = input('Digite uma coluna do navio (A-H): ').upper()
    is_comando = verificar_comando(coluna, comandos)
    if is_comando:
        return is_comando, coluna.upper(), "-"
    while coluna not in 'ABCDEFGH':
        print('Digite uma coluna válida')
        coluna = input('Digite uma coluna do navio (A-H): ').upper()
        is_comando = verificar_comando(coluna, comandos)
        if is_comando:
            return is_comando, coluna.upper(), "-"
    return is_comando, int(linha) - 1, letras_para_numeros[coluna]

def atualizar_tabuleiro_advinha(linha, coluna, tabuleiro, tabuleiro_advinha):
    acerto = False
    if (tabuleiro_advinha[linha][coluna] == "*" or tabuleiro_advinha[linha][coluna] == "X"):
        print("Desculpe, você já marcou essa posição antes.")
    elif (tabuleiro[linha][coluna] == "X"):
        acerto = True
        tabuleiro_advinha[linha][coluna] = "X"
        print("Parabéns, você acertou um navio!") 
    elif tabuleiro[linha][coluna] == "~":
        tabuleiro_advinha[linha][coluna] = "*"
        print('Desculpe, você errou.')
    return tabuleiro_advinha, acerto

def mostrar_menu():
    print('Digite a letra r para reiniciar o jogo')
    print('Digite a letra v para mostrar o seu tabuleiro')
    print('Digite a letra m para mostrar o menu')
    print('Digite a letra s para sair')
    
def processar_comando(comando, tabuleiro):
    if comando == "S":
        print("Saindo...")
    if comando == "V":
        imprimir_tabuleiro(tabuleiro)
    if comando == "M":
        mostrar_menu()
    if comando == "R":
        print("Reiniciando o jogo...")
