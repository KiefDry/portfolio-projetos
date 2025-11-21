from os import system as s
from time import sleep


# ENTRADA - RECEBE OS DADOS DO USUÁRIOS ###################################################################
def get_data_input():
    text = "    =================================\n" \
    "       Conversor de Temperatura 🌡️\n" \
    "    =================================\n"
    print(text)

    try:
        temperature_value = int(input("Digite a temperatura: "))
        
        while True:
            s("cls")
            original_temperature_unit = input("Digite a unidade original (C/F): ").lower().strip()

            if original_temperature_unit not in ["c", "f"]:
                s("cls")
                continue

            s("cls")
            desired_temperature_unit = input("Digite a unidade de conversão desejada (C/F): ").lower().strip()
            
            if desired_temperature_unit not in ["c", "f"]:
                s("cls")
                continue

            return [temperature_value, original_temperature_unit, desired_temperature_unit]
    except ValueError:
        s("cls")
        print("Por favor, digite apenas números!")
        sleep(3)
        s("cls")
###########################################################################################################


# EXECUÇÃO - FAZENDO A CONVERSÃO ##########################################################################
def check_conversion(data_list):
    try:
        celsius_calculation = (data_list[0] * 9/5) + 32
        fahrenheit_calculation = (data_list[0] - 32) * 5/9

        s("cls")
        if data_list[1] == "c" and data_list[2] == "f":
            return f"Resultado: {data_list[0]}°C = {celsius_calculation}°F"
        
        if data_list[1] == "f" and data_list[2] == "c":
            return f"Resultado: {data_list[0]}°F = {fahrenheit_calculation}°C"
        
    except TypeError:
        return "Tipos inválidos!"
###########################################################################################################


if __name__ == "__main__":
    while True:
        data_list = get_data_input()
        print(check_conversion(data_list))

        input("\n\nPressione Enter para continuar...")


        while True:
            s("cls")
            continue_ = input("Deseja fazer outra conversão [s/n]: ").lower().strip()
            s("cls")
            
            match continue_:
                case "s":
                    break
                case "n":
                    print("Saindo...")
                    sleep(2.5)
                    s("cls")
                    exit()
                case _:
                    continue
