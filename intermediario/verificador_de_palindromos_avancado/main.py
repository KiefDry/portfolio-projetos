from os import system as s
from time import sleep as sl
from functools import reduce
import unicodedata


# FILTRAGEM - REMOVENDO ACENTOS DO TEXTO #######################################
def remove_accents(text):
    return "".join(
        char for char in unicodedata.normalize("NFD", text)
        if unicodedata.category(char) != "Mn"
    )
################################################################################


# ENTRADA - RECEBENDO O TEXTO PARA VERIFICAÇÃO #################################
def get_palindrome():
    TITLE_TEXT = "    =============================================\n" \
    "            Verificador de Palíndromos ⚖️\n" \
    "    =============================================\n"
    print(TITLE_TEXT)

    user_palindrome = input("Digite uma palavra ou frase: ").lower().strip()
    filtered_palindrome = remove_accents(user_palindrome).replace("-", "").replace(",", "").replace(" ", "")
    
    return [user_palindrome, filtered_palindrome]
################################################################################


# EXECUÇÃO - VERIFICANDO SE O TEXTO É UM PALÍNDROMO ############################
def check_palindrome(text):
    inverted_text = text[1][::-1]

    if text[1] == inverted_text:
        s("cls")
        print(f"| {text[0]} | = É um palíndromo\n\n")
        input("Pressione Enter para continuar...")
    else:
        s("cls")
        print(f"| {text[0]} | = Não é um palíndromo\n\n")
        input("Pressione Enter para continuar...")
################################################################################


if __name__ == "__main__":
    while True:
        filtered_palindrome = get_palindrome()
        check_palindrome(filtered_palindrome)
        
        while True:
            s("cls")
            continue_ = input("Deseja jogar novamente [s/n]: ").lower().strip()
            s("cls")
            
            match continue_:
                case "s":
                    break
                case "n":
                    print("Saindo...")
                    sl(2.5)
                    s("cls")

                    exit()
                case _:
                    continue

