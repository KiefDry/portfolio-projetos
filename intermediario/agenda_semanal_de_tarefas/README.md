# Agenda Semanal 📅:

Um robusto gerenciador de tarefas de linha de comando (CLI) em Python, projetado para organizar atividades ao longo dos dias da semana.

Diferente de uma lista de tarefas padrão, este projeto permite ao usuário alocar tarefas para dias específicos (Segunda a Domingo) e gerenciá-las individualmente ou ver um resumo completo da semana.

<br>

### ✨ Funcionalidades em Destaque

* **Estrutura Semanal:** As tarefas são armazenadas em uma estrutura de dados que as mapeia para um dia específico da semana (indexado de 0 a 6).
* **Menu de Ações Completo:**
    * **Adicionar Tarefa:** Em um dia específico.
    * **Remover Tarefa:** De um dia específico, usando o índice da tarefa.
    * **Ver Tarefas (Por Dia):** Lista todas as tarefas de um único dia.
    * **Ver Tarefas (Semana):** Exibe um relatório completo de todas as tarefas de todos os dias.
    * **Marcar como Concluída:** Adiciona um marcador "✔️" a uma tarefa existente.
* **Uso de Decorators:** Utiliza um *decorator* customizado (`@day_text`) para DRY (Don't Repeat Yourself), reaproveitando o menu de seleção de dias em múltiplas funções (adicionar, remover, ver, etc.).
* **Tratamento de Erros Robusto:** Lida com `ValueError` (entradas não numéricas) e `IndexError` (índices de dias ou tarefas inexistentes).
* **Interface Limpa:** Gerencia o fluxo do console intensivamente com `os.system('cls')` e `time.sleep()` para uma experiência de usuário clara e passo a passo.

<br>

### 🛠️ Tecnologias Utilizadas

* **Python:** Linguagem principal (incluindo o uso de Decorators).
* **Módulo `os`:** Para limpeza do console (`cls`).
* **Módulo `time`:** Para pausas (`sleep`).

<br>

### ⚙️ Instalação e Execução

Este projeto utiliza apenas módulos nativos do Python.

1.  **Clone o Repositório:**
    ```bash
    git clone [https://github.com/KiefDry/agenda_semanal.git](https://github.com/KiefDry/agenda_semanal.git)
    cd agenda_semanal
    ```

2.  **Execute o Script:**
    ```bash
    python main.py
    ```
    O programa exibirá o menu principal (1-6) para você começar a gerenciar sua semana.