from random import randint
from os import system as s
from time import sleep as sl


# ENTRADA - RECEBE A QUANTIDADE DE DADOS A SER JOGADOS ##########################
def number_of_dice():
    title_text = "    ==============================\n" \
    "         SIMULADOR DE DADO 🎲\n" \
    "    ==============================\n"
    print(title_text)

    try:
        dice_count = int(input("Quantos dados você quer lançar: "))
    except ValueError:
        s("cls")
        print("Digite apenas números!")
        sl(2.5)
        s("cls")

        return None
    return dice_count
#################################################################################


# EXECUÇÃO - EXIBE O RESULTADOS DE CADA DADO ####################################
def dice_result(number_of_dice):
    s("cls")

    i = 1
    print("🎲 Resultado dos dados:")
    for _ in range(number_of_dice):
        print(f"    Dado {i} → {randint(1, 6)}")
        i += 1
    input("\nPressione Enter para continuar...")
#################################################################################


if __name__ == "__main__":
    while True:
        num_dice_rolled = number_of_dice()

        if num_dice_rolled == None:
            continue
        
        if num_dice_rolled <= 0:
            s("cls")
            print("Por favor, digite apenas números positivos maiores que 0...")
            sl(2.5)
            s("cls")
            continue
        dice_result(num_dice_rolled)

        s("cls")

        while True:
            continue_ = input("Deseja jogar novamente [s/n]: ").lower().strip()
            
            match continue_:
                case "s":
                    s("cls")
                    print("Iniciando o jogo novamente...")
                    sl(2.5)
                    s("cls")
                    break
                case "n":
                    s("cls")
                    print("Saindo...")
                    sl(2.5)
                    s("cls")
                    exit()
                case _:
                    s("cls")
                    print('Por favor, digite apenas "s" ou "n"...')
                    sl(2.5)
                    s("cls")
                    continue