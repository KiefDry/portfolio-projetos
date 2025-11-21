from os import system as s


# ENTRADA - RECEBENDO PESO E ALTURA DO USUÁRIO ###################################
def get_data_input():
    """
    - Recebe o peso e a altura para o cálculo de IMC
    """
    text = "    =================================\n" \
    "           Calculadora IMC 🧮\n" \
    "    =================================\n"
    print(text)

    try:
        weigth = input("Digite seu peso (KG): ")
        weigth = int(weigth)
        s("cls")

        height = input("Digite sua altura (M): ")
        height = float(height)
        s("cls")

        bmi = weigth / (height ** 2)
        return bmi
    except ValueError:
        print("Não foi possível converter os números.")
##################################################################################


# EXECUÇÃO - CALCULANDO O IMC DO USUÁRIO #########################################
def bmi_result(bmi):
    """
    - Faz o cálculo do peso e altura, e retorna o IMC
    """
    if bmi == None:
        return "bmi não pode ser calculado."

    bmi_conditions = [
        (18.5, f"{bmi:.1f} - Abaixo do Peso"),
        (24.9, f"{bmi:.1f} - Peso Normal"),
        (29.9, f"{bmi:.1f} - Sobrepeso"),
        (34.9, f"{bmi:.1f} - Obesidade Grau 1"),
        (39.9, f"{bmi:.1f} - Obesidade Grau 2"),
        (float("inf"), f"{bmi:.1f} - Obesidade grau 3")
    ]

    for limit, category in bmi_conditions:
        if bmi < limit:
            return category
##################################################################################


if __name__ == "__main__":
    bmi = get_data_input()
    print(bmi_result(bmi), end="\n\n")
        

