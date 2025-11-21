# Sistema de Login com JSON 🔐:

Um script de linha de comando (CLI) em Python que simula um sistema de autenticação de usuários (Login e Registro).

O diferencial deste projeto é o uso da biblioteca **`json`** para a persistência de dados. Diferente de salvar em texto puro, o JSON permite armazenar a lista de usuários e senhas de forma estruturada, facilitando a leitura e a manipulação dos dados pelo programa.

<br>

### ✨ Funcionalidades em Destaque

* **Cadastro de Usuários:** Permite registrar novos usuários solicitando "nome" e "senha".
* **Persistência em JSON:** Os dados são salvos em um arquivo `login.json`. O script lê e escreve neste formato estruturado.
* **Sistema de Login:** Verifica se as credenciais inseridas correspondem a algum usuário salvo no banco de dados JSON.
* **Menu Interativo:** Interface clara com opções numéricas para navegar entre cadastro, login e saída.
* **Feedback Visual:** Mensagens de sucesso, erro ou carregamento com pausas estratégicas (`time.sleep`) para melhorar a experiência do usuário.

<br>

### 🛠️ Tecnologias Utilizadas

* **Python:** Linguagem principal.
* **Módulo `json`:** Para serialização (salvar) e desserialização (ler) dos dados dos usuários.
* **Módulo `os`:** Para limpeza do console (`cls`).
* **Módulo `time`:** Para pausas (`sleep`).

<br>

### ⚙️ Instalação e Execução

Este projeto utiliza apenas módulos nativos do Python.

1.  **Clone o Repositório:**
    ```bash
    git clone [https://github.com/KiefDry/sistema_de_login.git](https://github.com/KiefDry/sistema_de_login.git)
    cd sistema_de_login
    ```

2.  **Execute o Script:**
    ```bash
    python main.py
    ```
    O programa exibirá o menu principal. Ao cadastrar o primeiro usuário, o arquivo `login.json` será criado automaticamente na pasta.

<br>

### ⚠️ Nota de Segurança

Este projeto tem fins **educacionais**. As senhas são armazenadas em **texto simples** (plain text) dentro do arquivo JSON. Em um ambiente de produção real, senhas devem ser sempre criptografadas (hash) antes de serem salvas.