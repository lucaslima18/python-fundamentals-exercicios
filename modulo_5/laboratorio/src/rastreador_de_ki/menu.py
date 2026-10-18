"""Menu principal do rastreador de ki.

exibir_menu: exibe o menu.
valida_opcao_menu: interpreta a opção escolhida.
"""

from rich import print


def exibir_menu() -> None:
    """Exibe o menu principal da aplicação."""
    print("[bold][italic][#ea76cb]###### RASTREADOR DE KI ######\n")
    print("[bold][italic][#179299]###### MENU ######")
    print("""
    [bold][italic]1 - Cadastrar guerreiro
    2 - Listar guerreiros
    3 - Buscar guerreiro
    4 - Atualizar guerreiro
    5 - Remover guerreiro
    6 - Sair
    """)
