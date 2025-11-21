# PYTHON QUIZ 📖:

Um script de linha de comando (CLI) em Python que executa um quiz de conhecimentos gerais.

O programa apresenta um menu principal com opções para iniciar o quiz, ver um ranking (ainda não implementado) ou sair. O quiz em si é carregado a partir de um dicionário, onde cada pergunta tem suas opções e a resposta correta.

<br>

### ✨ Funcionalidades em Destaque

* **Banco de Perguntas:** As perguntas e respostas são armazenadas em um dicionário (`general_knowlegde`), facilitando a adição ou remoção de conteúdo.
* **Sistema de Pontuação:** O script rastreia o número de `acertos` e `erros` do usuário.
* **Classificação Final:** Ao final do quiz, o programa calcula uma pontuação total e atribui uma classificação ao usuário (Iniciante, Intermediário, Veterano).
* **Menu de Navegação:** Utiliza `match...case` para um menu claro (Iniciar, Ranking, Sair).
* **Interface Limpa:** Utiliza `os.system('cls')` e `time.sleep()` para gerenciar o fluxo do console e limpar a tela.

<br>

### 🛠️ Tecnologias Utilizadas

* **Python:** Linguagem principal.
* **Módulo `os`:** Para limpeza do console.
* **Módulo `time`:** Para pausas (`sleep`).

<br>

### ⚙️ Instalação e Execução

Este projeto utiliza apenas módulos nativos do Python.

1.  **Clone o Repositório:**
    ```bash
    git clone [https://github.com/KiefDry/python_quiz.git](https://github.com/KiefDry/python_quiz.git)
    cd python_quiz
    ```

2.  **Execute o Script:**
    ```bash
    python main.py
    ```
    O programa exibirá o menu principal. Escolha "[1] - Iniciar Quiz" para jogar.