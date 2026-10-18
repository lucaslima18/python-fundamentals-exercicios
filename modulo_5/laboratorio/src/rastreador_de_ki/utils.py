from pyfiglet import figlet_format
from rich import print
from rich.console import Console

CONSOLE = Console()


def logo_principal():
    CONSOLE.print(f"""[#fe640b]{figlet_format(text="Rastreador de Ki")}
    [#7287fd bold italic]🔥 Salve seus guerreiros favoritos em um só lugar! 🚀\n
    ⚡ [#6c6f85 bold]Desenvolvido por:[/] [italic]Lucas Amorim (Kakaroto)
    📧 [#6c6f85 bold]Email:[/] [italic]lucas.ala1999@gmail.com
    🐙 [#6c6f85 bold]GitHub:[/] [#209fb5 italic]https://github.com/lucaslima18
    🔗 [#6c6f85 bold]LinkedIn:[/] [#209fb5 italic]https://www.linkedin.com/in/lucas-amorim-b09691173/""")
    print("\n\n")


def nova_tela() -> None:
    """Limpa o terminal e exibe o logo principal."""
    CONSOLE.clear()
    logo_principal()
