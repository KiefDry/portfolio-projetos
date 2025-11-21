from random import choice
from time import sleep as sl
from os import system as s

# ENTRADA E RETORNO - RECEBE AS LETRAS DO USUÁRIO E RETORNA OS RESULTADOS ####################
def secret_word(word, used):
    title_text = "   =============================\n" \
    "          JOGO DA FORCA 🎯\n" \
    "   =============================\n\n"
    print(f"{title_text}Adivinhe a palavra secreta!\n")
    
    chosen_word = choice(word)
    descovered_word = ["_ " for _ in range(len(chosen_word))]

    attempts = 0
    while True:
        print(f"Palavra: {"".join(l for l in descovered_word)}")
        print(f"Tentativas: {attempts}")
        print("Letras usadas: ", *used)

        typed_letter = input("\nDigite uma letra: ").lower().strip()
        s("cls")

        if len(typed_letter) > 1:
            s("cls")
            print("Digite uma única letra.")
            sl(2)
            s("cls")
            continue

        if not typed_letter in used:
            used.append(typed_letter)
        index = 0

        for letter in chosen_word:
            if typed_letter == letter:
                descovered_word[index] = letter
            index += 1

            if not typed_letter in chosen_word:
                print(f"A palavra não contém a letra ou número: {typed_letter}")
                sl(2.3)
                s("cls")
                attempts += 1
                break

        if descovered_word == [*chosen_word]:
            print(f"🎊🎊 PARABÉNS 🎊🎊 A palavra é: {chosen_word.capitalize()}")
            break
        else:
            if attempts == 6: 
                print("Você perdeu!!!")
                break
            continue
###############################################################################################
        

if __name__ == "__main__":
    words = ["bolo", "queijo", "corrigedoria", "lazer", "assassino"]
    used_words = []

    while True:
        secret_word(words, used_words)
        sl(3.5)
        s("cls")

        while True:
            continue_ = input("Deseja jogar novamente [s/n]: ").lower().strip()

            match continue_:
                case "s":
                    used_words = []
                    s("cls")
                    break
                case "n":
                    s("cls")
                    print("Saindo...")
                    sl(2)
                    s("cls")
                    exit()
                case _:
                    s("cls")
                    continue




