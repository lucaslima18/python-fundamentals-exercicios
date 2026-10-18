"""Ponto de entrada do rastreador de ki."""

import questionary
from rich import print
from rich.console import Console
from rich.table import Table

from rastreador_de_ki.ficha_do_guerreiro import cadastrar_guerreiro, criar_tabela_basica, valida_lendario, valida_nivel_ki, valida_saiyajin, valida_supersaiyajin
from rastreador_de_ki.menu import exibir_menu, valida_opcao_menu

if __name__ == "__main__":
    console: Console = Console()

    while True:
        exibir_menu()
        opcao: int = int(questionary.text("Digite o Número correspondente a opção desejada: ", validate=lambda texto: texto in ("1", "2") or "Opção inválida").ask())
        print("---\n\n")

        opcao_escolhida: (str | bool | None) = valida_opcao_menu(opcao=opcao)

        if opcao_escolhida:
            nome_do_guerreiro, ki_base, raca, dados_extras = cadastrar_guerreiro("cidade natal", "comida favorita do guerreiro")
            nivel_ki: str = valida_nivel_ki(ki_base=ki_base)
            e_saiyajin: str = valida_saiyajin(raca=raca)
            e_lendario: str = valida_lendario(ki_base=ki_base, e_saiyajin=e_saiyajin)
            e_supersaiyajin: str = valida_supersaiyajin(nivel_ki=nivel_ki, e_saiyajin=e_saiyajin)
            ficha_do_guerreiro: Table = criar_tabela_basica(**dados_extras)

            # TODO: transformar este bloco em funcoes
            # valida se o guerreiro pode virar um supersaiyajin para criar as colunas dinamicamente e inserir os dados nela
            if e_supersaiyajin == "Este guerreiro pode virar um supersaiyajin!!!":
                # criação das colunas baseadas no nível de supersaiyajin
                for nivel in range(1, 5):
                    ficha_do_guerreiro.add_column(header=f"Ki Super Saiyajin {nivel}", style="#f5c2e7", header_style="#f5c2e7")

                # cálculo dos valores de ki supersaiyajin e preenchimento das colunas com as linhas contendo os valores dinamicos de ki correspondentes ao nivel
                kis_transformados = [str(ki_base * (nivel * 50)) for nivel in range(1, 5)]
                ficha_do_guerreiro.add_row(
                    str(nome_do_guerreiro), str(raca), str(ki_base), str(ki_base), str(e_supersaiyajin), str(e_lendario), *kis_transformados, *dados_extras.values()
                )

            else:
                ficha_do_guerreiro.add_row(
                    str(nome_do_guerreiro), str(raca), str(ki_base), str(ki_base), str(e_supersaiyajin), str(e_lendario), *dados_extras.values()
                )

            # exibição da ficha do guerreiro
            print("---\n\n")
            console.print(ficha_do_guerreiro)
            print("---\n\n")

        if opcao_escolhida == "pare":
            break
