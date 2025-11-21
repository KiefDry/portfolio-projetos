# Jogo da Forca 🎯:

Um script de linha de comando (CLI) em Python que implementa o clássico jogo da Forca.

O programa seleciona aleatoriamente uma palavra secreta de uma lista predefinida. O usuário deve então adivinhar a palavra letra por letra, com um limite de 6 tentativas incorretas.

<br>

### ✨ Funcionalidades em Destaque

* **Seleção Aleatória de Palavras:** Utiliza `random.choice` para sortear uma palavra secreta da lista.
* **Limite de Tentativas:** O jogador tem 6 "chances" (tentativas incorretas) antes de perder o jogo.
* **Exibição da Palavra:** Mostra o progresso da palavra com *underscores* (`_ `), que são substituídos pelas letras corretas.
* **Rastreamento de Letras Usadas:** Exibe uma lista de todas as letras que o usuário já tentou.
* **Validação de Entrada:** Garante que o usuário digite apenas uma única letra por vez.
* **Loop "Jogar Novamente":** Ao final de cada partida (vitória ou derrota), o usuário pode escolher jogar novamente [s/n], o que reinicia o jogo.

<br>

### 🛠️ Tecnologias Utilizadas

* **Python:** Linguagem principal.
* **Módulo `random` (choice):** Para a seleção aleatória da palavra.
* **Módulo `os`:** Para limpeza do console (`cls`).
* **Módulo `time`:** Para pausas (`sleep`).

<br>

### ⚙️ Instalação e Execução

Este projeto utiliza apenas módulos nativos do Python.

1.  **Clone o Repositório:**
    ```bash
    git clone [https://github.com/KiefDry/jogo_da_forca.git](https://github.com/KiefDry/jogo_da_forca.git)
    cd jogo_da_forca
    ```

2.  **Execute o Script:**
    ```bash
    python main.py
    ```
    O jogo começará imediatamente, solicitando a primeira letra.