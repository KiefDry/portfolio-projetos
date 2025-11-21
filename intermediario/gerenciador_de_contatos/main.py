from os import system as s
from time import sleep as sl

# ENTRADA 1 - VERIFICANDO SE O USUÁRIO DESEJA CRIAR CONTATO ################
def should_generate_contact():
    text = "    ============================\n" \
    "       Gerador De Contatos 📒\n"\
    "    ============================\n"
    print(text)
    create_contact = input("Deseja criar um novo contato [s/n]: ").lower().strip()
    s("cls")

    return create_contact
############################################################################


# ENTRADA 2 - RECEBENDO OS DADOS DO CONTATO ################################
def generate_contact():
    text = "   --- Dados de Contato ---"
    print(text, end="\n\n")

    name = input("Nome: ").title()
    phone = input("Telefone: ")
    email = input("E-Mail: ")
    city = input("Cidade: ").title()

    with open("contacts.txt", "a", encoding="utf8") as f:
        f.write(f"Nome: {name}, Telefone: ({phone[0:2]}){phone[2:]}, E-Mail: {email}, Cidade: {city}\n")
        s("cls")
        print("   --- Contato Gerado com Sucesso ---")
        sl(3)
        s("cls")
############################################################################


if __name__ == "__main__":
    while True:
        create_contact = should_generate_contact()
        
        match create_contact:
            case "s":
                generate_contact()

                continue
            case "n":
                print("Saindo...")
                sl(3)
                s("cls")
                
                exit()
            case _:
                continue


