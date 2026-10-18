from typing import Any

from rich import print

dados: list[dict[str, Any]] = []


def criar_guerreiro(nome_do_guerreiro: str, ki_base: int, raca: str) -> dict[str, Any] | None:
    """Cadastra um guerreiro no banco.

    Args:
        nome: nome do guerreiro, usado como chave.
        ki_base: ki base do guerreiro.
        raca: raça do guerreiro.
        **extras: dados extras do guerreiro.

    Return:
        False se o guerreiro já existir, True caso contrário.
    """

    if not buscar_guerreiro(nome_do_guerreiro=nome_do_guerreiro):
        novo_guerreiro = {"nome": nome_do_guerreiro, "ki_base": ki_base, "raca": raca}
        dados.append(novo_guerreiro)
        return novo_guerreiro

    print("[italic red]O guerreiro já existe, portanto não pode ser cadastrado :(")


def listar_guerreiro() -> list[dict[str, Any]]:
    """Retorna todos os guerreiros cadastrados."""
    return dados


def buscar_guerreiro(nome_do_guerreiro: str) -> dict[str, Any] | None:
    """Busca um guerreiro pelo nome.

    Args:
        nome_do_guerreiro: nome do guerreiro.

    Return:
        Dados do guerreiro, ou None se não existir.
    """
    return next((guerreiro for guerreiro in dados if guerreiro["nome"] == nome_do_guerreiro), None)


def atualizar_guerreiro(nome_do_guerreiro: str, ki_base: int, raca: str) -> dict[str, Any] | None:
    """Substitui o ki base e a raça de um guerreiro.

    Args:
        nome: nome do guerreiro.
        ki_base: novo ki base.
        raca: nova raça.

    Return:
        Dados atualizados do guerreiro, ou None se ele não existir.
    """
    if guerreiro := buscar_guerreiro(nome_do_guerreiro=nome_do_guerreiro):
        guerreiro.update({"nome": nome_do_guerreiro, "ki_base": ki_base, "raca": raca})
        return guerreiro

    print("[italic red]O guerreiro não existe, portanto não pode ser atualizado :(")


def remover_guerreiro(nome_do_guerreiro: str) -> bool:
    """Exclui um guerreiro do banco.

    Args:
        nome_do_guerreiro: nome do guerreiro.

    Return:
        False se o guerreiro não existir, True caso contrário.
    """

    if guerreiro := buscar_guerreiro(nome_do_guerreiro=nome_do_guerreiro):
        dados.remove(guerreiro)
        return True

    print("[italic red]O guerreiro não existe, portanto não pode ser deletado :(")
