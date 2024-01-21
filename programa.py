from arvores import *
from clubes import *


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
        


    def prep_arq_aux(self, arq_entrada, coluna, strings, arq_saida):
        with open(arq_entrada, 'r', newline='', encoding='utf-8') as arq_csv:
            leitor_csv = csv.reader(arq_csv)
            colunas = next(leitor_csv)
            indice = colunas.index(coluna)

            with open(arq_saida, 'w', newline='', encoding='utf-8') as arq_csv:
                escritor_csv = csv.writer(arq_csv)
                
                escritor_csv.writerow(colunas)

                for linha in leitor_csv:
                    for string in strings:
                        if linha[indice] == string:
                            escritor_csv.writerow(linha)



def tela_adicionar_jogador():
    print('\nTela escolha jogador\n')

def tela_excluir_time():
    print('\nTela excluir jogadorer\n')

def tela_estatisticas():
    print('\nTela estatísticas\n')


def buscar_jogador():
    print('\nSe deseja buscar uma nacionalidade digite-a no campo de busca, ou tecle enter para deixar o campo vazio')
    entrada_teclado = input('Campo de Pesquisa: ')
    ##Faz a busca do que foi digitado nas arvores trie, caso encontrado -> Cria uma arvore b filtrando dos dados
    ##gerais somente oq foi digitado no campo de pesquisa

    print('\nSelecione uma opção\n1.Ordenar por overall crescente\n2.Ordenar por overall decrescente\n'
            '3.Ordenar por idade crescente\n4.Ordenar por idade decrescente\n')

    selecao_valida = False
    while(selecao_valida == False):
        selecao_filtro = input()
        if selecao_filtro == '1':
            arvoreB_overall_C = ArvoreB(3)

            aplicar_filtros(entrada_teclado, filtro='overall', atributo='Overall', ordem='crescente', 
                            lista=lista_overall, arvore_b=arvoreB_overall_C)
            selecao_valida = True

        elif selecao_filtro == '2':
            arvoreB_overall_D = ArvoreB(3)
            aplicar_filtros(entrada_teclado, filtro='overall', atributo='Overall', ordem='decrescente', 
                            lista=lista_overall, arvore_b=arvoreB_overall_D)
            selecao_valida = True

        elif selecao_filtro == '3':
            arvoreB_idade_C = ArvoreB(3)
            aplicar_filtros(entrada_teclado, filtro='age', atributo='Idade', ordem='crescente', 
                            lista=lista_idade, arvore_b=arvoreB_idade_C)
            selecao_valida = True

        elif selecao_filtro == '4':
            arvoreB_idade_D = ArvoreB(3)
            aplicar_filtros(entrada_teclado, filtro='age', atributo='Idade', ordem='decrescente', 
                            lista=lista_idade, arvore_b=arvoreB_idade_D)
            selecao_valida = True

        else:
            print('Opção inválida!')
        
    


def aplicar_filtros(entrada_teclado, filtro, atributo, ordem, lista, arvore_b):
    #### **** MELHORIA -> Pensar maneira pra nao repetir nomes - Pesquisa = in -> Schweinsteiger aparece 3x (?)
    if entrada_teclado == '':
        arvore_b.criar_arvore_b(coluna=str(filtro), arq_entrada=poucos_dados, arq_saida=lista)
        
        arvore_b.percorrer_e_imprimir_crescente(atributo, ordem)

    else:
        palavras_encontradas = arvoreTrie_nome_jogador.buscar_substring(entrada_teclado)
        if palavras_encontradas != []:
            print(f"Palavras que contêm a substring '{entrada_teclado}': {palavras_encontradas}")
            manipulador_arq.prep_arq_aux(arq_entrada=poucos_dados, coluna='short_name', strings=palavras_encontradas,arq_saida=arq_aux_dados)
            arvore_b.criar_arvore_b(coluna=str(filtro), arq_entrada=arq_aux_dados, arq_saida=lista)
            
            arvore_b.percorrer_e_imprimir_crescente(atributo, ordem)

        palavras_encontradas = arvoreTrie_nacionalidade.buscar_substring(entrada_teclado)
        if palavras_encontradas != []:
            manipulador_arq.prep_arq_aux(arq_entrada=poucos_dados, coluna='nationality', strings=palavras_encontradas,arq_saida=arq_aux_dados)
            arvore_b.criar_arvore_b(coluna=str(filtro), arq_entrada=arq_aux_dados, arq_saida=lista)
            
            arvore_b.percorrer_e_imprimir_crescente(atributo, ordem)

        palavras_encontradas = arvoreTrie_clube.buscar_substring(entrada_teclado)
        if palavras_encontradas != []:
            manipulador_arq.prep_arq_aux(arq_entrada=poucos_dados, coluna='club', strings=palavras_encontradas,arq_saida=arq_aux_dados)
            arvore_b.criar_arvore_b(coluna=str(filtro), arq_entrada=arq_aux_dados, arq_saida=lista)
            
            arvore_b.percorrer_e_imprimir_crescente(atributo, ordem)


###################################### Inicio da aplicação ########################################
    
#Definição de alguns arquivos
csv_entrada = 'arquivos/fifa_cards.csv'
arquivo_dos_dados = 'arquivos/arquivo_dos_dados.csv'
arq_aux_dados = 'arquivos/arquivo_aux.csv'
poucos_dados = 'arquivos/poucos_dados.csv'

lista_nacionalidades = 'arquivos/lista_nac.csv'
lista_clubes = 'arquivos/lista_clubes.csv'
lista_nomes = 'arquivos/lista_nomes.csv'
lista_overall = 'arquivos/lista_overall.csv'
lista_idade = 'arquivos/lista_idade.csv'
lista_meus_clubes = 'arquivos/lista_meus_clubes.csv'


manipulador_arq = Arquivos()

#Seleciona quais dados serão usados
lista = ['sofifa_id', 'short_name', 'age', 'nationality', 'overall', 'club', 'player_positions']
manipulador_arq.processar_csv(csv_entrada, arquivo_dos_dados, lista)

#Inicializa/cria as árvores Trie
arvoreTrie_nome_jogador = ArvoreTrie()
arvoreTrie_nome_jogador.criar_arvore_trie(coluna=1, arq_entrada=poucos_dados, arq_saida=lista_nomes)

arvoreTrie_nacionalidade = ArvoreTrie()
arvoreTrie_nacionalidade.criar_arvore_trie(coluna=4,arq_entrada=poucos_dados,arq_saida=lista_nacionalidades)

arvoreTrie_clube = ArvoreTrie()
arvoreTrie_clube.criar_arvore_trie(coluna=5, arq_entrada=poucos_dados, arq_saida=lista_clubes)


############### MENU ################### Não foi criada uma função menu() pois seriam mtos parametros para passar
opcao_menu = -1
while(opcao_menu != '4'):
    print('\nSelecione uma opção:\n'
        '1. Criar time\n'
        '2. Excluir time\n'
        '3. Estatísticas\n'
        '4. Sair')
    opcao_menu = input()
    
    #Criar novo clube
    if opcao_menu == '1':
        #Instacia um clube novo e da um nome à ele
        novo_clube = Clube()
        novo_clube.criar_clube(arvoreTrie_clube, lista_meus_clubes)
        #Adiciona jogadores ao clube novo
        buscar_jogador()
        novo_clube.adicionar_jogador()
          
    elif opcao_menu == '2':
        tela_excluir_time()
    
    elif opcao_menu == '3':
        tela_estatisticas()
    
    elif opcao_menu == '4':
        print("Fechando aplicação!")

    else:
        print('Opção inválida!\n')

