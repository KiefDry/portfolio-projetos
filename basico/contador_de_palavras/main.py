from os import system as s


# ENTRADA - RECEBENDO O TEXTO A FAZER A CONTAGEM ########################################
def get_data_inputs():
    text = "    =================================\n" \
    "          Contador de Plavras 🧮\n" \
    "    =================================\n"
    print(text)

    user_text = input("Digite seu texto: ").lower().strip().split()
    s("cls")

    return user_text
#########################################################################################


# EXECUÇÃO - FILTRANDO OS PONTOS DO TEXTO ###############################################
def process_text():
    punctuation_list = ["!", ".", ",", ";", "?"]
    new_list = []

    for word in get_data_inputs():
        for dot in punctuation_list:
            word = word.replace(dot, "")
        new_list.append(word)

    return new_list
#########################################################################################
    

# RESULTADO - RETORNANDO A CONTAGEM DE PALAVRAS #########################################
def return_count_output(list_):
    counter = 0
    for word in list_:
        for _ in word:
            counter += 1
    
    words_counter = ""
    for word in list_:
        count_output_text = f"     - '{word}' apareceu: {list_.count(word)}x\n"
        words_counter += "".join(
            count_output_text if not count_output_text
            in words_counter else ""
        )
    
    text = f"• Número de palavras no texto: {len(list_)}\n" \
    f"• Número de letras (Sem espaço): {counter}\n\n" \
    f"Contagem de ocorrência de cada palavras: \n" \
    f"{words_counter}"

    return text
#########################################################################################


if __name__ == "__main__":
    text_without_punctuation = process_text()
    print(return_count_output(text_without_punctuation))
        
