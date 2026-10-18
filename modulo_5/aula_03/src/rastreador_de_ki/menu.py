from rich import print


def exibir_menu():
    print("[bold][italic][#ea76cb]###### RASTREADOR DE KI ######")
    print("[bold][italic][#179299]###### MENU ######")
    print("""
    [bold][italic]1 - Registrar um novo guerreiro
    2 - Sair
    """)


def valida_opcao_menu(opcao):
    if opcao != 1 and opcao != 2:
        print("\n\nO número digitado não é válido :(, vamos voltar ao menu principal...\n\n")
        return False

    elif opcao == 2:
        return "pare"
