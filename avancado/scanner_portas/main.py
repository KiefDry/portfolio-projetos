from os import system as s
import ipaddress
import socket
import concurrent.futures
import threading
import time
import re
import csv


# INÍCIO - RECEBENDO IP ALVO DO USUÁRIO ##################################################
def get_ip():
    text = "      ============================\n" \
    "           SCANNER DE PORTAS 🖥️\n" \
    "      ============================\n\n" \
    "[1] - Hostname\n" \
    "[2] - IP\n"
    print(text)  # texto incial
    
    try:
        ip = input("Tipo de Alvo (Hostname | IP): ")  # escolha do tipo de alvo

        if ip == "1":
            s("cls")
            hostname = input("Digite o Hostname alvo: ").strip()
            ip = socket.gethostbyname(hostname)  # resolvendo/traduzindo hostname para IP

            s("cls")
            print(f"Hostname resolvido: {hostname} → {ip}")
            time.sleep(2.5)
            s("cls")

            return ip
        elif ip == "2":
            s("cls")
            ip = input("Digite o IP alvo: ").strip()
            ip = ipaddress.ip_address(ip)  # verifica se é um IP válido

            s("cls")
            print("IP Válido ☑️")
            time.sleep(2.5)
            s("cls")

            return ip
        else:
            s("cls")
            print(text)
            ip = input("Tipo de Alvo (Hostname | IP): ")
    except socket.gaierror:  # caso o hostname não se resolva em um IP válido
        s("cls")
        print("Hostname/IP inválido ❌")
        time.sleep(2.5)
        s("cls")
    except ValueError:
        s("cls")
        print("Digite um IP válido!")
        time.sleep(2.5)
        s("cls")
##########################################################################################


# APRIMORANDO - DECORANDO SCANS ##########################################################
def dec_scans(func):
    def wrapper(*args, **kwargs):
        s("cls")
        start_time = time.perf_counter()

        result = func(*args, **kwargs)

        final_time = time.perf_counter()
        duration = final_time - start_time
        
        print(f"Tempo total de scan: {duration:.2f}")
        input("\n\nPressione enter para continuar...")

        s("cls")
        save_scan(result)

        return result
    return wrapper


def dec_workers(workers_func, host, ports, result, open_ports):
    lock_list = threading.Lock()

    text = f"Iniciando scan em {host}:\n" \
    "-----------------------------------"
    print(text)

    with concurrent.futures.ThreadPoolExecutor(max_workers=1500) as pool:
        futures = [pool.submit(workers_func, host, port) for port in ports]

        for future in futures:
            host, port, connexion_result, process_end_time = future.result()

            return_text = ports_return(result, host, port, connexion_result, process_end_time, open_ports, lock_list)
            print(return_text)
        
        s("cls")
        print("Iniciando workers, aguarde os resultados...")
##########################################################################################


# BASE SCAN - SCANNER PARA OS WORKERS ####################################################
def template_scan(host, port):
    start_process = time.perf_counter()  # tempo inicial do processo

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # família = tipo IP (IPv4/IPv6), tipo = tipo de envio de pacotes (TCP/UDP)
    sock.settimeout(0.5)  # coloca um timer limite para testar conexão com uma porta
    connexion_result = sock.connect_ex((host, port))

    sock.close
    
    final_process = time.perf_counter()  # tempo final do processo
    process_end_time = final_process - start_process  # cálculo do tempo

    return [host, port, connexion_result, process_end_time]
##########################################################################################


# SCAN 1 = SCAN RÁPIDO ###################################################################
@dec_scans
def quick_scan(result, host):
    host = str(host)

    ports = [
        21, 22, 23, 24, 25,
        53, 67, 68, 80, 110,
        123, 143, 161, 162, 194,
        443, 445, 465, 587, 993,
        1433, 1521, 3306, 3389
    ]
    open_ports = []

    dec_workers(template_scan, host, ports, result, open_ports)

    s("cls")
    complete_scan(host, ports, open_ports)

    return result
##########################################################################################


# SCAN 2 = SCAN INTERVALADO ##############################################################
@dec_scans
def interval_scan(result, host):
    host = str(host)

    ports = [n for n in range(1, 1025)]
    open_ports = []

    dec_workers(template_scan, host, ports, result, open_ports)

    s("cls")
    complete_scan(host, ports, open_ports)

    return result
##########################################################################################


