import csv


#Definição de alguns arquivos
CSV_TODOS_ATRIBUTOS = 'arquivos/fifa_cards.csv'
ARQUIVO_DADOS_DESEJADOS = 'arquivos/arquivo_dos_dados.csv'
ARQUIVO_AUXILIAR = 'arquivos/arquivo_aux.csv'
POUCOS_DADOS = 'arquivos/poucos_dados.csv'

TODAS_NACIONALIDADES= 'arquivos/lista_nac.csv'
LISTA_TODOS_CLUBES = 'arquivos/lista_clubes.csv'
LISTA_TODOS_NOMES = 'arquivos/lista_nomes.csv'
ARVORE_OVERALL = 'arquivos/lista_overall.csv'
ARVORE_IDADE = 'arquivos/lista_idade.csv'
LISTA_MEUS_CLUBES = 'arquivos/lista_meus_clubes.csv'


class Arquivos:
    
    #Exemplo de entrada para lista_de_colunas_desejadas ->atribuir valores à uma lista = ['short_name', 'age'] 
    #E depois passar a lista como parâmetro
    def ler_arquivo_csv(self, csv_entrada, lista_de_colunas_desejadas):
        conteudo_do_csv = []

        with open(csv_entrada, 'r', newline='', encoding='utf-8') as arq_csv:
            leitura_csv = csv.DictReader(arq_csv)
            
            # Adiciona o cabeçalho ao arquivo
            conteudo_do_csv.append(','.join(lista_de_colunas_desejadas))
            
            for col in leitura_csv:
                # Obtém os valores das colunas desejadas
                info_selecionadas = [col[coluna] for coluna in lista_de_colunas_desejadas]
                conteudo_do_csv.append(','.join(info_selecionadas))

        return conteudo_do_csv
    
    def escrever_lista_em_csv(self, csv_saida, lista_de_dados):
        with open(csv_saida, 'w', encoding='utf-8') as arq_csv:
            for info in lista_de_dados:
                arq_csv.write(info + '\n')
            

    def processar_csv(self, csv_entrada, csv_saida, lista_de_colunas_desejadas):
        informacoes_desejadas = []
        informacoes_desejadas = self.ler_arquivo_csv(csv_entrada, lista_de_colunas_desejadas)

        self.escrever_lista_em_csv(csv_saida, informacoes_desejadas)
        





    #Acho q não vai ser feito
    def ajustar_coluna_posicoes(arq_entrada):
        posicoes = []
        coluna_desejada = ['player_positions']
        posicoes = manipulador_arq.ler_arquivo_csv(arq_entrada, coluna_desejada)
        #Trocar as siglas e deixar só Ataque com todas siglas de ataque, defesa com todas siglas de defesa, etc
        #Problemas: tem jogadores que podem ser tanto atacantes quanto meio campistas
        #Não vejo vantagem em fazer, a não ser pra ficar "mais bonito"
        return
    






    def prep_arq_aux(self, arq_entrada, coluna, strings, arq_saida):
        with open(arq_entrada, 'r', newline='', encoding='utf-8') as arq_csv:
            leitor_csv = csv.reader(arq_csv)
            colunas = next(leitor_csv)  #Pula cabeçalho
            indice = colunas.index(coluna)

            with open(arq_saida, 'w', newline='', encoding='utf-8') as arq_csv:
                escritor_csv = csv.writer(arq_csv)
                
                escritor_csv.writerow(colunas)

                for linha in leitor_csv:
                    for string in strings:
                        if linha[indice] == string:
                            escritor_csv.writerow(linha)


manipulador_arq = Arquivos()