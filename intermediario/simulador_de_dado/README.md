# Simulador de Dado (d6) 🎲:

Um script de linha de comando (CLI) em Python que simula o lançamento de um ou mais dados de seis faces (d6).

O programa pergunta ao usuário quantos dados ele gostaria de lançar e, em seguida, exibe o resultado individual de cada dado sorteado.

<br>

### ✨ Funcionalidades em Destaque

* **Múltiplos Lançamentos:** O usuário pode definir a quantidade de dados que deseja lançar em uma única jogada.
* **Resultado Individual:** Exibe o resultado de cada dado separadamente (ex: `Dado 1 → 4`, `Dado 2 → 6`).
* **Sorteio d6:** Utiliza `random.randint(1, 6)` para simular um dado de seis faces padrão.
* **Tratamento de Erros:** Valida a entrada do usuário para aceitar apenas números (`ValueError`) e para garantir que sejam números positivos maiores que 0.
* **Loop "Jogar Novamente":** Permite ao usuário realizar novos lançamentos [s/n] sem precisar reiniciar o script.
* **Interface Limpa:** Utiliza `os.system('cls')` e `time.sleep()` para gerenciar o fluxo do console.

<br>

### 🛠️ Tecnologias Utilizadas

* **Python:** Linguagem principal.
* **Módulo `random` (randint):** Para gerar o resultado do dado.
* **Módulo `os`:** Para limpeza do console (`cls`).
* **Módulo `time`:** Para pausas (`sleep`).

<br>

### ⚙️ Instalação e Execução

Este projeto utiliza apenas módulos nativos do Python.

1.  **Clone o Repositório:**
    ```bash
    git clone [https://github.com/KiefDry/simulador_de_dado.git](https://github.com/KiefDry/simulador_de_dado.git)
    cd simulador_de_dado
    ```

2.  **Execute o Script:**
    ```bash
    python main.py
    ```
    O programa perguntará quantos dados você deseja lançar.