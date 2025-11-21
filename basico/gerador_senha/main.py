from os import system as s
import string
from random import choice
from time import sleep


# ENTRADA - RECEBENDO AS CARACTERÍSTICAS DA SENHA ##################################################################
def password_characteristics():
    text = "    ==================================\n" \
    "           Gerador de Senhas 🔑\n" \
    "    ==================================\n"

    while True:
        try:
            print(text)
            char_count = int(input("Qual o tamanho da senha desejada: "))
            s("cls")
            
            uppercase_letters = input("A senha deve conter:\n   a. Incluir letras maiúsculas [S/N]: ").lower().strip()
            lowercase_letters = input("   b. Incluir letras minúsculas [S/N]: ").lower().strip()
            include_numbers = input("   c. Incluir números [S/N]: ").lower().strip()
            include_symbols = input("   d. Incluir símbolos [S/N]: ").lower().strip()
            
            return [char_count, uppercase_letters, lowercase_letters, include_numbers, include_symbols]
        except ValueError:
            s("cls")
            print("Digite apenas números.")
            sleep(2.5)
            s("cls")
            continue
###################################################################################################################


# EXECUÇÃO - CRIA A SENHA COM AS CARACTERÍSTICAS DO USUÁRIO #######################################################
def generate_password(char_count, uppercase_letters, lowercase_letters, include_numbers, include_symbols):
    uppercase_strings = string.ascii_uppercase
    lowercase_strings = string.ascii_lowercase
    digits = string.digits
    punctuation = string.punctuation
    password = ""

    if uppercase_letters == "n" and lowercase_letters == "n" and include_numbers == "n" and include_symbols == "n":
        return password

    while len(password) < char_count:
        if uppercase_letters == "s":
            password += "".join(choice(uppercase_strings))
        
        if lowercase_letters == "s":
            password += "".join(choice(lowercase_strings))
        
        if include_numbers == "s":
            password += "".join(choice(digits))
        
        if include_symbols == "s":
            password += "".join(choice(punctuation))

    return password
###################################################################################################################
    

if __name__ == "__main__":
    while True:
        s("cls")
        password_characteristics_ = password_characteristics()
        password = generate_password(password_characteristics_[0], password_characteristics_[1], password_characteristics_[2], password_characteristics_[3], password_characteristics_[4])
        s("cls")
        if password == "":
            print(f"Senha vazia.")
        else:
            print(f"A senha gerada foi: {password}\n\n")
        
        input("Pressione Enter para continuar...")

        s("cls")
        continue_ = input("Deseja continuar [s/n]: ").lower().strip()

        match continue_:
            case "s":
                continue
            case "n":
                s("cls")
                print("Saindo...")
                sleep(2)
                s("cls")
                exit()
        
