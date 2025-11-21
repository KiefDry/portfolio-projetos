from os import system as s
from time import sleep



# ENTRADA - RECEBENDO NÚMEROS E OPERADORES ######################################################
def get_data_input():
    """
    - Recebendo dois números e o operador para fazer o cálculo
    """    
    text = "    =================================\n" \
    "          Calculadora Básica 🧮\n" \
    "    =================================\n"
    print(text)

    first_number = int(input("Digite o primeiro número: "))
    second_number = int(input("Digite o segundo número: "))
    print()

    s("cls")
    operator_text = "Escolha um operador:\n" \
"   • Adição → +\n" \
"   • Subtração → -\n" \
"   • Multiplicação → *\n" \
"   • Divisão → /\n"
    print(operator_text)
    operator = input("Digite sua escolha: ")
    print()

    return [first_number, second_number, operator]
#################################################################################################


# EXECUÇÃO - EXECUTANDO E RETORNANDO RESULTADO DO CÁLCULO #######################################
def execute_operation(data):
    """
    - Cálcula e retorna o resultado do cálculo
    """
    number_1 = data[0]
    number_2 = data[1]
    operator = data[2]

    try:
        match operator:
            case "+":
                return f"O resultado da soma é: {number_1} + {number_2} = {number_1 + number_2}"
            case "-":
                return f"O resultado da subtração é: {number_1} - {number_2} = {number_1 - number_2}"
            case "*":
                return f"O resultado da multiplicação é: {number_1} * {number_2} = {number_1 * number_2}"
            case "/":
                return f"O resultado da divisão é: {number_1} / {number_2} = {number_1 / number_2}"
            case _:
                return f"Digite uma opção válida..."
    except ZeroDivisionError:
        return "Impossível dividir por zero."
#################################################################################################
    

if __name__ == "__main__":
    while True:
        try:
            data = get_data_input()
        except ValueError:
            s("cls")
            print("Por favor, digite apenas números...")
            sleep(2.5)
            s("cls")
            continue

        s("cls")
        resultado = execute_operation(data)
        print(resultado)

        input("\nPressione Enter para continuar...")
        s("cls")
        

        while True:
            continue_ = input("Deseja fazer outro cálculo [s/n]: ").lower().strip()
            
            match continue_:
                case "s":
                    s("cls")
                    continue
                case "n":
                    s("cls")
                    print("Saindo...")
                    sleep(2.5)
                    s("cls")
                    exit()
                case _:
                    s("cls")
                    continue
