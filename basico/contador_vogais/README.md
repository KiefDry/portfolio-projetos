# Contador de Vogais 🔡:

Um script de linha de comando (CLI) simples em Python que conta o número de ocorrências de cada vogal (A, E, I, O, U) em uma frase fornecida pelo usuário.

Para garantir uma contagem precisa e *case-insensitive*, o script primeiro **converte toda a frase para minúsculas** e remove espaços em branco desnecessários do início e do fim (`.lower().strip()`).

<br>

### ✨ Funcionalidades em Destaque

* **Contagem Individual:** Analisa a frase e informa quantas vezes cada vogal (`a`, `e`, `i`, `o`, `u`) apareceu.
* **Ignora Maiúsculas/Minúsculas:** O processo de contagem não diferencia maiúsculas de minúsculas.
* **Relatório Claro:** Exibe um relatório simples e formatado com a contagem de cada vogal.
* **Interface Limpa:** Utiliza `os.system('cls')` para limpar o terminal após a entrada de dados.

<br>

### 🛠️ Tecnologias Utilizadas

* **Python:** Linguagem principal do projeto.
* **Módulo `os`:** Utilizado para a limpeza do console.

<br>

### ⚙️ Instalação e Execução

Este projeto utiliza apenas módulos nativos do Python, não sendo necessária a instalação de dependências externas.

1.  **Clone o Repositório:**
    ```bash
    git clone [https://github.com/KiefDry/contador_de_vogais.git](https://github.com/KiefDry/contador_de_vogais.git)
    cd contador_de_vogais
    ```

2.  **Execute o Script:**
    ```bash
    python main.py
    ```
    O programa solicitará que você digite uma frase e, em seguida, exibirá a contagem de cada vogal.