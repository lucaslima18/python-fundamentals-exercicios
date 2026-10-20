import os
from datetime import datetime

from rich import print

CAMINHO_LOG = "src/rastreador_de_ki/logs/rastreador_de_ki.log"


def registrar_log(mensagem: str) -> None:
    with open(CAMINHO_LOG, "a", encoding="utf-8") as arquivo:
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        arquivo.write(f"[{timestamp}] {mensagem}\n")


def exibir_log() -> None:
    if os.path.exists(CAMINHO_LOG):
        with open(CAMINHO_LOG, "r", encoding="utf-8") as arquivo_de_logs:
            print(arquivo_de_logs.read())
    else:
        print("Nenhum evento registrado ainda.")
        