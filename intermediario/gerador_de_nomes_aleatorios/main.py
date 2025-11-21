from random import choice
from os import system as s
from time import sleep as sl


# APRIMORANDO - FUNÇÃO PARA EXIBIR UMA FRASE COM O NOME ESCOLHIDO ####################
def print_name(chosen_name):
    texto = f"O nome escolhido é: {chosen_name}\n\n"
    print(texto)
######################################################################################


# RECEBENDO E RETORNANDO - RECEBE A OPÇÃO DE NOME DESEJADA E RETORNA O MESMO #########
def names_options(names):
    title_text = "    =================================\n" \
    "            Gerador de Nomes ✍️\n" \
    "    =================================\n"

    while True:
        print(title_text)

        text = "Escolha uma opção:\n\n" \
        "   1 - Nome masculino\n" \
        "   2 - Nome feminino\n" \
        "   3 - Nome unissex\n" \
        "   4 - Nome completo (nome + sobrenome)"
        print(text, end="\n\n")
    
        try:
            user_option = int(input("Digite sua opção: "))
            chosen_name = ""

            match user_option:
                case 1:
                    chosen_name = choice(names["male_names"])
                    s("cls")
                    print_name(chosen_name)
                    input("Pressione enter para continuar...")
                    
                    return
                case 2:
                    chosen_name = choice(names["female_names"])
                    s("cls")
                    print_name(chosen_name)
                    input("Pressione enter para continuar...")
                    
                    return
                case 3:
                    chosen_name = choice(names["unisex_names"])
                    s("cls")
                    print_name(chosen_name)
                    input("Pressione enter para continuar...")
                    
                    return
                case 4:
                    chosen_name = choice(names["complete_names"])
                    s("cls")
                    print_name(chosen_name)
                    input("Pressione enter para continuar...")
                    
                    return
                case _:
                    s("cls")
                    continue
        except ValueError:
            s("cls")
            print("Por favor, digite apenas números!")
            sl(3)
            s("cls")
######################################################################################


if __name__ == "__main__":

    names_dict = {
        "male_names": ["Rafael", "Lucas", "Gabriel", "Matheus", "Gustavo"],
        "female_names": ["Mariana", "Fernanda", "Camila", "Juliana", "Ana"],
        "unisex_names": ["Alex", "Sam", "Cris", "Dani", "Taylor"],
        "complete_names": ["Rafael Souza", "Mariana Oliveira", "Alex Pereira", "Fernanda Costa", "Lucas Silva"],
    }

    while True:
        names_options(names_dict)

        while True:
            s("cls")
            continue_ = input("Deseja criar outro nome [s/n]: ").lower().strip()

            if continue_ == "s":
                s("cls")
                continue
            elif continue_ == "n":
                s("cls")
                print("Saindo...")
                sl(3)
                s("cls")

                exit()

