# Gerador de Senhas 🔑:

Um script de linha de comando (CLI) em Python para a geração de senhas personalizadas.

O usuário pode definir o **comprimento desejado** da senha e **quais conjuntos de caracteres** devem ser utilizados na geração (letras maiúsculas, letras minúsculas, números e/ou símbolos).

<br>

### ✨ Funcionalidades em Destaque

* **Comprimento Personalizado:** O usuário define o tamanho da senha a ser gerada.
* **Seleção de Caracteres:** O usuário escolhe [S/N] se deseja incluir:
    * Letras Maiúsculas (`string.ascii_uppercase`)
    * Letras Minúsculas (`string.ascii_lowercase`)
    * Números (`string.digits`)
    * Símbolos (`string.punctuation`)
* **Loop Interativo:** Permite ao usuário gerar múltiplas senhas em uma única execução, perguntando se deseja continuar [s/n].
* **Tratamento de Erros:** Captura `ValueError` caso o usuário digite um valor não numérico para o tamanho da senha.
* **Interface Limpa:** Utiliza `os.system('cls')` e `time.sleep()` para gerenciar o fluxo do console e limpar a tela.

<br>

### 🛠️ Tecnologias Utilizadas

* **Python:** Linguagem principal.
* **Módulo `os`:** Para limpeza do console.
* **Módulo `string`:** Para as constantes de conjuntos de caracteres.
* **Módulo `random` (choice):** Para selecionar os caracteres aleatoriamente.
* **Módulo `time`:** Para pausas (`sleep`).

<br>

### ⚙️ Instalação e Execução

Este projeto utiliza apenas módulos nativos do Python.

1.  **Clone o Repositório:**
    ```bash
    git clone [https://github.com/KiefDry/gerador_de_senhas.git](https://github.com/KiefDry/gerador_de_senhas.git)
    cd gerador_de_senhas
    ```

2.  **Execute o Script:**
    ```bash
    python main.py
    ```
    O programa solicitará o tamanho da senha e as opções de caracteres.