from typing import Any

from rich import print

from rastreador_de_ki.logs import registrar_log

GUERREIROS: list[dict[str, Any]] = []


def criar_guerreiro(nome_do_guerreiro: str, ki_base: int, raca: str) -> dict[str, Any] | None:
    registrar_log(f"cadastrando novo guerreiro {nome_do_guerreiro}")
    if not buscar_guerreiro(nome_do_guerreiro=nome_do_guerreiro):
        registrar_log(f"Guerreiro não existe, continuando a criação do guerreiro {nome_do_guerreiro}")
        novo_guerreiro = {"nome_do_guerreiro": nome_do_guerreiro, "ki_base": ki_base, "raca": raca}
        GUERREIROS.append(novo_guerreiro)
        registrar_log(f"novo guerreiro salvo: Nome: {nome_do_guerreiro}, Ki base: {ki_base}, Raça: {raca}")
        return novo_guerreiro

    registrar_log(f"Guerreiro {nome_do_guerreiro} já existe e não foi cadastrado")
    print("[italic red]O guerreiro já existe, portanto não pode ser cadastrado :(")


def listar_guerreiros() -> list[dict[str, Any]] | None:
    if GUERREIROS != []:
        return GUERREIROS
    print("[italic red]Ainda não temos guerreiros cadastrados no sistema :(")


def buscar_guerreiro(nome_do_guerreiro: str) -> dict[str, Any] | None:
    return next((guerreiro for guerreiro in GUERREIROS if guerreiro["nome_do_guerreiro"] == nome_do_guerreiro), None)


def atualizar_guerreiro(nome_do_guerreiro: str, ki_base: int, raca: str) -> dict[str, Any] | None:
    if guerreiro := buscar_guerreiro(nome_do_guerreiro=nome_do_guerreiro):
        guerreiro.update({"nome_do_guerreiro": nome_do_guerreiro, "ki_base": ki_base, "raca": raca})
        return guerreiro

    print("[italic red]O guerreiro não existe, portanto não pode ser atualizado :(")


def deletar_guerreiro(nome_do_guerreiro: str) -> None:
    if guerreiro := buscar_guerreiro(nome_do_guerreiro=nome_do_guerreiro):
        GUERREIROS.remove(guerreiro)
        print("[italic green]O guerreiro foi deletado com sucesso!!! :)")
    else:
        print("[italic red]O guerreiro não existe, portanto não pode ser deletado :(")