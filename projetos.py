import json
from time import sleep
from interface import cabecalho, carrega, leiaint, limpa_tela, lin, menu


def novo_projeto(nome, descricao, etapas, arquivo_projeto, etapas_finalizadas):
    projeto = {
        'nome':nome,
        'descricao':descricao,
        'projeto concluido':'nao' if etapas_finalizadas != len(etapas) else 'sim',
        'etapas':etapas
    }

    # Carregando os projetos existentes
    with open(arquivo_projeto) as projetos:
        try:
            todos_projetos = json.load(projetos)
        except:
            todos_projetos = {}
    
    # Cadastrando novo projeto
    todos_projetos[f'projeto{len(todos_projetos) + 1}'] = projeto
    todos_projetos = json.dumps(todos_projetos, indent=4)

    with open(arquivo_projeto, 'w') as projetos:
        projetos.write(todos_projetos)
    
    carrega('\033[32;1mCriando projeto\033[m', 0.5)

    print('\033[32;1mProjeto criado com sucesso!\033[m')
    sleep(1)

    limpa_tela()


def nomes_projetos(arquivo_projetos):
    with open(arquivo_projetos) as projetos:
        projetos = json.load(projetos)
    
    cabecalho('\033[33;1mSeus projetos\033[m'.center(49))

    for idx, projeto in enumerate(projetos.values()):
        print(f'\033[33;1m{idx + 1} \033[;1m - \033[32;1m{projeto["nome"]}\033[m')
    lin()


def existe_projeto(nome_projeto, arquivo_projetos):
    with open(arquivo_projetos) as projetos:
        projetos = json.load(projetos)

    for projeto in projetos.values():
        if projeto['nome'] == nome_projeto:
            return True
    
    return False


def mostra_etapas(projeto, arquivo_projetos):
    with open(arquivo_projetos) as projetos:
        projetos = json.load(projetos)

    cabecalho(f'\033[33;1mEtapas do projeto {projeto}\033[m'.center(49))
    
    for pjt in projetos.values():
        if pjt['nome'] == projeto:
            for idx, etp in enumerate(pjt['etapas']):
                print(f'\033[33;1m{idx + 1} - \033[34;1m{etp[f"etapa{idx + 1}"]}\033[m')


def existe_etapa(num_etapa, projeto, arquivo_projetos):
    with open(arquivo_projetos) as projetos:
        projetos = json.load(projetos)
    
    tot_etapas = 0

    for pjt in projetos.values():
        if pjt['nome'] == projeto:
            for etp in pjt['etapas']:
                tot_etapas += 1
    
    if num_etapa > 0:
        if tot_etapas >= num_etapa:
            return True
        else:
            return False
    else:
        return False
    

def completa_etapa(num_etapa, projeto, arquivo_projetos):
    with open(arquivo_projetos) as projetos:
        projetos = json.load(projetos)
    
    # Verificando se é etapa escolhida pelo usuario
    for pjt in projetos.values():
        if pjt['nome'] == projeto:
            for idx, etp in enumerate(pjt['etapas']):
                if idx + 1 == num_etapa:
                    etp['concluida'] = 'sim'
    
    # Salvando as modificações feitas
    projetos = json.dumps(projetos, indent=4)

    with open(arquivo_projetos, 'w') as pjts:
        pjts.write(projetos)


def nova_etapa(projeto, nome_etapa, arquivo_projetos):
    with open(arquivo_projetos) as projetos:
        projetos = json.load(projetos)
    
    # Adicionando a nova etapa ao projeto
    for pjt in projetos.values():
        if pjt['nome'] == projeto:
            etapa = {
                f'etapa{len(pjt["etapas"]) + 1}':nome_etapa,
                'concluida':'nao'
            }

            pjt['etapas'].append(etapa)
    
    # Salvando as modificações
    projetos = json.dumps(projetos, indent=4)

    with open(arquivo_projetos, 'w') as pjts:
        pjts.write(projetos)

    carrega('\033[33;1mCriando nova etapa\033[m', 0.5)
    print('\033[32;1mEtapa criada com sucesso!\033[m')

    sleep(1)
    limpa_tela()


def organiza_etapas(projeto, arquivo_projetos):
    with open(arquivo_projetos) as projetos:
        projetos = json.load(projetos)

    etapasOrganizadas = []
    etapaAtual = 1

    # Organizando as etapas
    for infoProjetos in projetos.values():
        if infoProjetos['nome'] == projeto:
            for etps in infoProjetos['etapas']:
                for etp in etps.keys():
                    etapaTemp = {}

                    etapaTemp[f'etapa{etapaAtual}'] = etps[etp]
                    etapaTemp['concluida'] = etps['concluida']

                    etapaAtual += 1

                    etapasOrganizadas.append(etapaTemp)
                    break
    
    # Salvando as modificações
    for infoProjeto in projetos.values():
        if infoProjetos['nome'] == projeto:
            infoProjetos['etapas'] = etapasOrganizadas
    
    projetos = json.dumps(projetos, indent=4)

    with open(arquivo_projetos, 'w') as file:
        file.write(projetos)
    
    carrega('\033[33;1mOrganizando etapas\033[m', 0.5)
    limpa_tela()


