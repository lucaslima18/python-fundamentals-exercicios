from typing import Any

from rich import print

from rastreador_de_ki.utils import salvar_tabela_dos_guerreiros, tabela_dos_guerreiros

TABELA = tabela_dos_guerreiros()

def criar_guerreiro(nome_do_guerreiro: str, ki_base: int, raca: str) -> dict[str, Any] | None:
    """Cadastra um guerreiro no banco.

    Args:
        nome_do_guerreiro: nome do guerreiro, usado como chave.
        ki_base: ki base do guerreiro.
        raca: raça do guerreiro.

    Return:
        False se o guerreiro já existir, True caso contrário.
    """

    if not buscar_guerreiro(nome_do_guerreiro=nome_do_guerreiro):
        novo_guerreiro = {"nome_do_guerreiro": nome_do_guerreiro, "ki_base": ki_base, "raca": raca}
        TABELA.append(novo_guerreiro)
        salvar_tabela_dos_guerreiros(guerreiros=TABELA)
        return novo_guerreiro

    print("[italic red]O guerreiro já existe, portanto não pode ser cadastrado :(")


def listar_guerreiros() -> list[dict[str, Any]]:
    """Retorna todos os guerreiros cadastrados."""
    if not TABELA:
        print("[italic red]Ainda não temos guerreiros cadastrados no sistema :(")

    return TABELA
    


def buscar_guerreiro(nome_do_guerreiro: str) -> dict[str, Any] | None:
    """Busca um guerreiro pelo nome.

    Args:
        nome_do_guerreiro: nome do guerreiro.

    Return:
        Dados do guerreiro, ou None se não existir.
    """
    return next((guerreiro for guerreiro in TABELA if guerreiro["nome_do_guerreiro"] == nome_do_guerreiro), None)


def atualizar_guerreiro(nome_do_guerreiro: str, ki_base: int, raca: str) -> dict[str, Any] | None:
    """Substitui o ki base e a raça de um guerreiro.

    Args:
        nome_do_guerreiro: nome do guerreiro.
        ki_base: novo ki base.
        raca: nova raça.

    Return:
        Dados atualizados do guerreiro, ou None se ele não existir.
    """
    if guerreiro := buscar_guerreiro(nome_do_guerreiro=nome_do_guerreiro):
        guerreiro.update({"nome_do_guerreiro": nome_do_guerreiro, "ki_base": ki_base, "raca": raca})
        salvar_tabela_dos_guerreiros(TABELA)
        return guerreiro

    print("[italic red]O guerreiro não existe, portanto não pode ser atualizado :(")


def deletar_guerreiro(nome_do_guerreiro: str) -> None:
    """Exclui um guerreiro do banco.

    Args:
        nome_do_guerreiro: nome do guerreiro.

    Return:
        False se o guerreiro não existir, True caso contrário.
    """

    if guerreiro := buscar_guerreiro(nome_do_guerreiro=nome_do_guerreiro):
        tabela_dos_guerreiros().remove(guerreiro)
        salvar_tabela_dos_guerreiros(TABELA)
        print(f"[italic green]O guerreiro {nome_do_guerreiro} foi deletado com sucesso!!! :)")

    else:
        print(f"[italic red]O guerreiro {nome_do_guerreiro} não existe, portanto não pode ser deletado :(")
