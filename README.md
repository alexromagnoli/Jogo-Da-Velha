<div align="center">

# ❌⭕ Jogo da Velha em Python

Uma implementação em **Python 3** do clássico Jogo da Velha para dois jogadores via terminal.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

![Status](https://img.shields.io/badge/Status-Em_Ajuste-yellow?style=for-the-badge)

![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

</div>

---

## 📌 Sobre o Projeto

Este projeto consiste numa aplicação de linha de comando (CLI) desenvolvida em **Python** para permitir que dois jogadores disputem partidas de Jogo da Velha no mesmo terminal.

O sistema conta com sorteio automático de quem inicia a partida, mapeamento de coordenadas dinâmico (`1a` a `3c`), tratamento de jogadas inválidas e limpeza automática do ecrã a cada turno.

---

## 🛠️ Tecnologias Utilizadas

* **[Python 3](https://www.python.org/):** Linguagem principal do projeto.
  
* **Módulo `random`:** Utilizado para sortear aleatoriamente qual jogador começa.

* **Módulo `os`:** Utilizado para limpar o ecrã do terminal a cada rodada (`cls`).

---

## 🎮 Como Jogar

1. Ao iniciar, digite os nomes dos dois jogadores.
2. O programa sorteará aleatoriamente quem fará a primeira jogada.
3. O tabuleiro é exibido com posições baseadas em coordenadas de linha (`1`, `2`, `3`) e coluna (`a`, `b`, `c`):

```text
    A  B  C
1  ☐  ☐  ☐
2  ☐  ☐  ☐
3  ☐  ☐  ☐
