import json
from typing import Any

from pyfiglet import figlet_format
from rich import print
from rich.console import Console

CONSOLE = Console()
ARQUIVO_DADOS_GUERREIROS = "src/rastreador_de_ki/dados/guerreiros.json"


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


def normalizar_strings(texto: str) -> str:
    return texto.strip().lower()


def tabela_dos_guerreiros() -> list[dict[str, Any]]:
    with open(ARQUIVO_DADOS_GUERREIROS, "r+", encoding="utf-8") as guerreiros_arquivo:
        guerreiros = guerreiros_arquivo.read()
        if not guerreiros:
            tabela_guerreiro = {"guerreiros": []}
            json.dump(tabela_guerreiro, guerreiros_arquivo, indent=4)
            return tabela_guerreiro["guerreiros"]
        else:
            return json.loads(guerreiros)["guerreiros"]


def salvar_tabela_dos_guerreiros(guerreiros: list[dict[str, Any]]) -> None:
    """Grava a lista de guerreiros no arquivo JSON, substituindo o conteúdo.

    Args:
        guerreiros: lista de guerreiros.
    """
    with open(ARQUIVO_DADOS_GUERREIROS, "w", encoding="utf-8") as guerreiros_arquivo:
        json.dump({"guerreiros": guerreiros}, guerreiros_arquivo, indent=4, ensure_ascii=False)
