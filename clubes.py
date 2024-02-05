from arquivos import *
from arvores import *
from paginas import *

TOTAL_JOGADORES_POR_CLUBE = 2

class Clube:
    def __init__(self):
        self.nome_clube = 'Inválido'
        self.numero_jogadores = 0
        self.arvore_jogadores = ArvoreB(3)


    def adicionar_clube_em_lista(self, arvore_times, arvore_meus_clubes):
        self.nome_clube = self.validar_nome_clube(arvore_times, arvore_meus_clubes)
        
        return self.nome_clube


    def validar_nome_clube(self, arvore_times, arvore_meus_clubes):
        nome_valido = False

        while not nome_valido:
            self.nome_clube = input('Digite o nome do seu time: ')
            time_existente_csv = False
            time_existente_arvore = False
            time_existente_meus_clubes = False

            if not time_existente_meus_clubes:
                times_existentes = arvore_meus_clubes.buscar_substring(self.nome_clube)
                if times_existentes:
                    print('Já existe um time com esse nome!\n')
                    time_existente_meus_clubes = True 
            
            #Verifica se o nome do clube está na arvore de clubes do FIFA
            if not time_existente_meus_clubes:
                times_existentes = arvore_times.buscar_substring(self.nome_clube)
                if times_existentes:
                    print('Já existe um time com esse nome!\n')
                    time_existente_arvore = True

            #Se não estiver em nenhum lugar o nome do clube é válido
            if not time_existente_meus_clubes and not time_existente_arvore:
                #arvore_times.inserir(self.nome_clube)
                nome_valido = True

        return self.nome_clube
    

    def adicionar_jogador(self):
        #1- Buscar jogador
        #   -Campo de busca (nome parcial, nacionalidade ou clube parcial) + Filtro (overall ou idade,ambos crescentes ou decrescentes)
        #receber como retorno o nome do jogador e seus dados
        while self.numero_jogadores < TOTAL_JOGADORES_POR_CLUBE:
            #Buscas por campo de pesquisa e filtros
            arvore_jogadores_encontrados = ArvoreB(3)
            campo_pesquisa = input('Digite um nome, uma nacionalidade ou um clube:\nCampo de Pesquisa: ')
            opcao_filtro = selecionar_filtro()
            
            #Busca na árvore conforme os filtros e retorna uma lista de jogadores que se enquadram
            jogadores_encontrados = self.buscar_jogadores(campo_pesquisa, opcao_filtro, arvore_jogadores_encontrados)
            
            jogador_escolhido = self.escolher_jogador(opcao_filtro, arvore_jogadores_encontrados)
            

            if jogador_escolhido == 'imprimir':
                jogador_escolhido = input('\nSe deseja adicionar algum jogador digite seu ID\n'
                                            'Se deseja fazer uma nova busca tecle "b"\n'
                                            'Selecione uma das opções acima: ')
                print('\n') #print para formatação no terminal ficar certinho
            #'b' por causa que a escolha do usuario dps de imprimir todos jogadores só é feita logo acima
            if jogador_escolhido == 'b' or jogador_escolhido == 'nova_busca': 
                continue
            
            #Adiciona jogadores de fato
            else:
                jogador_valido = verifica_id_do_jogador(jogadores_encontrados, jogador_escolhido)
                if jogador_valido:
                    arvore_jogadores = arvoreTrie_meus_clubes.buscar_raiz_arvore_b(self.nome_clube)
                    dados_jogador = manipulador_arq.procurar_id_na_lista(ARQUIVO_DADOS_DESEJADOS, jogador_escolhido)

                    for dado in dados_jogador:
                        arvore_jogadores.inserir(dado)

                    self.numero_jogadores += 1
                    print('Jogador adicionado ao seu time!')
                    print(f'Jogadores no seu clube: {self.numero_jogadores} de {TOTAL_JOGADORES_POR_CLUBE}\n')
                else:
                    print('O ID fornecido não foi encontrado!')
                continue
        


    def buscar_jogadores(self, campo_pesquisa, opcao_filtro, arvore_jogadores_encontrados):

        jogadores_encontrados = arvore_jogadores_encontrados.buscar_em_arvores(campo_pesquisa, opcao_filtro)

        return jogadores_encontrados
    

    def escolher_jogador(self, opcao_filtro, arvore_jogadores_encontrados):
            
        if opcao_filtro == '1':
            escolha_usuario = percorrer_e_imprimir(arvore_jogadores_encontrados.raiz, 'overall', 'decrescente')
        elif opcao_filtro == '2':
            escolha_usuario = percorrer_e_imprimir(arvore_jogadores_encontrados.raiz, 'overall', 'crescente')
        elif opcao_filtro == '3':
            escolha_usuario = percorrer_e_imprimir(arvore_jogadores_encontrados.raiz, 'age', 'decrescente')
        elif opcao_filtro == '4':
            escolha_usuario = percorrer_e_imprimir(arvore_jogadores_encontrados.raiz, 'age', 'crescente')


        if escolha_usuario == 'nova_busca':
            # Voltar ao início do loop para uma nova busca
            return 'nova_busca'
        elif escolha_usuario == 'imprimir':
            return 'imprimir'
        else:
            # Retornar o ID do jogador e sair do loop
            return escolha_usuario
    

def verifica_id_do_jogador(jogadores_encontrados, jogador_escolhido):
    jogador_valido = False

    for col in jogadores_encontrados:  # 2 é o índice que contém os IDs dos jogadores na lista
        for ident in col:  # Agora, iteramos diretamente sobre os elementos da sublist
            # Divide a string em partes usando a vírgula como delimitador
            partes = ident.split(',')
            # Extrai a ID do jogador
            id_jogador = partes[2]
            # Compara com a escolha do usuário
            if id_jogador == str(jogador_escolhido):
                jogador_valido = True
                break  # Se encontrado, sai do loop interno
        if jogador_valido:
            break  # Se encontrado, sai do loop externo
    return jogador_valido


def selecionar_filtro():
    opcao_valida = False
    while opcao_valida == False:
        opcao_filtro = input('\nOpções disponíveis:\n'
                            '1. Ordenados por overall decrescente\n2. Ordenados por overall crescente\n'
                            '3. Ordenados por idade decrescente\n4. Ordenados por idade crescente\n'
                            '\nDeseja que os jogadores encontrados sejam visualizados de qual maneira? ')
        print('\n') #print para formatação no terminal ficar certinha
                        
        if opcao_filtro == '1' or opcao_filtro == '2' or opcao_filtro == '3' or opcao_filtro == '4':
            opcao_valida = True
        else:
            print('\nOpcão inválida!\n')
            opcao_valida = False

    return opcao_filtro





