import questionary

from rastreador_de_ki.menu import exibir_menu, realizar_acao
from rastreador_de_ki.utils import nova_tela

if __name__ == "__main__":
    while True:
        nova_tela()
        exibir_menu()
        opcao: int = int(
            questionary.text(
                "Digite o número correspondente à opção desejada: ", validate=lambda texto: texto in ("1", "2", "3", "4", "5", "6", "0") or "Opção inválida"
            ).ask()
        )
        nova_tela()
        acao = realizar_acao(opcao=opcao)

        if not acao:
            break
