from os import system as s
from time import sleep as sl


# ENTRADA - RECEBE A OPÇÃO DO USUÁRIO ##############################################
def display_start_options():
    title_text = "   ==============================\n" \
    "           PYTHON QUIZ 📖\n" \
    "   ==============================\n\n" \
    "[1] - Iniciar Quiz\n" \
    "[2] - Ver Ranking\n" \
    "[3] - Sair\n"
    print(title_text)
    user_choice = input("Sua resposta: ")

    return user_choice
####################################################################################


# EXECUÇÃO - EXIBE OPÇÕES E RECEBE AS RESPOSTAS DO USUÁRIO #########################
def start_quiz(options, ranking):
    questions_and_answers = list(options.items())
    correct_answers = ["a", "b", "c", "d"]
    user_choice = ""

    for questions, aswers in questions_and_answers:
        print(questions)
        for answer in aswers:
            if not answer in correct_answers:
                print(f"    {answer}")
        print()
        user_choice = input("Digite sua escolha: ").lower().strip()
        
        if user_choice == aswers[-1]:
            s("cls")
            print("✅ Correto!")
            ranking["acertos"] += 1
        else:
            s("cls")
            print("❌ Errado!")
            ranking["erros"] += 1
        sl(2.5)
        s("cls")
    
    s("cls")
    print(display_end_game_message(correct_count), end="\n\n")
    input("Pressione enter para continuar...")
    s("cls")
####################################################################################


# FINALIZAÇÃO - EXIBINDO A CLASSIFICAÇÃO FINAL DO QUIZ #############################
def display_end_game_message(score):
    total_score = score["acertos"] * 10
    classification = ""
    
    if total_score <= 50:
        classification = "⭐ Iniciante"
    elif total_score >= 60 and total_score <= 100:
        classification = "⭐⭐ Intermediário"
    elif total_score > 100:
        classification = "⭐⭐⭐ Veterano"
    
    message = "----------------------------------------\n" \
    "   Fim do Quiz!\n" \
    f"   Você acertou {score["acertos"]} de {score["acertos"] + score["erros"]} perguntas.\n" \
    f"   Pontuação: {total_score} pontos\n" \
    f"   Classificação: {classification}\n" \
    "----------------------------------------\n"

    return message


def ranking():
    s("cls")
    print("Ranking ainda não disponível nesta versão!\n" \
          "Jogue uma partida para ver seu desempenho.")
    sl(3)
    s("cls")
####################################################################################


if __name__ == "__main__":
    general_knowlegde = {
        "Capital da Austrália: ": ["A) Sidney", "B) Melbourne", "C) Canberra", "D) Brisbane", "c"],
        "Quem Pintou Monalisa: ": ["A) Van Gogh", "B) Leonardo da Vinci", "C) Picasso", "D) Michelangelo", "b"],
        "Qual é o Maior Planeta do Sistema Solar: ": ["A) Saturno", "B) Júpiter", "C) Netuno", "D) Terra", "b"],
        "Quem é Considerado o 'Pai da Computação': ": ["A) Alan Turing", "B) Bill Gates", "C) Steve Jobs", "D) Ada Lovelace", "a"],
        "Qual é o Símbolo Químico da Água: ": ["A) O₂", "B) H₂O", "C) CO₂", "D) HO", "b"],
        "Em Que Ano Foi Lançado o Primeiro iPhone: ": ["A) 2005", "B) 2007", "C) 2010", "D) 2003", "b"],
        "Quanto é 12 x 8: ": ["A) 92", "B) 86", "C) 96", "D) 88", "c"],
        "Qual é a Raiz Quadrada de 144: ": ["A) 10", "B) 11", "C) 12", "D) 14", "c"],
        "O Que Vem a Seguir na Sequência 2, 4, 8, 16, ...: ": ["A) 20", "B) 24", "C) 32", "D) 64", "c"],
        "Em Que Ano Foi Lançado o Filme Matrix: ": ["A) 1997", "B) 1999", "C) 2001", "D) 2003", "b"],
        "Quem é o Criador da Série One Piece: ": ["A) Masashi Kishimoto", "B) Eiichiro Oda", "C) Akira Toriyama", "D) Yoshiro Togashi", "b"],
        "Qual é o Verdadeiro Nome do Batman: ": ["A) Clark Kent", "B) Bruce Wayne", "C) Peter Parker", "D) Tony Stark", "b"],
        "Qual Animal é Considerado o Mais Rápido do Mundo: ": ["A) Guepardo", "B) Falcão-Peregrino", "C) Cavalo Árabe", "D) Golfinho", "b"],
        "Qual País é Conhecido Como 'Terra do Sol Nascente': ": ["A) China", "B) Coreia do Sul", "C) Japão", "D) Tailândia", "c"],
        "Qual é o Idioma Mais Falado do Mundo: ": ["A) Inglês", "B) Espanhol", "C) Mandarim", "D) Hindi", "c"]
    }

    while True:
        user_option = display_start_options()
        s("cls")

        match user_option:
            case "1":
                correct_count = {
                    "acertos": 0,
                    "erros": 0,
                }
                start_quiz(general_knowlegde, correct_count)
                
                continue
            case "2":
                ranking()

                continue
            case "3":
                print("Saindo...")
                sl(3)
                s("cls")

                break
