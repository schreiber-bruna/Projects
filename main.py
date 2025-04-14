from batalha_naval import iniciar_jogo, imprimir_tabuleiro, receber_entrada, atualizar_tabuleiro_advinha, limpar_tela, processar_comando
# Trabalho Final - Batalha Naval
# Bruna Schreiber Fernandes - dre: 121158217

def executar_jogo():
    comandos = ["R", "V", "M", "S"]
    acertos_jogadores, TURNO_JOGADOR1, tabuleiros_ocultos, tabuleiros_advinha = iniciar_jogo()

    imprimir_tabuleiro(tabuleiros_advinha[0])
    imprimir_tabuleiro(tabuleiros_advinha[1])
    
    while max(acertos_jogadores) < 30:
        mensagem = 'Turno do Jogador 1' if TURNO_JOGADOR1 else 'Turno do Jogador 2'
        print(mensagem)
        
        eh_comando, linha, coluna = receber_entrada(comandos)
        
        if eh_comando:
            processar_comando(linha, tabuleiros_advinha[TURNO_JOGADOR1])
            if linha == "R":
                acertos_jogadores, TURNO_JOGADOR1, tabuleiros_ocultos, tabuleiros_advinha = iniciar_jogo()
            if linha == "S":
                break
            else:
                continue
        else:
            tabuleiros_advinha[TURNO_JOGADOR1], acerto = atualizar_tabuleiro_advinha(
                linha,
                coluna,
                tabuleiros_ocultos[TURNO_JOGADOR1],
                tabuleiros_advinha[TURNO_JOGADOR1]
            )
            if acerto:
                acertos_jogadores[TURNO_JOGADOR1] += 1
            else:
                TURNO_JOGADOR1 = not TURNO_JOGADOR1
        
        print("Próximo turno")
        limpar_tela()

def main():
    executar_jogo()

if __name__ == '__main__':
    main()
