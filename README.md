# Batalha Naval em Python

Este projeto é uma implementação do jogo Batalha Naval para terminal, desenvolvida em Python. O sistema processa partidas locais em turnos alternados entre dois jogadores num tabuleiro padrão de 8x8.

## Funcionalidades

* **Geração Automática de Frota:** O algoritmo de inicialização distribui os navios aleatoriamente no tabuleiro de cada jogador, calculando orientações horizontais e verticais e prevenindo a sobreposição de peças em coordenadas ocupadas.
* **Sistema de Turnos:** A lógica de estado alterna o controle da rodada automaticamente caso o tiro caia na água (símbolo `*`)[cite: 11, 12]. Acertar um navio (marcado como `X`) concede ao jogador a vantagem de realizar um novo disparo consecutivo[cite: 11, 12].
* **Composição da Frota:** O mapa de cada jogador abriga estrategicamente as seguintes embarcações[cite: 11]:
  * 1 Porta-aviões (5 espaços)
  * 2 Navios-tanque (4 espaços)
  * 3 Contra-torpedeiros (3 espaços)
  * 4 Submarinos (2 espaços)
* **Condição de Vitória:** O laço de repetição mantém a partida ativa até que o limite de 30 acertos seja atingido por um dos lados, o que representa a destruição total da frota inimiga[cite: 12].

## Interação e Comandos

Para jogar, o usuário fornece as coordenadas de ataque divididas em entradas de Linha (de 1 a 8) e Coluna (de A a H)[cite: 11]. O código possui tratamento de erros para impedir inputs de strings vazias ou fora dos limites estabelecidos[cite: 11, 12].

Adicionalmente, o jogo aceita os seguintes comandos alfabéticos a qualquer instante[cite: 11, 12]:
* **`V` (Visualizar):** Imprime o tabuleiro oculto, revelando a localização exata das embarcações de defesa do jogador atual.
* **`R` (Reiniciar):** Zera completamente o placar, recriando novos mapas randômicos e reiniciando a partida.
* **`M` (Menu):** Exibe a lista de instruções de tela.
* **`S` (Sair):** Encerra e quebra a execução do programa em definitivo.

## Estrutura do Código

* **`batalha_naval.py`:** Cuida da lógica principal do jogo, como espalhar os navios pelo tabuleiro sem sobreposições, limpar a tela dependendo do seu sistema operacional (Windows, Mac ou Linux) e validar se as jogadas são válidas.
* **`main.py`:** É o arquivo que roda a partida de fato, gerenciando os turnos, faz com o que você digita no teclado com as ações do jogo e dá uma pausa  na tela entre uma jogada e outra.

## Como Executar

É necessário ter o Python 3 instalado no ambiente.

1. Faça o clone do repositório ou baixe os dois arquivos `.py` no mesmo diretório.
2. Abra o terminal (ou a interface do VS Code) e navegue até a pasta do jogo.
3. Inicie o sistema executando:
   ```bash
   python main.py
