# Conversor de Temperatura 🌡️:

Um script de linha de comando (CLI) em Python para converter temperaturas entre **Celsius (C)** e **Fahrenheit (F)**.

O projeto foca em uma interface de usuário interativa e robusta, que guia o usuário na entrada de dados (valor, unidade original, unidade desejada) e valida as entradas para garantir que apenas "c" ou "f" sejam aceitos.

<br>

### ✨ Funcionalidades em Destaque

* **Conversão Bidirecional:** Converte temperaturas de Celsius para Fahrenheit e de Fahrenheit para Celsius.
* **Validação de Entrada:** Possui loops de validação que forçam o usuário a digitar "c" ou "f" para as unidades, rejeitando qualquer outra entrada.
* **Tratamento de Erros:** Captura `ValueError` caso o usuário digite um valor não numérico para a temperatura.
* **Loop de Execução Contínuo:** Permite ao usuário realizar múltiplas conversões em sequência, perguntando se deseja "continuar [s/n]" ao final de cada cálculo.
* **Interface Limpa:** Utiliza `os.system('cls')` e `time.sleep()` para limpar o console e gerenciar o fluxo de mensagens, tornando a experiência de usuário mais limpa.

<br>

### 🛠️ Tecnologias Utilizadas

* **Python:** Linguagem principal do projeto.
* **Módulo `os`:** Utilizado para a limpeza do console (`cls`).
* **Módulo `time`:** Utilizado para pausas (`sleep`) na exibição de mensagens.

<br>

### ⚙️ Instalação e Execução

Este projeto utiliza apenas módulos nativos do Python, não sendo necessária a instalação de dependências externas.

1.  **Clone o Repositório:**
    ```bash
    git clone [https://github.com/KiefDry/conversor_de_temperatura.git](https://github.com/KiefDry/conversor_de_temperatura.git)
    cd conversor_de_temperatura
    ```

2.  **Execute o Script:**
    ```bash
    python main.py
    ```
    O programa solicitará o valor da temperatura, a unidade original (C/F) e a unidade de conversão desejada (C/F).