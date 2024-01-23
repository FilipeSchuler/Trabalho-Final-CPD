import csv
from arquivos import *
from arvores import *
from paginas import *

class Clube:
    def __init__(self, arvore_b):
        self.nome_clube = 'Inválido'
        self.lista_jogadores = []
        self.numero_jogadores = 0
        self.arvore_jogadores = arvore_b


    def adicionar_clube_em_lista(self, arvore_times, lista):
        self.nome_clube = self.validar_nome_clube(arvore_times, lista)
        meus_clubes = []
        #Le clubes já criado para reescreve-los adicionados do novo clube criado
        coluna_desejada = ['meus_clubes']
        meus_clubes = manipulador_arq.ler_arquivo_csv(lista, coluna_desejada, ler_cabecalho=True)

        if self.nome_clube not in meus_clubes:
            meus_clubes.append(self.nome_clube)
        
        manipulador_arq.escrever_lista_em_csv(lista,meus_clubes)
        

    def validar_nome_clube(self, arvore_times, lista):
        print('Digite o nome do seu time: ')
        nome_valido = False

        while not nome_valido:
            self.nome_clube = input()
            time_existente_csv = False
            time_existente_arvore = False

            #Verifica se o nome do clube está no arquivo csv contendo todos MEUS CLUBES
            with open(lista, 'r', newline='', encoding='utf-8') as arq_csv:
                leitor_csv = csv.DictReader(arq_csv)
                for linha in leitor_csv:
                    if linha['meus_clubes'] == self.nome_clube:
                        print('Já existe um time com esse nome!\n')
                        print('Digite o nome do seu time: ')
                        time_existente_csv = True
                        break
            
            #Verifica se o nome do clube está na arvore de clubes do FIFA
            if not time_existente_csv:
                times_existentes = arvore_times.buscar_substring(self.nome_clube)
                if times_existentes:
                    print('Já existe um time com esse nome!\n')
                    print('Digite o nome do seu time: ')
                    time_existente_arvore = True

            #Se não estiver em nenhum lugar o nome do clube é válido
            if not time_existente_csv and not time_existente_arvore:
                arvore_times.inserir(self.nome_clube)
                nome_valido = True

        return self.nome_clube
    

    def adicionar_jogador(self):
        #1- Buscar jogador
        #   -Campo de busca (nome parcial, nacionalidade ou clube parcial) + Filtro (overall ou idade,ambos crescentes ou decrescentes)
        #receber como retorno o nome do jogador e seus dados
        
        while self.numero_jogadores < 11:
            #Buscas por campo de pesquisa e filtros
            arvore_jogadores_encontrados = ArvoreB(3)
            campo_pesquisa = input('Digite arvore_b.um nome, uma nacionalidade ou um clube:\nCampo de Pesquisa: ')
            opcao_filtro = selecionar_filtro()
            
            #Busca na árvore conforme os filtros e retorna uma lista de jogadores que se enquadram
            jogadores_encontrados = self.buscar_jogadores(campo_pesquisa, opcao_filtro, arvore_jogadores_encontrados)
            print(f'\nID DO JOGADOR ESCOLHIDO {jogadores_encontrados}\n')
            
            jogador_escolhido = self.escolher_jogador(opcao_filtro, jogadores_encontrados, arvore_jogadores_encontrados)
            

            if jogador_escolhido == 'imprimir':
                jogador_escolhido = input('Se deseja adicionar algum jogador digite seu ID\n'
                                          'Se deseja fazer uma nova busca tecle "b"\n')
            #'b' por causa que a escolha do usuario dps de imprimir todos jogadores só é feita logo acima
            if jogador_escolhido == 'b' or jogador_escolhido == 'nova_busca': 
                                         
                print('\nENTROU ONDE DEVIA E PROXIMA LINHA DEVE SER CAMPO DE PESQUISA\n\n')
                continue
            

            else:
                self.numero_jogadores += 1
                print(f'\nID JOGADOR ESCOLHIDO: {jogador_escolhido} - NUM JOGADORES NO MEU CLUBE -{self.numero_jogadores}\n')
                continue

        

    def buscar_jogadores(self, campo_pesquisa, opcao_filtro, arvore_jogadores_encontrados):

        jogadores_encontrados = arvore_jogadores_encontrados.buscar_em_arvores(campo_pesquisa, opcao_filtro)

        return jogadores_encontrados
        


    def escolher_jogador(self, opcao_filtro, jogadores_encontrados, arvore_jogadores_encontrados):
        jogador_escolhido = False
        while jogador_escolhido == False:
            
            if opcao_filtro == '1':
                escolha_usuario = percorrer_e_imprimir(arvore_jogadores_encontrados.raiz, 'overall', 'decrescente')
            elif opcao_filtro == '2':
                escolha_usuario = percorrer_e_imprimir(arvore_jogadores_encontrados.raiz, 'overall', 'crescente')
            elif opcao_filtro == '3':
                escolha_usuario = percorrer_e_imprimir(arvore_jogadores_encontrados.raiz, 'age', 'decrescente')
            elif opcao_filtro == '4':
                escolha_usuario = percorrer_e_imprimir(arvore_jogadores_encontrados.raiz, 'age', 'crescente')

            # # Verificar se a busca foi interrompida devido à paginação
            # escolha_usuario = controle_paginas.paginacao()

            #print(f'\nESCOLHA NA FUNÇÃO ESCOLHER{escolha_usuario}\n')

            if escolha_usuario == 'nova_busca':
                # Voltar ao início do loop para uma nova busca
                return 'nova_busca'
            elif escolha_usuario == 'imprimir':
                return 'imprimir'
            else:
                #print(f'\nLISTA DE JOGADORES ENCONTRADOS{jogadores_encontrados}\n')
                #print(f'\nESCOLHA NA FUNÇÃO ESCOLHER{jogadores_encontrados[2]}\n')
                # Retornar o ID do jogador e sair do loop
                for col in jogadores_encontrados:  # 2 é o índice que contém os IDs dos jogadores na lista
                    for ident in col:  # Agora, iteramos diretamente sobre os elementos da sublist
                        # Divide a string em partes usando a vírgula como delimitador
                        partes = ident.split(',')
                        # Extrai a ID do jogador
                        id_jogador = partes[2]
                        # Compara com a escolha do usuário
                        if id_jogador == escolha_usuario:
                            jogador_escolhido = True
                            break  # Se encontrado, sai do loop interno
                    if jogador_escolhido:
                        break  # Se encontrado, sai do loop externo

        
        return escolha_usuario
    
def selecionar_filtro():
    opcao_valida = False
    while opcao_valida == False:
        opcao_filtro = input('\nInformação do Campo de Pesquisa salvo!\n'
                        'Deseja que os jogadores encontrados sejam visualizados de qual maneira?\n'
                        '1. Ordenados por overall decrescente\n2. Ordenados por overall crescente\n'
                        '3. Ordenados por idade decrescente\n4. Ordenados por idade crescente\n')
        if opcao_filtro == '1' or opcao_filtro == '2' or opcao_filtro == '3' or opcao_filtro == '4':
            opcao_valida = True
        else:
            print('\nOpcão inválida!\n')
            opcao_valida = False

    return opcao_filtro





