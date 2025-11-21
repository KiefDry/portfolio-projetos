from os import system as s
from time import sleep


# ENTRADA - EXIBINDO OPÇÕES PARA O USUÁRIO #######################
def get_user_choice():
    TITLE_TEXT = "    ==================================\n" \
    "           Lista de Tarefas 📖\n" \
    "    ==================================\n"
    print(TITLE_TEXT)

    TEXT = "Escolha uma opção:\n\n" \
"    1 - Adicionar tarefa\n" \
"    2 - Ver tarefas\n" \
"    3 - Remover tarefa\n" \
"    4 - Sair\n"
    print(TEXT)
    user_choice = input("Digite sua escolha: ")
    
    return user_choice
##################################################################


# EXECUÇÃO - CRIANDO AS AÇÕES DO PROJETO #########################
def add_tasks(list_task_):
    s("cls")
    new_task = input("Digite a tarefa a ser adicionada: ")

    if len(new_task) > 0:
        if new_task not in list_task_:
            list_task_.append(new_task)
            s("cls")
            print(f"Tarefa adicionada com sucesso! Tarefa: '{new_task}'")
            print("-" * 52)
            sleep(3)
            s("cls")
        else:
            s("cls")
            print("Tarefa já adicionada!")
            sleep(3)
            s("cls")
    else:
        s("cls")
        print("Por favor, digite algo a ser adicionado.")
        sleep(3)
        s("cls")


def display_enumerated_lists(list_size_, list_task_):
    print("Tarefas:")
    if list_size_ > 0:
        for task in range(0, list_size_):
            print(f"    {task}. {list_task_[task]}")
    else:
        print("    Lista vazia.")


def show_tasks(list_task_):
    list_size = len(list_task_)

    s("cls")
    display_enumerated_lists(list_size, list_task_)
    print("-" * 52)

    input("\nPressione enter para continuar...")
    s("cls")


def remove_tasks(list_task_):
    s("cls")
    list_size = len(list_task_)
    display_enumerated_lists(list_size, list_task_)

    try:
        deleted_task = int(input("\nDigite a tarefa que deseja excluir: "))
    except ValueError:
        s("cls")
        print("Por favor, digite apenas índices.")
        sleep(3)
        s("cls")
        return 0
        
    list_task_.pop(deleted_task)
    print("\nTarefa excluída!!!")
    print("-" * 20)


def exit_program():
    s("cls")
    print("Encerrando...")
##################################################################


if __name__ == "__main__":
    list_task = []

    while True:
        s("cls")
        user_choice_ = get_user_choice()

        match user_choice_:
            case "1":
                add_tasks(list_task)
                continue
            case "2":
                show_tasks(list_task)
                continue
            case "3":
                try:
                    remove_tasks(list_task)
                except ValueError:
                    print("Digite apenas números.")
                    continue
                except IndexError:
                    print("Digite apenas índices existentes.")
                    continue
            case "4":
                exit_program()
                break
    