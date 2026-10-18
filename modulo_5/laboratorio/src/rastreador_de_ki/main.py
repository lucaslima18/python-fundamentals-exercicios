import questionary
from rich import print

from rastreador_de_ki.crud_guerreiro import atualizar_guerreiro, buscar_guerreiro, criar_guerreiro, listar_guerreiro, remover_guerreiro
from rastreador_de_ki.ficha_do_guerreiro import cadastrar_guerreiro, montar_ficha
from rastreador_de_ki.menu import exibir_menu
from rastreador_de_ki.utils import CONSOLE, nova_tela

if __name__ == "__main__":
    while True:
        nova_tela()
        exibir_menu()
        opcao: int = int(
            questionary.text(
                "Digite o número correspondente à opção desejada: ", validate=lambda texto: texto in ("1", "2", "3", "4", "5", "6") or "Opção inválida"
            ).ask()
        )
        nova_tela()

        match opcao:
            case 1:
                guerreiro = cadastrar_guerreiro()
                if dado_guerreiro := criar_guerreiro(*guerreiro):
                    CONSOLE.print(montar_ficha(guerreiros=[dado_guerreiro]))

            case 2:
                print(montar_ficha(guerreiros=listar_guerreiro()))

            case 3:
                nome_do_guerreiro = str(questionary.text("Digite o nome do guerreiro: ").ask()).lower()
                if guerreiro := buscar_guerreiro(nome_do_guerreiro):
                    CONSOLE.print(montar_ficha(guerreiros=[guerreiro]))
                else:
                    print("[italic red]O Guerreiro não foi encontrado :(")

            case 4:
                guerreiro = cadastrar_guerreiro()
                if guerreiro := atualizar_guerreiro(*guerreiro):
                    CONSOLE.print(montar_ficha(guerreiros=[guerreiro]))

            case 5:
                nome_do_guerreiro = str(questionary.text("Digite o nome do guerreiro: ").ask()).lower()
                remover_guerreiro(nome_do_guerreiro)

            case 6:
                break
        questionary.confirm("Continuar?").ask()
        print("---\n\n")
