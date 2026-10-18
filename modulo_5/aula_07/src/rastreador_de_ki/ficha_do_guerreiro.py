"""Cadastro e avaliação de guerreiros.

cadastrar_guerreiro: coleta os dados do guerreiro.
valida_nivel_ki: classifica o ki base.
valida_saiyajin: verifica se é saiyajin.
valida_lendario: verifica se é lendário.
valida_supersaiyajin: verifica se pode virar supersaiyajin.
criar_tabela_basica: cria a tabela da ficha.
"""

from typing import Any

import questionary
from rich import print
from rich.table import Table


def cadastrar_guerreiro(*dados_extras: str) -> tuple[str, int, str, dict[Any, Any]]:
    """Coleta pelo terminal os dados do guerreiro.

    Args:
        *dados_extras: rótulos de dados extras a perguntar; viram chaves
            em snake_case no dicionário retornado.

    Return:
        Tupla (nome, ki_base, raca, dados_extras), com nome e raça em
        minúsculas.

    Raises:
        ValueError: se o ki base não for inteiro.
    """
    nome_do_guerreiro: str = str(questionary.text("Digite o nome do Guerreiro: ").ask()).lower()
    ki_base: int = int(questionary.text("Digite o nível do KI base do guerreiro: ").ask())
    raca: str = str(questionary.text("Digite a raça do guerreiro: ").ask()).lower()
    colecao_de_dados_extras: dict[Any, Any] = {}

    for chave_do_dado_extra in dados_extras:
        valor_do_dado_extra: Any = questionary.text(f"Digite {chave_do_dado_extra}: ").ask()
        colecao_de_dados_extras.update({"_".join(chave_do_dado_extra.lower().split()): valor_do_dado_extra})

    return nome_do_guerreiro, ki_base, raca, colecao_de_dados_extras


def valida_nivel_ki(ki_base: int) -> str:
    """Retorna a classificação do ki base.

    Faixas: BAIXO < 500 <= MÉDIO < 2000 <= ALTO < 9000 <= LENDÁRIO.

    Args:
        ki_base: ki base do guerreiro.

    Return:
        Mensagem com a classificação do ki.
    """
    if ki_base < 500:
        return "O ki é considerado BAIXO!"

    if ki_base < 2000:
        return "O ki é considerado MÉDIO!"

    if ki_base < 9000:
        return "O ki é considerado ALTO!"

    return "O ki é considerado LENDÁRIO!"


def valida_saiyajin(raca: str) -> str:
    """Retorna a mensagem que informa se a raça é saiyajin.

    Args:
        raca: raça do guerreiro em minúsculas.

    Return:
        Mensagem positiva ou negativa.
    """
    return "Este guerreiro é um siyajin." if raca == "saiyajin" else "Este guerreiro NÃO é um siyajin."


def valida_lendario(ki_base: int, e_saiyajin: str) -> str:
    """Retorna a mensagem que informa se o guerreiro é lendário.

    É lendário se o ki base passar de 9000 ou se for saiyajin.

    Args:
        ki_base: ki base do guerreiro.
        e_saiyajin: mensagem retornada por valida_saiyajin.

    Return:
        Mensagem positiva ou negativa.
    """
    return "Este é um guerreiro lendário!!!" if ki_base > 9000 or e_saiyajin == "Este guerreiro é um siyajin." else "Este NÃO é um guerreiro lendário :("


def valida_supersaiyajin(nivel_ki: str, e_saiyajin: str) -> str:
    """Retorna a mensagem que informa se o guerreiro pode virar supersaiyajin.

    Pode virar se o ki for ALTO, ou LENDÁRIO e o guerreiro for saiyajin.

    Args:
        nivel_ki: mensagem retornada por valida_nivel_ki.
        e_saiyajin: mensagem retornada por valida_saiyajin.

    Return:
        Mensagem positiva ou negativa.
    """
    if nivel_ki == "O ki é considerado ALTO!" or nivel_ki == "O ki é considerado LENDÁRIO!" and e_saiyajin == "Este guerreiro é um siyajin.":
        return "Este guerreiro pode virar um supersaiyajin!!!"
    return "Este guerreiro não pode virar um supersaiyajin :("


def criar_tabela_basica(**dados_extras: dict[Any, Any]) -> Table:
    """Cria a tabela da ficha do guerreiro, sem linhas.

    Cada coluna extra criada é informada no terminal.

    Args:
        **dados_extras: dados extras; cada chave vira uma coluna.

    Return:
        Tabela com as colunas fixas e extras.
    """
    ficha_do_guerreiro: Table = Table(title="FIXA DO GUERREIRO", style="#f9e2af", title_style="#b4befe")
    ficha_do_guerreiro.add_column(header="Guerreiro", style="#f5c2e7", header_style="#f5c2e7")
    ficha_do_guerreiro.add_column(header="Raça", style="#f5c2e7", header_style="#f5c2e7")
    ficha_do_guerreiro.add_column(header="Ki Base", style="#f5c2e7", header_style="#f5c2e7")
    ficha_do_guerreiro.add_column(header="O ki base é alto?", style="#f5c2e7", header_style="#f5c2e7")
    ficha_do_guerreiro.add_column(header="O guerreiro pode virar super saiyajin?", style="#f5c2e7", header_style="#f5c2e7")
    ficha_do_guerreiro.add_column(header="O guerreiro pode ser considerado um ser lendário?", style="#f5c2e7", header_style="#f5c2e7")

    for chave, valor in dados_extras.items():
        ficha_do_guerreiro.add_column(header=chave, style="#f5c2e7", header_style="#f5c2e7")
        print(f"a chave {chave} foi adicionada na tabela da ficha do guerreiro e irá receber o valor {valor} em breve!")

    return ficha_do_guerreiro
