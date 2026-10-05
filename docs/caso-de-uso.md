# 📄 Especificação de Caso de Uso: Jogo da Velha CLI

## UC01 - Jogar Partida de Jogo da Velha

### 1. Descrição Sucinta
Permite que dois jogadores realizem uma partida completa de Jogo da Velha via terminal, desde o cadastro dos nomes e sorteio do jogador inicial até a definição de um vencedor ou empate (velha).

### 2. Atores
* **Jogador 1:** Primeiro participante cadastrado.
* **Jogador 2:** Segundo participante cadastrado.
* **Sistema (Python CLI):** Script executável que gerencia a lógica, sorteios, validações e renderização do tabuleiro.

### 3. Pré-condições
* Ter o ambiente de execução Python 3 instalado no computador.
* Ter permissão para execução de comandos no terminal.

### 4. Pós-condições
* O resultado da partida (vitória de um dos jogadores ou empate) é exibido na tela e o programa é finalizado.

---

### 5. Fluxo Principal

| Passo | Ação do Ator | Reação do Sistema |
| :---: | :--- | :--- |
| **1** | Executa o arquivo `jogo_da_velha.py` no terminal. | Exibe prompt solicitando o nome do Jogador 1. |
| **2** | Digita o nome do Jogador 1 e confirma. | Exibe prompt solicitando o nome do Jogador 2. |
| **3** | Digita o nome do Jogador 2 e confirma. | Sortear aleatoriamente qual jogador fará a primeira jogada. |
| **4** | - | Limpa a tela e exibe o tabuleiro inicial com posições vazias (`☐`). |
| **5** | O Jogador da vez informa a coordenada da sua jogada (ex: `1a`, `2b`, `3c`). | Chama a validação da jogada (`verificar_jogada`). |
| **6** | - | Atualiza o tabuleiro com o símbolo do jogador atual (`✖` para o 1º a jogar, `◯` para o 2º). |
| **7** | - | Verifica se a jogada resultou em vitória (`verificar_ganhador`). |
| **8** | - | Verifica se o número de jogadas resultou em empate. |
| **9** | - | Limpa a tela, reexibe o tabuleiro atualizado e alterna a vez para o próximo jogador. |
| **10**| Os atores repetem os passos **5 a 9** até atingir o fim de jogo. | Anuncia o resultado final (Vencedor ou Velha) e encerra o fluxo. |

---

### 6. Fluxos Alternativos

#### FA01: Ocorrência de Empate (Velha)
1. No passo **8** do Fluxo Principal, o sistema verifica que o número de jogadas válidas atingiu o limite sem haver um vencedor.
2. O sistema exibe a mensagem **"VELHA!!!"**.
3. A partida é encerrada.

---

### 7. Fluxos de Exceção

#### FE01: Coordenada em Formato Inválido ou Inexistente
1. No passo **5** do Fluxo Principal, o jogador digita um valor fora do padrão (ex: `4d`, `xyz`, `11`).
2. O sistema identifica a entrada inválida.
3. O sistema exibe a mensagem: *"Digite um formato válido!(numero/letra)"*.
4. O sistema solicita novamente a jogada para o **mesmo** jogador sem alterar o estado do tabuleiro.

#### FE02: Coordenada Já Ocupada
1. No passo **5** do Fluxo Principal, o jogador digita uma coordenada de uma célula que já contém `✖` ou `◯`.
2. O sistema identifica que a posição já está registrada no histórico de jogadas.
3. O sistema exibe a mensagem de erro e solicita que o jogador informe uma célula livre.

---

### 8. Diagrama do Caso de Uso (Mermaid)

```mermaid
graph TD
    J1[Jogador 1] --> UC1(Informar Nomes)
    J2[Jogador 2] --> UC1
    J1 --> UC2(Realizar Jogada - Coordenada)
    J2 --> UC2

    UC2 .-> UC3(Validar Jogada)
    UC3 .-> UC4(Verificar Vitória / Empate)
    UC4 --> SYS[Sistema Python]
    SYS --> UC5(Exibir Resultado Final)
