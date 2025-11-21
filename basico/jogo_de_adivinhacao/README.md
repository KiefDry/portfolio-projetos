# Jogo de Adivinhação 🔑:

Um script de linha de comando (CLI) em Python que implementa o clássico jogo "Adivinhe o Número".

O programa gera um número secreto aleatório (entre 0 e 100) e o usuário deve tentar adivinhá-lo. A cada palpite, o script informa se o número secreto é **"maior"** ou **"menor"** que o palpite inserido.

<br>

### ✨ Funcionalidades em Destaque

* **Geração Aleatória:** Utiliza `random.randint(0, 100)` para gerar um novo número secreto a cada jogo.
* **Dicas Interativas:** Guia o usuário a cada tentativa, informando se o número secreto é maior ou menor.
* **Contador de Tentativas:** Registra o número de palpites e exibe o total quando o usuário acerta.
* **Tratamento de Erros:** Captura `ValueError` caso o usuário digite algo que não seja um número inteiro.
* **Loop "Jogar Novamente":** Ao final de cada partida, o usuário pode escolher jogar novamente [s/n] sem precisar reiniciar o script.
* **Interface Limpa:** Utiliza `os.system('cls')` e `time.sleep()` para manter o console limpo e legível.

<br>

### 🛠️ Tecnologias Utilizadas

* **Python:** Linguagem principal.
* **Módulo `random` (randint):** Para gerar o número secreto.
* **Módulo `os`:** Para limpeza do console (`cls`).
* **Módulo `time`:** Para pausas (`sleep`).

<br>

### ⚙️ Instalação e Execução

Este projeto utiliza apenas módulos nativos do Python.

1.  **Clone o Repositório:**
    ```bash
    git clone [https://github.com/KiefDry/jogo_de_adivinhacao.git](https://github.com/KiefDry/jogo_de_adivinhacao.git)
    cd jogo_de_adivinhacao
    ```

2.  **Execute o Script:**
    ```bash
    python main.py
    ```
    O jogo começará, e você deverá adivinhar um número entre 0 e 100.