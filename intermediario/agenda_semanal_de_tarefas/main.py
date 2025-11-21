from os import system as s
from time import sleep as sl


# DECORANDO - DECORA FUNÇÕES COM O TEXTO BASE #################################
def day_text(func):
    def inner(*args, **kwargs):
        try:
            text = "Escolha o dia da semana:\n\n" \
            "    0. Segunda-Feira\n" \
            "    1. Terça-Feira\n" \
            "    2. Quarta-Feira\n" \
            "    3. Quinta-Feira\n" \
            "    4. Sexta-Feira\n" \
            "    5. Sábado\n" \
            "    6. Domingo\n"
            print(text)
        except ValueError:
            print("Por favor, digite o número do dia!")
        return func(*args, **kwargs)
    return inner
###############################################################################


# ENTRADA - RECEBENDO O DIA DESEJADO PELO USUÁRIO #############################
def day():
    try:
        day = input("Digite o número do dia: ")
        integer_day = int(day)
    except ValueError:
        print("Por favor, digite um dia válido!")
    s("cls")

    return [day, integer_day]
###############################################################################


# EXECUÇÃO - AÇÕES DO PROJETO #################################################
@day_text
def add_task(tasks_log):
    try:
        days_ = day()
        s("cls")
        
        if days_[1] <= 6:
            task = input("Digite a tarefa a ser adicionada: ")
            tasks_log[days_[1]][days_[0]].append(task)
            
            s("cls")
            print("Tarefa adicionada com sucesso!")
            sl(3)
            s("cls")
        else:
            s("cls")
            print("Por favor, digite um dia válido!")
            sl(3)
            s("cls")
    except ValueError:
        s("cls")
        print("Por favor, digite o dia em números!")
        sl(3)
        s("cls")
    except IndexError:
        s("cls")
        print("Por favor, escolha um dia válido!")
        sl(3)
        s("cls")


@day_text
def delete_task(tasks_log):
    try:
        text = "Tarefas: "
        day_ = day()
        s("cls")

        index = 0
        print(text, end="\n")
        
        if tasks_log[day_[1]][day_[0]] == []:
            print("    Sem tarefas para ser removida!\n\n")

            input("Pressione Enter para continuar...")
            s("cls")
            return
        else:
            for item in tasks_log[day_[1]][day_[0]]:
                print(f"     {index}. {item}")
                index += 1
            print()

        task = input("Digite a tarefa a ser removida: ")
        task = int(task)
        tasks_log[day_[1]][day_[0]].pop(task)

        s("cls")
        print("Tarefa removida com sucesso!")
        sl(3)
        s("cls")
    except ValueError:
        s("cls")
        print("Por favor, digite o dia em números!")
        sl(3)
        s("cls")
    except IndexError:
        s("cls")
        print("Por favor, escolha um dia válido!")
        sl(3)
        s("cls")


@day_text
def list_day_tasks(tasks_log):
    try:
        day_ = day()
        day_task = tasks_log[day_[1]][day_[0]]
        s("cls")
        text = f"Tarefas dia {day_[0]}:"

        index = 0
        print(text, end="\n")
        if day_task == []:
            print("     Sem tarefas para hoje!")
        else:
            for item in day_task:
                print(f"     {index}. {item}")
                index += 1

        print()
        input("Pressione enter para continuar...")
        s("cls")
    except ValueError:
        s("cls")
        print("Por favor, digite o dia em números!")
        sl(3)
        s("cls")
    except IndexError:
        s("cls")
        print("Por favor, escolha um dia válido!")
        sl(3)
        s("cls")


def list_weekly_tasks(tasks_log):
    s("cls")
    day_index = 0
    
    task_index = 0
    for days_dicts in tasks_log:
        day_string = str(day_index)
        
        print(f"Tarefas dia {day_index}:")

        if days_dicts[day_string] == []:
            print("     Sem tarefas para hoje!")
            day_index += 1

            print()
            print("--" * 15)
            print()

            continue
        else:
            day_index += 1

            for tarefa in days_dicts[day_string]:
                print(f"     {task_index} - {tarefa}")
                task_index += 1

            print()
            print("--" * 15)
            print()

            continue

    input("Pressione enter para continuar...")
    s("cls")


@day_text
def mark_as_complete(tasks_log):
    try:
        day_ = day()
        tasks = tasks_log[day_[1]][day_[0]]

        s("cls")
        text = f"Tarefas dia {day_[0]}:"
        print(text, end="\n\n")

        index = 0
        for task in tasks:
            print(f"     {index}. {task}")
            index += 1
        print()
    
        task_ = input("Digite o número da tarefa: ")
        integer_task = int(task_)

        tasks[integer_task] += "".join(" | Concluída ✔️")

        s("cls")
        print("Tarefa concluída com sucesso - 🎊PARABÉNS🎊")
        sl(3)
        s("cls")
    except ValueError:
        s("cls")
        print("Por favor, digite apenas o número da tarefa!")
        sl(3)
        s("cls")
    except IndexError:
        s("cls")
        print("Por favor, escolha um dia válido")
        sl(3)
        s("cls")
###############################################################################


if __name__ == "__main__":
    options_text = " 1. Adicionar tarefa\n" \
    " 2. Remover tarefa\n" \
    " 3. Ver tarefas (Por dia)\n" \
    " 4. Ver todas as tarefas (Semana)\n"\
    " 5. Marcar tarefa como concluída\n" \
    " 6. Sair\n"
    
    weekly_task_log = [
        {"0": []},
        {"1": []},
        {"2": []},
        {"3": []},
        {"4": []},
        {"5": []},
        {"6": []}
    ]

    while True:
        try:
            title_text = "    =================================\n" \
            "            Agenda Semanal 📅\n" \
            "    =================================\n"
            print(title_text)

            print(options_text)
            opcao_selecionada = int(input("Digite o número da sua escolha: "))

            match opcao_selecionada:
                case 6:
                    s("cls")
                    print("Saindo...")
                    sl(2.5)
                    s("cls")
                    break
                case 1:
                    s("cls")
                    add_task(weekly_task_log)
                    continue
                case 2:
                    s("cls")
                    delete_task(weekly_task_log)
                    continue
                case 3:
                    s("cls")
                    list_day_tasks(weekly_task_log)
                    continue
                case 4:
                    s("cls")
                    list_weekly_tasks(weekly_task_log)
                    continue
                case 5:
                    s("cls")
                    mark_as_complete(weekly_task_log)
                    continue
                case _:
                    s("cls")
                    continue
        except ValueError:
            s("cls")
            print("Por favor, digite o número de uma opção válida.")
            sl(3)
            s("cls")
            continue
