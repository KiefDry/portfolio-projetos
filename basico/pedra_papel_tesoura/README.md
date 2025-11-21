# Calculadora de Índice de Massa Corporal (IMC) 📏:

Um script interativo de linha de comando (CLI) em Python para calcular o Índice de Massa Corporal (IMC) do usuário e fornecer a classificação correspondente (Abaixo do Peso, Peso Normal, Obesidade, etc.).

O projeto foca em uma **entrada de dados simples** e uma **classificação precisa** e otimizada por faixas.

<br>

### ✨ Funcionalidades em Destaque

* **Cálculo Imediato:** Calcula o IMC com base no peso (KG) e altura (M) fornecidos pelo usuário.
* **Classificação Otimizada:** Utiliza uma estrutura de dados concisa (lista de tuplas) para classificar o IMC nas diferentes categorias de saúde.
* **Tratamento Básico de Erros:** Lida com entradas não numéricas para evitar quebras do script.
* **Interface Limpa:** Usa o módulo `os` para limpar a tela e manter a interface do console organizada durante a interação.

<br>

### 🛠️ Tecnologias Utilizadas

* **Python:** Linguagem principal do projeto.
* **Módulo `os`:** Utilizado para a limpeza do console (`cls`).

<br>

### ⚙️ Instalação e Execução

Este projeto utiliza apenas módulos nativos do Python e não requer dependências externas.

1.  **Clone o Repositório:**
    ```bash
    git clone [https://github.com/KiefDry/calculadora_imc.git](https://github.com/KiefDry/calculadora_imc.git)
    cd calculadora_imc
    ```

2.  **Execute o Script:**
    ```bash
    python main.py
    ```
    O programa pedirá que você insira seu peso e altura sequencialmente.

<br>

### ⚠️ Referência de Classificação

Para referência, as faixas de IMC utilizadas para a classificação (seguindo o padrão da Organização Mundial da Saúde) são:

* Abaixo do Peso: IMC < 18.5
* Peso Normal: 18.5 a 24.9
* Sobrepeso: 25.0 a 29.9
* Obesidade Grau 1: 30.0 a 34.9
* Obesidade Grau 2: 35.0 a 39.9
* Obesidade Grau 3: 40.0 ou mais