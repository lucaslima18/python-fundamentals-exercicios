import questionary

from rastreador_de_ki.logs import registrar_log
from rastreador_de_ki.menu import exibir_menu, realizar_acao
from rastreador_de_ki.utils import nova_tela

if __name__ == "__main__":
    while True:
        registrar_log("Iniciando rastreador de ki")
        nova_tela()
        exibir_menu()
        opcao: int = int(
            questionary.text(
                "Digite o Número correspondente a opção desejada: ", validate=lambda texto: texto in ("1", "2", "3", "4", "5", "6", "0") or "Opção inválida"
            ).ask()
        )
        nova_tela()
        registrar_log(f"Opcao registrada pelo usuário: {opcao}")

        acao = realizar_acao(opcao=opcao)

        if not acao:
            registrar_log("Finalizando execução do rastreador de ki")
            break
