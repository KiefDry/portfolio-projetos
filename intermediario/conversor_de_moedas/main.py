from os import system as s
from time import sleep as sl


# EXECUÇÃO - FAZENDO A CONVERSÃO ######################################################
def conversion(currency_):
    currency = 0
    converted_value = 0

    try:
        match currency_:
            case "1":
                currency = float(input("Digite o valor em Reais: "))
                converted_value = currency * 5.45
                s("cls")
                return f"{currency} BRL equivale a {converted_value} USD"
            case "2":
                currency = float(input("Digite o valor em Dólar: "))
                converted_value = currency * 0.86
                s("cls")
                return f"{currency} USD equivale a {converted_value} EUR"
            case "3":
                currency = float(input("Digite o valor em Euro: "))
                converted_value = 5.45 * currency
                s("cls")
                return f"{currency} EUR equivale a {converted_value} BRL"
            case _:
                return "Escolha uma opção válida [0-3]"
    except ValueError:
        print("Só consigo converter números!")
#######################################################################################


# ENTRADA - RECEBENDO A ESCOLHA DE CONVERSÃO DO USUÁRIO ###############################
def main():
    while True:
        s("cls")

        title_text = "    =================================\n" \
        "          Conversor de Moedas 💱\n" \
        "    =================================\n"
        print(title_text)

        text = "Escolha uma opção:\n\n" \
        "   1 - Real (BRL) para Dólar (USD);\n" \
        "   2 - Dólar (USD) para Euro (EUR);\n" \
        "   3 - Euro (EUR) para Real (BRL)\n"
        print(text)
        conversion_choice = input("Digite a opção desejada: ")

        if conversion_choice not in ["1", "2", "3"]:
            s("cls")
            print("Escolha uma opção válida [0-3].")
            sl(3)
            s("cls")
        else:
            s("cls")
            print(conversion(conversion_choice), end="\n\n")
            input("Pressione Enter para continuar...")
            s("cls")
            
            while True:
                continue_ = input("Deseja fazer outra conversão [s/n]: ").lower().strip()

                if continue_ in ["s", "sim", "y", "yes"]:
                    break
                elif continue_ in ["n", "não", "no", "nao"]:
                    s("cls")
                    print("Saindo...")
                    sl(3)
                    s("cls")

                    exit()
                else:
                    s("cls")
                    print("Digite apenas Sim ou Não.")
                    input("Pressione enter para continuar...")
                    print()
                    s("cls")

                    continue
#######################################################################################


if __name__ == "__main__":
    main()
