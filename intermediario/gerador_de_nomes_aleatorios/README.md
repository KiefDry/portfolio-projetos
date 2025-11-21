# Gerador de Nomes ✍️:

Um script de linha de comando (CLI) em Python que gera nomes aleatórios com base em listas predefinidas.

O script é organizado em torno de um menu interativo que permite ao usuário selecionar a categoria do nome desejado (masculino, feminino, unissex ou completo), sorteando um resultado da categoria correspondente.

<br>

### ✨ Funcionalidades em Destaque

* **Menu Interativo:** Permite ao usuário escolher entre 4 categorias de nomes.
* **Nomes Categorizados:** Gera nomes a partir de listas de `male_names`, `female_names`, `unisex_names` e `complete_names` armazenadas em um dicionário.
* **Seleção Aleatória:** Utiliza `random.choice()` para sortear um nome da lista selecionada.
* **Tratamento de Erros:** Captura `ValueError` caso o usuário digite uma opção de menu não numérica.
* **Loop de Execução:** Permite ao usuário gerar múltiplos nomes em sequência sem reiniciar o script [s/n].
* **Interface Limpa:** Utiliza `os.system('cls')` e `time.sleep()` para gerenciar o fluxo do console.

<br>

### 🛠️ Tecnologias Utilizadas

* **Python:** Linguagem principal (incluindo `match...case`).
* **Módulo `random` (choice):** Para a seleção aleatória.
* **Módulo `os`:** Para limpeza do console (`cls`).
* **Módulo `time`:** Para pausas (`sleep`).

<br>

### ⚙️ Instalação e Execução

Este projeto utiliza apenas módulos nativos do Python.

1.  **Clone o Repositório:**
    ```bash
    git clone [https://github.com/KiefDry/gerador_de_nomes.git](https://github.com/KiefDry/gerador_de_nomes.git)
    cd gerador_de_nomes
    ```

2.  **Execute o Script:**
    ```bash
    python main.py
    ```
    O programa exibirá o menu principal (1-4) para você escolher o tipo de nome.