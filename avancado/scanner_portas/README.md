# Scanner de Portas Multi-Thread 🖥️:

Um scanner de portas TCP de linha de comando (CLI) avançado, escrito em Python. Este projeto utiliza **multi-threading** (`concurrent.futures`) para executar varreduras de alta velocidade em um host alvo (IP ou Hostname), permitindo ao usuário identificar portas abertas de forma rápida e eficiente.

A ferramenta é totalmente interativa, oferecendo múltiplos modos de scan e a opção de salvar os resultados em um arquivo `.csv`.

<br>

### ✨ Funcionalidades em Destaque

* **Multi-Threading de Alta Velocidade:** Utiliza `concurrent.futures.ThreadPoolExecutor` (com até 1500 *workers*) para escanear centenas de portas simultaneamente, tornando o scan muito mais rápido.
* **Resolução de Hostname:** Converte automaticamente hostnames (ex: 'google.com') para o seu endereço IP correspondente usando `socket.gethostbyname`.
* **Validação de IP:** Garante que os endereços IP inseridos sejam válidos usando a biblioteca `ipaddress`.
* **Múltiplos Modos de Scan:**
    * **Rápido:** Verifica uma lista predefinida das portas mais comuns (21, 22, 80, 443, etc.).
    * **Intervalado:** Verifica todas as portas "bem conhecidas" (1-1024).
    * **Personalizado:** Permite ao usuário definir portas (`80,443`) ou intervalos (`8080-8090`).
    * **Full Scan:** Verifica todas as 65.535 portas TCP.
* **Medição de Desempenho:** Um decorator customizado (`@dec_scans`) mede e exibe o tempo total de cada scan.
* **Segurança em Threads (Thread-Safe):** Utiliza `threading.Lock()` ao adicionar resultados à lista principal, evitando conflitos de dados entre as threads.
* **Exportação de Resultados:** Permite ao usuário salvar o relatório completo do scan (IP, Porta, Status) em um arquivo `.csv`.

<br>

### 🛠️ Tecnologias Utilizadas

* **Python:** Linguagem principal.
* **`socket`:** Para realizar as conexões TCP (`connect_ex`).
* **`ipaddress`:** Para validação de endereços IP.
* **`concurrent.futures` (ThreadPoolExecutor):** Para gerenciamento do pool de threads.
* **`threading` (Lock):** Para garantir a segurança ao acessar listas compartilhadas.
* **`csv`:** Para salvar os resultados.
* **`os` e `time`:** Para a interface do usuário (limpeza de tela e pausas).

<br>

### ⚙️ Instalação e Execução

Este projeto utiliza apenas módulos nativos do Python, não sendo necessária a instalação de dependências externas.

1.  **Clone o Repositório:**
    ```bash
    git clone [https://github.com/KiefDry/port_scanner.git](https://github.com/KiefDry/port_scanner.git)
    cd port_scanner
    ```

2.  **Execute o Script:**
    ```bash
    python main.py
    ```
    O programa exibirá o menu principal para você escolher o alvo (IP/Hostname) e o modo de scan.

<br>

### ⚠️ Aviso de Uso Ético

Esta ferramenta foi criada para fins educacionais e de estudo. O uso de scanners de porta em redes ou servidores sem autorização explícita é ilegal e antiético. Utilize apenas em seus próprios sistemas ou em ambientes controlados (CTFs, laboratórios) onde você tenha permissão.