def deleta_etapa(num_etapa, projeto, arquivo_projetos):
    with open(arquivo_projetos) as projetos:
        projetos = json.load(projetos)
    
    for pjt in projetos.values():
        if pjt['nome'] == projeto:
            for idx, etp in enumerate(pjt['etapas']):
                if idx + 1 == num_etapa:
                    del pjt['etapas'][idx]  # Deletando a etapa
    
    # Salvando as modificações
    projetos = json.dumps(projetos, indent=4)

    with open(arquivo_projetos, 'w') as pjts:
        pjts.write(projetos)
    
    carrega('\033[33;1mSalvando alterações\033[m', 0.5)
    print('\033[32;1mAlterações salvas\033[m')

    sleep(1)
    limpa_tela()


def renomeia_projeto(projeto, arquivo_projetos, novo_nome_projeto):
    with open(arquivo_projetos) as projetos:
        projetos = json.load(projetos)

    projetos_atualizados = {}

    # Renomeando o projeto
    projetoAtual = 0
    outrosProjetos = {}

    for infoProjeto in projetos.values():
        projetoAtual += 1

        if infoProjeto['nome'] == projeto:
            for info in infoProjeto.keys():
                projetos_atualizados[info] = infoProjeto[info] if infoProjeto[info] != projeto else novo_nome_projeto
        else:
            for info in infoProjeto.keys():
                outrosProjetos[info] = infoProjeto[info]
        
        projetos_atualizados[f'projeto{projetoAtual}'] = outrosProjetos

    # Salvando alterações
    with open(arquivo_projetos, 'w') as file:
        projetos_atualizados = json.dumps(projetos_atualizados, indent=4)

        file.write(projetos_atualizados)
    
    carrega('\033[33;1mRenomeando projeto\033[m', 0.5)

    print('\033[32;1mO projeto foi renomeado com sucesso!\033[m')

    sleep(1)
    limpa_tela()
            

def modifica_projeto(arquivo_projetos):
    while True:
        nomes_projetos(arquivo_projetos)

        projeto = str(input('\033[33;1mNome do projeto que deseja modificar:\033[m ')).strip().lower()

        if not existe_projeto(projeto, arquivo_projetos):
            print(f'\033[31;1mNão existe um projeto com o nome {projeto}\033[m')
            sleep(1)

            limpa_tela()
        else:
            break
    
    while True:
        menu_modificacao = menu(
            'Completar etapa',
            'Criar nova etapa',
            'Remover etapa',
            'Renomear projeto',
            'Excluir projeto',
            'Cancelar',
            titulo_menu = 'Menu de modificação'.center(42)
        )

        if menu_modificacao > 6:
            print('\033[31;1mOpção inválida\033[m')
            sleep(1)

            limpa_tela()
        else:
            break

    match menu_modificacao:
        case 1:
            limpa_tela()

            while True:
                mostra_etapas(projeto, arquivo_projetos)
                lin()

                num_etapa = leiaint(f'Qual etapa do projeto \033[33;1m{projeto}\033[m deseja completar? (Número da etapa) ')

                lin()

                if not existe_etapa(num_etapa, projeto, arquivo_projetos):
                    print(f'\033[31;1mNão existe essa etapa no projeto {projeto}\033[m')
                    sleep(1)

                    limpa_tela()
                else:
                    break
            completa_etapa(num_etapa, projeto, arquivo_projetos)
            carrega('\033[33;1mConcluindo modificações\033[m', 0.5)

            limpa_tela()
        case 2:
            nome_etapa = str(input('Nome da etapa: ')).lower()

            nova_etapa(projeto, nome_etapa, arquivo_projetos)
        case 3:
            while True:
                mostra_etapas(projeto, arquivo_projetos)
                lin()

                num_etapa = leiaint('\033[33;1mNúmero da etapa:\033[m ')

                if not existe_etapa(num_etapa, projeto, arquivo_projetos):
                    print('\033[31;1mNão existe esta etapa!\033[m')
                else:
                    limpa_tela()
                    break

            deleta_etapa(num_etapa, projeto, arquivo_projetos)
            organiza_etapas(projeto, arquivo_projetos)
        case 4:
            nomeNovoProjeto = str(input('Renomear o projeto para: (Nome do projeto) ')).lower()

            renomeia_projeto(projeto, arquivo_projetos, nomeNovoProjeto)
        case 5:
            pass
        case 6:
            print('\033[33;1mModificação cancelada!\033[m')
            sleep(1)

            limpa_tela()


if __name__ == '__main__':
    modifica_projeto('projetos.json')