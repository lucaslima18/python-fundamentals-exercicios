import questionary
from rich import print

from rastreador_de_ki.crud_guerreiro import atualizar_guerreiro, buscar_guerreiro, criar_guerreiro, deletar_guerreiro, listar_guerreiros
from rastreador_de_ki.ficha_do_guerreiro import cadastrar_guerreiro, montar_ficha
from rastreador_de_ki.logs import exibir_log, registrar_log


def exibir_menu() -> None:
    """Exibe o menu principal da aplicação."""
    print("[bold italic #ea76cb]###### RASTREADOR DE KI ######\n")
    print("[bold italic #179299]###### MENU ######")
    print("""
    [bold italic]1 - Cadastrar guerreiro
    2 - Listar guerreiros
    3 - Buscar guerreiro
    4 - Atualizar guerreiro
    5 - Remover guerreiro
    6 - Exibir logs
    0 - Sair
    """)


def realizar_acao(opcao: int) -> bool:
    match opcao:
        case 1:
            registrar_log("Processando pedido de cadastro de guerreiro")
            nome_do_guerreiro, ki_base, raca = cadastrar_guerreiro()
            if guerreiro := criar_guerreiro(nome_do_guerreiro=nome_do_guerreiro, ki_base=ki_base, raca=raca):
                    print(montar_ficha(guerreiros=[guerreiro]))
                    registrar_log(f"guerreiro {nome_do_guerreiro} cadastrado e ficha exibida com")

        case 2:
            if guerreiros := listar_guerreiros():
                    print(montar_ficha(guerreiros=guerreiros))

        case 3:
            nome_do_guerreiro = str(questionary.text("Digite o nome do Guerreiro: ").ask()).lower()
            if guerreiro := buscar_guerreiro(nome_do_guerreiro=nome_do_guerreiro):
                print(montar_ficha(guerreiros=[guerreiro]))
            
            else:
                    print("[italic red]O Guerreiro não foi encontrado :(")

        case 4:
            nome_do_guerreiro, ki_base, raca = cadastrar_guerreiro()
            if guerreiro := atualizar_guerreiro(nome_do_guerreiro=nome_do_guerreiro, ki_base=ki_base, raca=raca):
                print(montar_ficha(guerreiros=[guerreiro]))

        case 5:
            nome_do_guerreiro = str(questionary.text("Digite o nome do Guerreiro: ").ask()).lower()

        case 6:
           exibir_log()

        case 0:
            print("Até a próxima!")
            return False

    print("[#7287fd bold italic]---\n")
    estilo_pausa = questionary.Style([("", "fg:#7287fd bold italic")])
    questionary.press_any_key_to_continue("Pressione qualquer tecla para voltar ao menu...", style=estilo_pausa).ask()
    print("[#7287fd bold italic]---\n\n")
    return True