# Calculadora Básica em Python 🧮:

Um script de linha de comando (CLI) simples, interativo e robusto para realizar as quatro operações matemáticas básicas (soma, subtração, multiplicação e divisão).

O projeto foi desenvolvido com foco em uma interface de usuário limpa (limpando o console a cada etapa) e um tratamento de erros eficaz, utilizando a sintaxe moderna `match...case` do Python.

<br>

### ✨ Funcionalidades em Destaque

* **Operações Básicas:** Suporta Adição (`+`), Subtração (`-`), Multiplicação (`*`) e Divisão (`/`).
* **Tratamento de Erros:** Valida a entrada do usuário para aceitar apenas números (`ValueError`) e impede o *crash* em divisões por zero (`ZeroDivisionError`).
* **Loop Interativo:** Permite que o usuário realize múltiplos cálculos em sequência sem precisar reiniciar o script.
* **Interface Limpa:** Utiliza `os.system('cls')` para limpar o terminal, proporcionando uma experiência de usuário organizada.
* **Resultado Detalhado:** Exibe o resultado da operação mostrando a expressão completa (ex: `10 + 5 = 15`).

<br>

### 🛠️ Tecnologias Utilizadas

* **Python:** Linguagem principal do projeto.
* **Módulo `os`:** Utilizado para a limpeza do console.
* **Módulo `time`:** Utilizado para pausas (`sleep`) na exibição de mensagens.

<br>

### ⚙️ Instalação e Execução

Este projeto utiliza apenas módulos nativos do Python, não sendo necessária a instalação de dependências externas.

1.  **Clone o Repositório:**
    ```bash
    git clone [https://github.com/KiefDry/calculadora_simples.git](https://github.com/KiefDry/calculadora_simples.git)
    cd calculadora_simples
    ```

2.  **Execute o Script:**
    ```bash
    python main.py
    ```
    O programa solicitará o primeiro número, o segundo número e, em seguida, o operador desejado.