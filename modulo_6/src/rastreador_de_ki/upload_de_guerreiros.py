from typing import Any

import pandas as pd
from rich import print
from rich.panel import Panel
from rich.progress import track
from rich.table import Table

from rastreador_de_ki.crud_guerreiro import atualizar_guerreiro, buscar_guerreiro, criar_guerreiro
from rastreador_de_ki.utils import normalizar_strings


def importar_guerreiros(caminho: str) -> dict[str, int]:
    """Cadastra os guerreiros lidos de um arquivo CSV.

    O CSV deve ter as colunas nome_do_guerreiro, ki_base e raca.
    Guerreiros já existentes são ignorados por criar_guerreiro.

    Args:
        caminho: caminho do arquivo CSV.

    Return:
        Lista dos guerreiros cadastrados.
    """
    planilha = pd.read_csv(caminho, dtype={"ki_base": str})
    resumo: dict[str, int] = {"adicionados": 0, "atualizados": 0, "pulados": 0}
    print("[#7287fd bold italic]---\n")

    for linha in track(planilha.to_dict("records"), description="Importando guerreiros..."):
        nome_do_guerreiro = normalizar_strings(linha["nome_do_guerreiro"])
        ki_base = int(linha["ki_base"])
        raca = normalizar_strings(linha["raca"])

        if not (guerreiro := buscar_guerreiro(nome_do_guerreiro=nome_do_guerreiro)):
            criar_guerreiro(nome_do_guerreiro=nome_do_guerreiro, ki_base=ki_base, raca=raca)
            resumo["adicionados"] += 1

        elif guerreiro["ki_base"] != ki_base or guerreiro["raca"] != raca:
            atualizar_guerreiro(nome_do_guerreiro=nome_do_guerreiro, ki_base=ki_base, raca=raca)
            resumo["atualizados"] += 1

        else:
            resumo["pulados"] += 1

    return resumo


def exibir_resumo_importacao(resumo: dict[str, int]) -> Panel:
    """Monta o painel com o resumo da importação.

    Args:
        resumo: quantidades retornadas por importar_guerreiros.

    Return:
        Painel com a quantidade de guerreiros em cada categoria.
    """
    grade = Table.grid(padding=(0, 3))
    grade.add_column()
    grade.add_column(justify="right", style="bold")
    grade.add_row("[green]✅ Adicionados", str(resumo["adicionados"]))
    grade.add_row("[yellow]🔄 Atualizados", str(resumo["atualizados"]))
    grade.add_row("[#6c6f85]⛔ Duplicados (pulados)", str(resumo["pulados"]))

    return Panel(grade, title="Resumo da importação", border_style="#7287fd", expand=False)
