from batalha_naval_final import iniciar_jogo, imprimir_tabuleiro, receber_entrada, atualizar_tabuleiro_advinha, limpar_tela, processar_comando

def executar_jogo():
    comandos = ["R", "V", "M", "S"]
    acertos_jogadores, TURNO_JOGADOR1, tabuleiros_ocultos, tabuleiros_advinha = iniciar_jogo()
    
    while max(acertos_jogadores) < 30:
        limpar_tela()
        mensagem = 'Turno do Jogador 1' if TURNO_JOGADOR1 else 'Turno do Jogador 2'
        indice_jogador = 0 if TURNO_JOGADOR1 else 1
        indice_oponente = 1 if TURNO_JOGADOR1 else 0
        
        print(f"\n--- {mensagem} ---")
        print("Seu tabuleiro de tiros (Advinhação):")
        imprimir_tabuleiro(tabuleiros_advinha[indice_jogador])
        print(f"Acertos: {acertos_jogadores[indice_jogador]}")
        
        eh_comando, linha, coluna = receber_entrada(comandos)
        
        if eh_comando:
            if linha == "V":
                print("\n--- Seus Navios ---")
                processar_comando(linha, tabuleiros_ocultos[indice_jogador])
            else:
                processar_comando(linha, tabuleiros_advinha[indice_jogador])
                
            if linha == "R":
                acertos_jogadores, TURNO_JOGADOR1, tabuleiros_ocultos, tabuleiros_advinha = iniciar_jogo()
            if linha == "S":
                break
            else:
                input("\nPressione Enter para continuar...")
                continue
        else:
            tabuleiros_advinha[indice_jogador], acerto = atualizar_tabuleiro_advinha(
                linha,
                coluna,
                tabuleiros_ocultos[indice_oponente],
                tabuleiros_advinha[indice_jogador]
            )
            
            if acerto:
                acertos_jogadores[indice_jogador] += 1
            else:
                TURNO_JOGADOR1 = not TURNO_JOGADOR1
        
        input("\nPressione Enter para ir para o próximo turno...")

def main():
    executar_jogo()

if __name__ == '__main__':
    main()