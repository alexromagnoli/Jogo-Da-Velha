# ❌⭕ Jogo da Velha em Python

Uma aplicação em **Python** que implementa o clássico **Jogo da Velha** para ser jogado via terminal por dois jogadores. O projeto utiliza lógica procedural, mapeamento por coordenadas em matriz ($3 \times 3$), sorteio aleatório de turnos e tratamento de erros de entrada de utilizador.

---

## 📋 Índice

- [📌 Visão Geral do Projeto](#-visão-geral-do-projeto)
- [🎮 Como Jogar](#-como-jogar)
- [⚙️ Funcionalidades e Regras](#️-funcionalidades-e-regras)
- [📐 Lógica e Estrutura do Código](#-lógica-e-estrutura-do-código)
- [📊 Diagrama de Fluxo (UML)](#-diagrama-de-fluxo-uml)
- [🛠️ Tecnologias Utilizadas](#️-tecnologias-utilizadas)
- [🚀 Como Executar o Projeto](#-como-executar-o-projeto)
- [🤝 Contribuição](#-contribuição)
- [📄 Licença](#-licença)

---

## 📌 Visão Geral do Projeto

O objetivo deste projeto é demonstrar a aplicação prática de conceitos fundamentais da programação em Python, incluindo:
- **Estruturas de Dados:** Uso de listas aninhadas e conjuntos (`sets`) para representação do tabuleiro e avaliação de subconjuntos de vitória.
- **Controle de Fluxo e Funções:** Modularização em funções com recursão para tratamento de entradas inválidas.
- **Experiência do Utilizador (CLI):** Limpeza de ecrã a cada turno para manter a visualização fluida e utilização de caracteres Unicode (`☐`, `✖`, `◯`).

---

## 🎮 Como Jogar

1. Ao iniciar o programa, são solicitados os nomes do **Jogador 1** e do **Jogador 2**.
2. O sistema sorteia aleatoriamente quem fará a primeira jogada.
3. O tabuleiro é exibido com um sistema de coordenadas:
   - **Linhas:** `1`, `2`, `3`
   - **Colunas:** `a`, `b`, `c`

```text
    A  B  C
1  ☐  ☐  ☐
2  ☐  ☐  ☐
3  ☐  ☐  ☐
