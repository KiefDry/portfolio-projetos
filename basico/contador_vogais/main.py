from os import system as s


# ENTRADA - RECEBENDO FRASE DO USUÁRIO #############################
def get_data_input():
    text = "    =================================\n" \
    "          Contador de Vogais 🅰️\n" \
    "    =================================\n"
    print(text)

    user_phrase = input("Digite uma frase: ").lower().strip()
    vowels = ["a", "e", "i", "o", "u"]

    return [user_phrase, vowels]
####################################################################


# EXECUÇÃO - FAZENDO A CONTAGEM DAS VOGAIS #########################
def count_vowels(phrase, vowels):
    s("cls")
    text = f"A frase: {phrase.capitalize()}, tem:\n"

    for vowel in vowels:
        repetition_count = phrase.count(vowel)
        text += "".join(f"{vowel}: {repetition_count}\n")

    return text
####################################################################


if __name__ == "__main__":
    data = get_data_input()
    print(count_vowels(data[0], data[1]))
