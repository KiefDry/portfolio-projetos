from os import system as s
from time import sleep


# ENTRADA - RECEBENDO NÚMERO A SER CALCULADO #######################################################
def number_input():
    """
    - Recebe o número do usuário a ser calculado
    """
    text = "    ===================================\n" \
    "          Calculadora Fatorial 🧮\n" \
    "    ===================================\n"
    print(text)

    try:
        positive_integer = int(input("Digite um número inteiro positivo: "))

        return positive_integer
    except ValueError:
        return "Envie apenas números!"
####################################################################################################


# PROCESSAMENTO - CALCULANDO O FATORIAL ############################################################
def calculate(number):
    """
    - Função responsável por fazer os cálculos fatoriais
    """
    num = 1
    multiplied_number = 1
    text = f"O fatorial de {number} é:\n" \
    f"      {number}! = "

    try:
        while num <= number:
            multiplied_number *= num
            
            if num <= number:
                text += "".join(f"{num} x " if num < number else f"{num} = {multiplied_number}")
            num += 1

        return text
    except TypeError:
        return f"Por favor, digite apenas números inteiros e positivos."
####################################################################################################


# FILTRANDO ERROS - CALCULANDO O FATORIAL ##########################################################
def filter():
    """
    - Função responsável por filtrar apenas números inteiros
    """
    s("cls")
    print("Por favor, digite apenas números inteiros e positivos.")
    sleep(3)
    s("cls")
####################################################################################################
    

# EXECUÇÃO #########################################################################################
if __name__ == "__main__":
    while True:
        received_number = number_input()

        if isinstance(received_number, int) and received_number >= 0:
            s("cls")

            c = calculate(received_number)
            print(c, end="\n\n")
            input("\nPressione enter para continuar...")

            while True:
                s("cls")
                continue_ = input("Deseja fazer outro cálculo [s/n]: ").lower().strip()
                
                if continue_ == "s":
                    s("cls")
                    break
                elif continue_ == "n":
                    s("cls")
                    print("Saindo...")
                    exit()
        else: 
            filter()
####################################################################################################
