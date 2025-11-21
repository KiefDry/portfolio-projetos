# Contador de Palavras e Ocorrências 📊:

Um script de linha de comando (CLI) em Python que analisa um texto fornecido pelo usuário.

O programa processa o texto para fornecer uma análise detalhada, focando em estatísticas simples de contagem. Para garantir uma contagem precisa, o script primeiro **converte todo o texto para minúsculas** e **remove pontuações comuns** (ex: `!`, `.`, `,`, `;`, `?`).

<br>

### ✨ Funcionalidades em Destaque

* **Limpeza de Texto:** Remove automaticamente a pontuação e padroniza o texto para minúsculas.
* **Contagem Total de Palavras:** Exibe o número total de palavras no texto processado.
* **Contagem Total de Letras:** Exibe o número total de caracteres alfabéticos (ignorando espaços).
* **Frequência de Ocorrência:** Lista cada palavra única encontrada no texto e mostra quantas vezes ela apareceu.
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
    git clone [https://github.com/KiefDry/contador_palavras.git](https://github.com/KiefDry/contador_palavras.git)
    cd contador_palavras
    ```

2.  **Execute o Script:**
    ```bash
    python main.py
    ```
    O programa solicitará que você digite o texto e, em seguida, exibirá a análise de contagem.