import csv
from arquivos import *
from arvores import *

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
        meus_clubes = manipulador_arq.ler_arquivo_csv(lista, coluna_desejada)

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
        jogadores_encontrados = self.buscar_jogador()
        print(jogadores_encontrados)
        
        #self.lista_jogadores.append(jogador_encontrado) #append retorno da função de busca
        
        self.numero_jogadores += 1

    def buscar_jogador(self):
        campo_pesquisa = input('Digite um nome, uma nacionalidade ou um clube:\nCampo de Pesquisa: ')
        
        opcao_filtro = selecionar_filtro()

        jogadores_encontrados = self.arvore_jogadores.buscar_em_arvores(campo_pesquisa, opcao_filtro)
        if opcao_filtro == '1':
            print(self.arvore_jogadores.obter_dados_arvore_b())
            self.arvore_jogadores.percorrer_e_imprimir('overall', 'decrescente')

        return jogadores_encontrados
    
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





