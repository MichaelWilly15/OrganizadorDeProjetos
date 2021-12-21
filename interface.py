from time import sleep


def lin(tam=42):
    print('-' * tam)


def cabecalho(msg):
    lin()
    print(msg)
    lin()


def limpa_tela():
    from sys import platform
    from os import system

    if platform == 'win32':
        system('cls')
    else:
        system('clear')


def leiaint(txt):
        try:
            num = int(input(txt))
        except ValueError:
            print('\033[31;1mSó aceitamos inteiros!\033[m')
            sleep(1.5)
            limpa_tela()

            return None
        else:
            return num


def carrega(msg, salto):
    print(msg, end='', flush=True)

    sleep(salto)
    print('.', end='', flush=True)

    sleep(salto)
    print('.', end='', flush=True)

    sleep(salto)
    print('.')

    sleep(salto)


def menu(*itens, titulo_menu):
    while True:
        cabecalho(titulo_menu)

        for idx, item in enumerate(itens):
            print(f'\033[33;1m {idx + 1} \033[m - \033[34;1m {item} \033[m')
        lin()

        opcao = leiaint('\033[34;1mSua opção: \033[m')

        if opcao:
            return opcao


def confirma_opcao(msg):
    while True:
        pergunta = str(input(msg)).lower().lstrip()[0]

        if pergunta in 'sn':
            return pergunta
        else:
            print('\033[31;1mResposta inválida\033[m')
            sleep(1)

            limpa_tela()