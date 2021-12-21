import os.path
from interface import carrega, confirma_opcao, leiaint, limpa_tela, lin, menu
from time import sleep
from projetos import modifica_projeto, novo_projeto

raiz = os.path.dirname(__file__)
arquivo_projetos = os.path.join(raiz, 'projetos.json')

while True:
    match menu('Criar novo projeto', 'Modificar projeto', 'sair', titulo_menu = 'Organizador de projetos'.center(42)):
        case 1:
            lin()

            nome_projeto = str(input('Nome do projeto: ')).strip().lower()
            descricao = str(input('Descrição do projeto: '))

            # Validando a quantidade de etapas que o projeto terá
            while True:
                quant_etapas = leiaint('Quantas etapas seu projeto tem? ')
                lin()

                confirma_etapa = confirma_opcao(f'Confirmando... Seu projeto tem {quant_etapas} etapas? (s/n) ')

                if confirma_etapa == 's':
                    limpa_tela()
                    break
                else:
                    limpa_tela()
            
            etapas_projeto = []

            # Adicionando as etapas do projeto
            etapas_finalizadas = 0

            for i in range(quant_etapas):
                nome_etapa = str(input(f'Diga a {i + 1}ª etapa: ')).lower()

                etapa_concluida = confirma_opcao(f'A etapa {nome_etapa} está completa? (s/n) ')

                if etapa_concluida == 's':
                    etapas_finalizadas += 1

                etapas_projeto.append(
                    {
                        f'etapa{len(etapas_projeto) +  1}':nome_etapa,
                        'concluida': 'nao' if etapa_concluida == 'n' else 'sim'
                    }
                )
                
                limpa_tela()
            
            novo_projeto(
                nome = nome_projeto,
                descricao = descricao,
                etapas = etapas_projeto,
                arquivo_projeto = arquivo_projetos,
                etapas_finalizadas = etapas_finalizadas
            )
        case 2:
            modifica_projeto(arquivo_projetos)
        case 3:
            carrega(
                msg = '\033[32;1mAté mais\033[m',
                salto = 0.5
            )

            limpa_tela()
            exit()
        case _:
            print('\033[31;1mOpção inválida\033[m')
            sleep(1.5)

            limpa_tela()