# 📊 Fluxograma do Projeto: Jogo da Velha CLI

Este documento descreve o fluxo de execução lógica e tomada de decisões do algoritmo implementado no arquivo `jogo_da_velha.py`.

---

## 🔄 Diagrama de Fluxo (Mermaid)

```mermaid
flowchart TD
    A([Início do Program]) --> B[Solicitar Nome do Jogador 1]
    B --> C[Solicitar Nome do Jogador 2]
    C --> D[Sortear Jogador Inicial via random.choice]
    D --> E[Limpar Tela - os.system]
    E --> F[Exibir Tabuleiro Inicial com '☐']
    
    F --> G[Aguardar Jogada do Jogador Atual]
    G --> H[Digitar Coordenada ex: '1a', '2b']
    
    H --> I{Coordenada é Válida e Livre?}
    I -- Não --> J[Exibir 'Digite um formato válido!']
    J --> H
    
    I -- Sim --> K[Atualizar Tabuleiro com '✖' ou '◯']
    K --> L[Incrementar Número de Jogadas]
    
    L --> M{Verificar Se Houve Vencedor}
    M -- Sim --> N[Limpar Tela & Exibir Tabuleiro Final]
    N --> O[Anunciar Jogador Vencedor!]
    O --> Z([Fim da Partida])
    
    M -- Não --> P{Número de Jogadas > 7?}
    P -- Sim --> Q[Anunciar 'VELHA!!!']
    Q --> Z
    
    P -- Não --> R[Alternar Vez do Jogador]
    R --> E
