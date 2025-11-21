# Conversor de Moedas 💱:

Um script de linha de comando (CLI) em Python que atua como um conversor de moedas, focado em três rotas de conversão específicas: Real (BRL), Dólar (USD) e Euro (EUR).

O projeto é estruturado em torno de um menu interativo e utiliza taxas de câmbio **estáticas (hardcoded)** no próprio código para realizar os cálculos.

<br>

### ✨ Funcionalidades em Destaque

* **Menu Interativo:** Permite ao usuário escolher entre 3 opções de conversão:
    1.  Real (BRL) para Dólar (USD)
    2.  Dólar (USD) para Euro (EUR)
    3.  Euro (EUR) para Real (BRL)
* **Taxas de Câmbio Estáticas:** As conversões são feitas usando valores fixos (ex: `1 EUR = 5.45 BRL`).
* **Loop de Execução Contínuo:** Possui um loop robusto que pergunta ao usuário se deseja "continuar [s/n]", aceitando múltiplas formas de resposta (s, sim, y, yes, n, nao, no).
* **Tratamento de Erros:** Valida a entrada do menu principal (aceitando apenas 1, 2 ou 3) e captura `ValueError` se o usuário digitar um valor não numérico para a moeda.
* **Interface Limpa:** Utiliza `os.system('cls')` e `time.sleep()` para gerenciar o fluxo do console e limpar a tela.

<br>

### 🛠️ Tecnologias Utilizadas

* **Python:** Linguagem principal (incluindo `match...case`).
* **Módulo `os`:** Para limpeza do console.
* **Módulo `time`:** Para pausas (`sleep`).

<br>

### ⚙️ Instalação e Execução

Este projeto utiliza apenas módulos nativos do Python.

1.  **Clone o Repositório:**
    ```bash
    git clone [https://github.com/KiefDry/conversor_de_moedas.git](https://github.com/KiefDry/conversor_de_moedas.git)
    cd conversor_de_moedas
    ```

2.  **Execute o Script:**
    ```bash
    python main.py
    ```
    O programa exibirá o menu com as 3 opções de conversão.