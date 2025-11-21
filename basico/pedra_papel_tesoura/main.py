from random import choice
from os import system as s
import sys
from time import sleep

# ENTRADA - RECEBENDO E RETORNANDO ESCOLHAS ##################################################################
def get_input_data():
    text = "    ==================================\n" \
    "         Pedra, Papel, Tesoura ✌️\n" \
    "    ==================================\n"
    print(text)

    question_text = f"                 Pedra          \n" \
    f"                 Papel          \n" \
    f"                 Tesoura          \n"
    print(question_text)

    user_choice = input("Digite sua escolha: ").lower().strip()
    computer_choice = choice(["pedra", "papel", "tesoura"])

    s("cls")
    return [user_choice, computer_choice]
##############################################################################################################


# EXECUÇÃO - RETORNANDO A MENSAGEM DE ESCOLHAS ###############################################################
def determine_winner(user_choice, computer_choice):
    choice_text = f"Você escolheu: {user_choice.capitalize()}\n" \
        f"Computador escolheu: {computer_choice.capitalize()}\n"
    print(choice_text)
    
    user_conditions_list = [
        (user_choice == "pedra" and computer_choice == "tesoura", "🎊🎊  VOCÊ GANHOU!!!  🎊🎊"),
        (user_choice == "tesoura" and computer_choice == "papel", "🎊🎊  VOCÊ GANHOU!!!  🎊🎊"),
        (user_choice == "papel" and computer_choice == "pedra", "🎊🎊  VOCÊ GANHOU!!!  🎊🎊"),
        (user_choice == computer_choice, "🤯🤯  Você empatou  🤯🤯")
    ]

    computer_conditions_list = [
        (computer_choice == "pedra" and user_choice == "tesoura", "Você perdeu...  🥹"),
        (computer_choice == "tesoura" and user_choice == "papel", "Você perdeu...  🥹"),
        (computer_choice == "papel" and user_choice == "pedra", "Você perdeu...  🥹")
    ]
    
    for condition, message in user_conditions_list:
        if condition:
            return message
        
    for condition, message in computer_conditions_list:
        if condition:
            return message
##############################################################################################################


if __name__ == "__main__":
    while True:
        choices = get_input_data()
        
        user_choice = choices[0]
        computer_choice = choices[1]
        print(determine_winner(user_choice, computer_choice))
        input("\n\nPressione Enter para continuar...")
        s("cls")


        while True:
            continue_ = input("Deseja continar [s/n]: ").lower().strip()
            s("cls")

            match continue_:
                case "s":
                    break
                case "n":
                    s("cls")
                    print("Saindo...")
                    sleep(2)
                    s("cls")
                    exit()
