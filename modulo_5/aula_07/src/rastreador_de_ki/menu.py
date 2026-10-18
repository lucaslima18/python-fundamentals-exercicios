"""Menu principal do rastreador de ki.

exibir_menu: exibe o menu.
valida_opcao_menu: interpreta a opção escolhida.
"""

from rich import print


def exibir_menu() -> None:
    """Exibe o menu principal da aplicação."""
    print("[bold][italic][#ea76cb]###### RASTREADOR DE KI ######")
    print("[bold][italic][#179299]###### MENU ######")
    print("""
    [bold][italic]1 - Registrar um novo guerreiro
    2 - Sair
    """)


def valida_opcao_menu(opcao: int) -> str | bool | None:
    """Valida a opção escolhida no menu.

    Args:
        opcao: número digitado pelo usuário.

    Return:
        None para 1, "pare" para 2 e False para as demais.
    """
    if opcao != 1 and opcao != 2:
        print("\n\nO número digitado não é válido :(, vamos voltar ao menu principal...\n\n")
        return False

    elif opcao == 2:
        return "pare"

    return None
