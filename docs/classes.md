# 📐 Diagrama de Classes (Estrutura de Código)

Este documento descreve a organização das estruturas de dados, variáveis globais e funções que compõem o módulo `jogo_da_velha.py`.

---

## 📊 Diagrama de Classes / Módulo (Mermaid)

```mermaid
classDiagram
    class JogoDaVelhaModule {
        +list lista_de_coordenadas
        +list lista_ganhadora
        +list lista_de_jogadas_1
        +list lista_de_jogadas_2
        +list lista_total_de_jogadas
        +int numero_de_jogadas
        +str jogador_1
        +str jogador_2
        +str primeiro
        +str segundo
        +mostrar_tabuleiro() void
        +atualizar_tabuleiro(jogadas_1, jogadas_2, jogada) void
        +verificar_ganhador(lista_de_jogadas) bool
        +verificar_jogada(jogada) bool
        +jogada_1() bool
        +jogada_2() bool
        +limpar_tela() void
    }
