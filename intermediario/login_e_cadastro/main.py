from os import system as s
from time import sleep as sl
import json


# ENTRADA - RECEBENDO A OPÇÃO DE LOGIN OU REGISTRO DO USUÁRIO ################
def homepage():
    text = "   ==============================\n" \
    "        SISTEMA DE LOGIN 🔐\n" \
    "   ==============================\n\n" \
    "[1] - Cadastrar Novo Usuário\n" \
    "[2] - Login\n" \
    "[3] - Sair\n"
    print(text)
    choice_option = input("Escolha uma das opções: ")
    
    return choice_option    
############################################################################## 


# REQUESTS - RECEBENDO INFORMAÇÕES DE LOGIN OU CADASTRO OD USUÁRIO ###########
def user_questions():
    s("cls")
    user = input("Digite o nome de usuário: ")
    password = input("Digite uma senha: ")

    return [user, password]
##############################################################################


# EXECUÇÃO - FUNÇÃO DE REGISTRO ##############################################
def register(data):
    """
    - Usuário escolhe um nome de usuário.
    - Digita uma senha.
    - O programa salva isso (normalmente em um arquivo .txt, .json ou até banco de dados).
    """
    user_questions_ = user_questions()
    data.append({"user": user_questions_[0], "password": user_questions_[1]})

    with open("login.json", "w", encoding="utf8") as f:
        json.dump(data, f, indent=2)
        s("cls")
        print("Contato adicionado com sucesso!")
        sl(2.5)
        s("cls")
##############################################################################


# EXECUÇÃO - FUNÇÃO DE LOGIN #################################################
def login(data):
    """
    - Usuário informa nome e senha.
    - O programa compara com os dados salvos.
    - Se coincidir → login feito com sucesso.
    - Se não → erro, tentar novamente.
    """
    user_questions_ = user_questions()
    s("cls")

    with open("login.json", "r", encoding="utf8") as f:
        data = json.load(f)

        for user in data:
            if user["user"] == user_questions_[0] and user["password"] == user_questions_[1]:
                print(f"Bem-Vindo de volta {user_questions_[0]}, logando...")
                break
            else:
                print(f"Usuário ou Senha inválidos!")
                break
        sl(3)
##############################################################################


# ENCERRAMENTO - FUNÇÃO DE RETORNO DA SAÍDA DO PROGRAMA ######################
def shutdown_message():
    s("cls")
    print("Saindo...")
    sl(2.5)
    s("cls")
##############################################################################


if __name__ == "__main__":
    data = []

    while True:
        s("cls")
        user_choice = homepage()

        match user_choice:
            case "1":
                register(data)
                continue
            case "2":
                login(data)
                continue
            case "3":
                shutdown_message()
                break
