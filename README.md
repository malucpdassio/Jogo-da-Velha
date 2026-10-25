# ❌ Jogo da Velha (Tic-Tac-Toe) em Python

Um clássico Jogo da Velha desenvolvido em **Python**, utilizando **Tkinter** para a construção da interface gráfica (GUI) e **Pygame** para o gerenciamento de áudio, efeitos sonoros imersivos e trilha sonora em loop sem interrupções.

---

## 🚀 Funcionalidades

- **Interface Gráfica Moderna:** Desenvolvida em Tkinter com design modularizado e paleta de cores personalizada.
- **Placar Dinâmico:** Conta e exibe em tempo real a pontuação acumulada do **Player 1 (X)** e do **Player 2 (O)**.
- **Sistema de Áudio Independente (Pygame Mixer):** 
  - Trilha sonora de fundo tocando em loop infinito.
  - Canais de áudio separados (`pygame.mixer.Channel`) para que os efeitos sonoros de clique e vitória não interrompam a música de fundo.
- **Arquitetura Modular:** Código limpo e separado entre lógica de jogo, interface de janelas,  gerenciamento de sons e gerenciamento de cores.

---

## 📂 Estrutura do Projeto

```text
Jogo-da-Velha/
│
├── core/
│   └── jogo.py         # Lógica principal do jogo, verificação de vitória e estado do tabuleiro
│
├── interface/
│   └── janela.py       # Configuração da janela principal, frames e elementos visuais (Tkinter)
│
├── config/
|   ├── cores.py
│   ├── sons.py         # Gerenciamento de áudio, canais do Pygame e carregamento de trilhas
│   └── sound/          # Pasta com os arquivos de áudio (.mp3 / .wav)
│       ├── trilha-sonora.mp3
│       ├── clique.wav
│       └── vencedor.mp3
│
└── main.py             # Ponto de entrada (Entry point) da aplicação