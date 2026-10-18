"""Menu principal do rastreador de ki.

exibir_menu: exibe o menu.
valida_opcao_menu: interpreta a opção escolhida.
"""

from typing import Any

import questionary
from rich import print

from rastreador_de_ki.crud_guerreiro import atualizar_guerreiro, buscar_guerreiro, criar_guerreiro, deletar_guerreiro, listar_guerreiros
from rastreador_de_ki.ficha_do_guerreiro import cadastrar_guerreiro, exibir_tabela_paginada, montar_ficha
from rastreador_de_ki.upload_de_guerreiros import exibir_resumo_importacao, importar_guerreiros
from rastreador_de_ki.utils import nova_tela

NOME_DOS_GUERREIROS = [guerreiro["nome_do_guerreiro"] for guerreiro in listar_guerreiros()]


def exibir_menu() -> None:
    """Exibe o menu principal da aplicação."""
    print("[bold italic #ea76cb]###### RASTREADOR DE KI ######\n")
    print("[bold italic #179299]###### MENU ######")
    print("""
    [bold italic]1 - Cadastrar guerreiro
    2 - Importar guerreiros
    3 - Atualizar guerreiro
    4 - Listar guerreiros
    5 - Buscar guerreiro
    6 - Remover guerreiro
    0 - Sair
    """)


def navegar_ficha_paginada(guerreiros: list[dict[str, Any]], por_pagina: int = 10) -> None:
    """Exibe os guerreiros página por página, perguntando a próxima ação.

    Args:
        guerreiros: guerreiros a exibir.
        por_pagina: quantidade de guerreiros por página.
    """
    pagina = 1
    ultima_pagina = (len(guerreiros) - 1) // por_pagina + 1

    while True:
        nova_tela()
        print(exibir_tabela_paginada(guerreiros, pagina, por_pagina))

        opcoes = []
        if pagina < ultima_pagina:
            opcoes.append("Próxima")
        if pagina > 1:
            opcoes.append("Anterior")
        opcoes.append("Sair")

        match questionary.select(f"Página {pagina} de {ultima_pagina}", choices=opcoes).ask():
            case "Próxima":
                pagina += 1
            case "Anterior":
                pagina -= 1
            case _:
                break


def pergunta_nome_guerreiro():
    if not NOME_DOS_GUERREIROS:
        print("[italic red]Nenhum guerreiro cadastrado ainda :(")
    return str(questionary.autocomplete("Digite o nome do guerreiro: ", choices=NOME_DOS_GUERREIROS).ask()).lower()


def realizar_acao(opcao: int) -> bool:
    match opcao:
        case 1:
            nome_do_guerreiro, ki_base, raca = cadastrar_guerreiro()
            if guerreiro := criar_guerreiro(nome_do_guerreiro=nome_do_guerreiro, ki_base=ki_base, raca=raca):
                print(montar_ficha(guerreiros=[guerreiro]))

        case 2:
            caminho = questionary.path("Digite o caminho da planilha: ").ask()
            if guerreiros_importados := importar_guerreiros(caminho):
                print(exibir_resumo_importacao(guerreiros_importados))

        case 3:
            if nome_do_guerreiro := pergunta_nome_guerreiro():
                nome_do_guerreiro, ki_base, raca = cadastrar_guerreiro()
                if guerreiro := atualizar_guerreiro(nome_do_guerreiro=nome_do_guerreiro, ki_base=ki_base, raca=raca):
                    print(montar_ficha(guerreiros=[guerreiro]))

        case 4:
            if guerreiros := listar_guerreiros():
                navegar_ficha_paginada(guerreiros=guerreiros)

        case 5:
            if nome_do_guerreiro := pergunta_nome_guerreiro():
                if guerreiro := buscar_guerreiro(nome_do_guerreiro):
                    print(montar_ficha(guerreiros=[guerreiro]))
                else:
                    print("[italic red]O Guerreiro não foi encontrado :(")

        case 6:
            if nome_do_guerreiro := pergunta_nome_guerreiro():
                deletar_guerreiro(nome_do_guerreiro)

        case 0:
            return False

    print("[#7287fd bold italic]---\n")
    estilo_pausa = questionary.Style([("", "fg:#7287fd bold italic")])
    questionary.press_any_key_to_continue("Pressione qualquer tecla para voltar ao menu...", style=estilo_pausa).ask()
    print("[#7287fd bold italic]---\n\n")
    return True
