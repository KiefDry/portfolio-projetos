# Gerador De Contatos 📒:

Um script de linha de comando (CLI) em Python que funciona como uma agenda simples, permitindo ao usuário cadastrar novos contatos.

A principal funcionalidade deste projeto é a **persistência de dados**. Cada novo contato (composto por Nome, Telefone, E-mail e Cidade) é salvo permanentemente em um arquivo de texto chamado `contacts.txt` no modo "append" (anexar).

<br>

### ✨ Funcionalidades em Destaque

* **Persistência em Arquivo:** Salva todos os contatos gerados no arquivo `contacts.txt`, mantendo um histórico das entradas.
* **Formatação de Dados:**
    * Formata automaticamente o número de telefone no padrão `(DD)XXXXX...` no momento de salvar.
    * Utiliza `.title()` para capitalizar automaticamente os campos "Nome" e "Cidade".
* **Loop Interativo:** O script pergunta continuamente ao usuário se deseja criar um novo contato [s/n] ou sair do programa.
* **Interface Limpa:** Utiliza `os.system('cls')` e `time.sleep()` para gerenciar o fluxo do console e limpar a tela.

<br>

### 🛠️ Tecnologias Utilizadas

* **Python:** Linguagem principal.
* **Manipulação de Arquivos:** Uso de `with open("contacts.txt", "a")` para salvar dados.
* **Módulo `os`:** Para limpeza do console (`cls`).
* **Módulo `time`:** Para pausas (`sleep`).

<br>

### ⚙️ Instalação e Execução

Este projeto utiliza apenas módulos nativos do Python.

1.  **Clone o Repositório:**
    ```bash
    git clone [https://github.com/KiefDry/gerador_de_contatos.git](https://github.com/KiefDry/gerador_de_contatos.git)
    cd gerador_de_contatos
    ```

2.  **Execute o Script:**
    ```bash
    python main.py
    ```
    O programa perguntará se você deseja criar um novo contato. Após o preenchimento, o arquivo `contacts.txt` será criado ou atualizado na mesma pasta do script.