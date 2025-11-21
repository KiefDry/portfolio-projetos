from random import randint
from os import system as s
from time import sleep


# FUNÇÃO PRINCIPAL - RECEBENDO E RETORNANDO RESULTADO #####################################################################
def main():
    text = "    ==================================\n" \
    "          Jogo de Adivinhação 🔑\n" \
    "    ==================================\n"

    random_number = randint(0, 100)
    attempts = 0

    while True:
        try:
            print(text)
            user_number = int(input("Adivinhe um número entre 0 e 100: "))
            attempts += 1
            conditions_list = [
                (random_number > user_number, f"O número é maior que: {user_number}"),
                (random_number < user_number, f"O número é menor que: {user_number}"),
                (random_number == user_number, f"VOCÊ ACERTOU!!! O número é: {random_number} (Tentativas: {attempts})")
            ]

            if conditions_list[0][0]:
                s("cls")
                print(conditions_list[0][1])
                
                input("\n\nPressione Enter para continuar...")

                s("cls")
                continue
            
            if conditions_list[1][0]:
                s("cls")
                print(conditions_list[1][1])
                
                input("\n\nPressione Enter para continuar...")

                s("cls")                
                continue

            if conditions_list[2][0]:
                s("cls")
                print(conditions_list[2][1])
                
                input("\n\nPressione Enter para continuar...")
                
                s("cls")
                break
        except ValueError:
            print("Por favor, digite apenas números!\n\n")
            continue
###########################################################################################################################

if __name__ == "__main__":
    while True:
        main()

        continue_ = input("Deseja jogar novamente [s/n]: ").lower().strip()

        match continue_:
            case "s":
                s("cls")
                continue
            case "n":
                s("cls")
                print("Saindo...")
                sleep(2)
                s("cls")
                exit()