# SCAN 3 = SCAN PERSONALIZADO ############################################################
@dec_scans
def scan_personalizado(result, host):
    ports = input("Digite as portas desejadas: ").strip(" ")
    s("cls")
    transformed_ports = ports.split(",")
    integer_ports = set()

    for port in transformed_ports:
        stripped_port = str(port).strip()
        port_range = stripped_port.split("-")
        
        if not "-" in stripped_port:
            integer_ports.add(int(stripped_port))
        else:
            integer_ports.update(set(n for n in range(int(port_range[0]), int(port_range[1]))))
    
    integer_ports = list(sorted(integer_ports))
    open_ports = []

    dec_workers(template_scan, host, integer_ports, result, open_ports)

    s("cls")
    complete_scan(host, integer_ports, open_ports)

    return result
##########################################################################################
    
   
# SCAN 4 = SCAN COMPLETO #################################################################
@dec_scans
def full_scan(result, host):
    ports = [n for n in range(1, 65535 + 1)] 
    open_ports = []

    dec_workers(template_scan, host, ports, result, open_ports)

    s("cls")
    complete_scan(host, ports, open_ports)

    return result
##########################################################################################


# EXECUÇÃO - ESCOLHA DO MODO #############################################################
def scanner():
    text = "Escolha o modo:\n" \
    "   [1] - Rápido (portas comuns)\n" \
    "   [2] - Intervalado (ex: 1-1024)\n" \
    "   [3] - Lista Personalizada (ex: 22, 80, 443)\n" \
    "   [4] - Full (1-65535)\n" \
    "   [5] - Sair\n"
    print(text)
    try:
        mode = int(input("> "))
        return mode
    except ValueError:
        s("cls")
        print("Digite uma opção válida.")
        time.sleep(2.5)
        s("cls")
##########################################################################################


# CONCLUSÃO - MSG FIM DO SCAN ############################################################
def complete_scan(target, tested_ports, open_ports):
    tested_ports_count = len(tested_ports)
    open_ports_count = len(open_ports)
    
    text = "      ===========================\n" \
    "           SCAN CONCLUÍDO 🖥️\n" \
    "      ===========================\n\n" \
    f"Alvo: {target}\n" \
    f"Portas Testadas: {tested_ports_count}\n" \
    f"Portas Abertas: {open_ports_count}\n\n" \
    f"Portas Abertas:\n"
    text += "".join(
        f"  - {porta}\n" for porta in open_ports if len(open_ports) > 0
    )
    print(text)
##########################################################################################


# CONCLUSÃO - PERSISTÊNCIA DE DADOS ######################################################
def save_scan(results):
    wants_to_save = input("Deseja salvar o Scan [s/n]: ").lower().strip()

    s("cls")
    if wants_to_save == "s":
        file = input("Digite o nome do arquivo a ser salvo (adcione .csv ao final): ")

        with open(file, "w", encoding="utf8") as f:
            writer = csv.writer(f)
            writer.writerow(["IP Alvo", "Porta", "Status"])

            for line in results:
                target = line[0]
                port = line[1]
                status = line[2]
                
                list_to_save = [target, port, status]
                writer.writerow(list_to_save)
            
        s("cls")
        print("Scan salvo com sucesso!")
        time.sleep(2.5)  
    elif wants_to_save == "n":
        return 0
    else:
        s("cls")
        wants_to_save = input("Deseja salvar o Scan [s/n]: ").lower().strip()
##########################################################################################


# EXECUÇÃO - RETORNO DE PORTAS (MODIFICADO PARA THREADS) ##################################
def ports_return(results, target, port, connexion_result, time, open_ports, lock):
    if connexion_result == 0:
        open_ports.append(port)
        resultado_parcial = f"[{port}] - OPEN 🟢   ({time:.1f}ms)"
        
        connexion_result = "OPEN🟢"
        
        # Pega o "cadeado" antes de mexer na lista compartilhada
        with lock:
            results.append([target, port, connexion_result])
        
    else:
        resultado_parcial = f"[{port}] - CLOSED 🔴 ({time:.1f}ms)"

    return resultado_parcial
##########################################################################################


if __name__ == "__main__":
    results = []

    while True:
        s("cls")
        ip = get_ip()

        try:
            ipaddress.ip_address(ip)
        except ValueError:
            continue
        
        s("cls")
        scan = scanner()
        match scan:
            case 1:
                quick_scan(results, ip)
                results = []
            case 2:
                interval_scan(results, ip)
                results = []
            case 3:
                scan_personalizado(results, ip)
                results = []
            case 4:
                full_scan(results, ip)
                results = []
            case 5:
                s("cls")
                print("Saindo...")
                time.sleep(2.5)
                s("cls")
                break
        continue
