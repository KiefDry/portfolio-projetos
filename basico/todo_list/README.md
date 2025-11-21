# Lista de Tarefas (To-Do List) 📖:

Um script de linha de comando (CLI) em Python que funciona como um sistema de gerenciamento de tarefas (To-Do List).

O projeto é totalmente interativo e baseado em um menu de opções (1- Adicionar, 2- Ver, 3- Remover, 4- Sair), permitindo ao usuário gerenciar suas tarefas de forma eficiente.

<br>

### ✨ Funcionalidades em Destaque

* **Adicionar Tarefas:** Inclui validação para impedir que tarefas em branco ou tarefas **duplicadas** sejam adicionadas à lista.
* **Visualizar Tarefas:** Exibe todas as tarefas ativas em uma lista numerada (por índice), tratando também o caso de a lista estar vazia.
* **Remover Tarefas:** Permite ao usuário excluir uma tarefa específica informando seu **índice** numérico.
* **Tratamento de Erros Robusto:** O script lida com entradas inválidas, como tentar remover um índice não numérico (`ValueError`) ou um índice que não existe na lista (`IndexError`).
* **Interface Limpa:** Utiliza `os.system('cls')` e `time.sleep()` para manter o console organizado e fornecer feedback claro ao usuário (ex: "Tarefa adicionada com sucesso!").

<br>

### 🛠️ Tecnologias Utilizadas

* **Python:** Linguagem principal.
* **Módulo `os`:** Para limpeza do console (`cls`).
* **Módulo `time`:** Para pausas (`sleep`).

<br>

### ⚙️ Instalação e Execução

Este projeto utiliza apenas módulos nativos do Python.

1.  **Clone o Repositório:**
    ```bash
    git clone [https://github.com/KiefDry/lista_de_tarefas.git](https://github.com/KiefDry/lista_de_tarefas.git)
    cd lista_de_tarefas
    ```

2.  **Execute o Script:**
    ```bash
    python main.py
    ```
    O programa exibirá o menu principal com as opções (1-4) para você começar a gerenciar suas tarefas.