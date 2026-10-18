import questionary
from rich import print
from rich.table import Table


def cadastrar_guerreiro(*dados_extras):
    nome_do_guerreiro: str = str(questionary.text("Digite o nome do Guerreiro: ").ask()).lower()
    ki_base: int = int(questionary.text("Digite o nível do KI base do guerreiro: ").ask())
    raca: str = str(questionary.text("Digite a raça do guerreiro: ").ask()).lower()
    colecao_de_dados_extras = {}

    for chave_do_dado_extra in dados_extras:
        valor_do_dado_extra = questionary.text(f"Digite {chave_do_dado_extra}: ").ask()
        colecao_de_dados_extras.update({"_".join(chave_do_dado_extra.lower().split()): valor_do_dado_extra})

    return nome_do_guerreiro, ki_base, raca, colecao_de_dados_extras


def valida_nivel_ki(ki_base):
    if ki_base < 500:
        return "O ki é considerado BAIXO!"

    if ki_base < 2000:
        return "O ki é considerado MÉDIO!"

    if ki_base < 9000:
        return "O ki é considerado ALTO!"

    return "O ki é considerado LENDÁRIO!"


def valida_saiyajin(raca):
    return "Este guerreiro é um siyajin." if raca == "saiyajin" else "Este guerreiro NÃO é um siyajin."


def valida_lendario(ki_base, e_saiyajin):
    return "Este é um guerreiro lendário!!!" if ki_base > 9000 or e_saiyajin == "Este guerreiro é um siyajin." else "Este NÃO é um guerreiro lendário :("


def valida_supersaiyajin(nivel_ki, e_saiyajin):
    if nivel_ki == "O ki é considerado ALTO!" or nivel_ki == "O ki é considerado LENDÁRIO!" and e_saiyajin == "Este guerreiro é um siyajin.":
        return "Este guerreiro pode virar um supersaiyajin!!!"
    return "Este guerreiro não pode virar um supersaiyajin :("


def criar_tabela_basica(**dados_extras):
    ficha_do_guerreiro = Table(title="FIXA DO GUERREIRO", style="#f9e2af", title_style="#b4befe")
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
