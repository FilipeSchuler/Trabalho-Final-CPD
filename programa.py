from arvores import *
from clubes import *

def processar_csv(csv_entrada, csv_saida):
    informacoes_desejadas = []

    with open(csv_entrada, 'r', newline='', encoding='utf-8') as arq_csv:
        leitura_csv = csv.DictReader(arq_csv)

        # Adiciona o cabeçalho ao arquivo 
        atributos = ['sofifa_id','short_name', 'overall', 'age', 'nationality', 'club', 'player_positions']
        informacoes_desejadas.append(','.join(atributos))
        #Adiciona dados ao arquivo
        for col in leitura_csv:
            info_selecionadas = [col['sofifa_id'], col['short_name'], col['overall'], col['age'], col['nationality'],
                                  col['club'], col['player_positions']]
            informacoes_desejadas.append(','.join(info_selecionadas))

    with open(csv_saida, 'w', encoding='utf-8') as arq_csv:
        for info in informacoes_desejadas:
            arq_csv.write(info + '\n')

def prep_arq_aux(arq_entrada, coluna, strings, arq_saida):
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
            filtro = 'overall'
            arvore_b = arvoreB_overall
            lista = lista_overall
            ordem = 'crescente'
        
            selecao_valida = True
        elif selecao_filtro == '2':
            filtro = 'overall'
            arvore_b = arvoreB_overall
            lista = lista_overall
            ordem = 'decrescente'

            selecao_valida = True
        elif selecao_filtro == '3':
            filtro = 'age'
            arvore_b = arvoreB_idade
            lista = lista_idade
            ordem = 'crescente'

            selecao_valida = True
        elif selecao_filtro == '4':
            filtro = 'age'
            arvore_b = arvoreB_idade
            lista = lista_idade
            ordem = 'decrescente'

            selecao_valida = True
        else:
            print('Opção inválida!')
        
    aplicar_filtros(entrada_teclado, filtro, ordem, lista, arvore_b)


def aplicar_filtros(entrada_teclado, filtro, ordem, lista, arvore_b):
    #### **** MELHORIA -> Pensar maneira pra nao repetir nomes - Pesquisa = in -> Schweinsteiger aparece 3x (?)
    if entrada_teclado == '':
        arvore_b.criar_arvore_b(coluna=str(filtro), arq_entrada=poucos_dados, arq_saida=lista)
        if ordem == 'crescente':
            arvore_b.percorrer_e_imprimir_crescente()
        if ordem == 'decrescente':
            arvore_b.percorrer_e_imprimir_decrescente()

    else:
        palavras_encontradas = arvoreTrie_nome_jogador.buscar_substring(entrada_teclado)
        if palavras_encontradas != []:
            print(f"Palavras que contêm a substring '{entrada_teclado}': {palavras_encontradas}")
            prep_arq_aux(arq_entrada=poucos_dados, coluna='short_name', strings=palavras_encontradas,arq_saida=arq_aux_dados)
            arvore_b.criar_arvore_b(coluna=str(filtro), arq_entrada=arq_aux_dados, arq_saida=lista)
            if ordem == 'crescente':
                arvore_b.percorrer_e_imprimir_crescente()
            if ordem == 'decrescente':
                arvore_b.percorrer_e_imprimir_decrescente()

        palavras_encontradas = arvoreTrie_nacionalidade.buscar_substring(entrada_teclado)
        if palavras_encontradas != []:
            prep_arq_aux(arq_entrada=poucos_dados, coluna='nationality', strings=palavras_encontradas,arq_saida=arq_aux_dados)
            arvore_b.criar_arvore_b(coluna=str(filtro), arq_entrada=arq_aux_dados, arq_saida=lista)
            if ordem == 'crescente':
                arvore_b.percorrer_e_imprimir_crescente()
            if ordem == 'decrescente':
                arvore_b.percorrer_e_imprimir_decrescente()

        palavras_encontradas = arvoreTrie_clube.buscar_substring(entrada_teclado)
        if palavras_encontradas != []:
            prep_arq_aux(arq_entrada=poucos_dados, coluna='club', strings=palavras_encontradas,arq_saida=arq_aux_dados)
            arvore_b.criar_arvore_b(coluna=str(filtro), arq_entrada=arq_aux_dados, arq_saida=lista)
            if ordem == 'crescente':
                arvore_b.percorrer_e_imprimir_crescente()
            if ordem == 'decrescente':
                arvore_b.percorrer_e_imprimir_decrescente()


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

#Seleciona quais dados serão usados
#processar_csv(csv_entrada, arquivo_dos_dados)

#Inicializa/cria as árvores Trie
arvoreTrie_nome_jogador = ArvoreTrie()
arvoreTrie_nome_jogador.criar_arvore_trie(coluna=1, arq_entrada=poucos_dados, arq_saida=lista_nomes)

arvoreTrie_nacionalidade = ArvoreTrie()
arvoreTrie_nacionalidade.criar_arvore_trie(coluna=4,arq_entrada=poucos_dados,arq_saida=lista_nacionalidades)

arvoreTrie_clube = ArvoreTrie()
arvoreTrie_clube.criar_arvore_trie(coluna=5, arq_entrada=poucos_dados, arq_saida=lista_clubes)


arvoreB_overall = ArvoreB(3)
arvoreB_idade = ArvoreB(3)
arvore_b = ArvoreB(3)


############### MENU ################### Não foi criada uma função menu() pois seriam mtos parametros para passar
opcao_valida = False
while(opcao_valida == False):
    print('Selecione uma opção:\n'
        '1. Criar time\n'
        '2. Excluir time\n'
        '3. Estatísticas\n')
    opcao_menu = input()
    
    #Criar novo clube
    if opcao_menu == '1':
        opcao_valida == True
        #Instacia um clube novo e da um nome à ele
        novo_clube = Clube()
        novo_clube.criar_clube(arvoreTrie_clube, lista_meus_clubes)
        #Adiciona jogadores ao clube novo
        buscar_jogador()
        novo_clube.adicionar_jogador()
          
    elif opcao_menu == '2':
        opcao_valida == True
        tela_excluir_time()
    elif opcao_menu == '3':
        opcao_valida == True
        tela_estatisticas()
    else:
        print('Opção inválida!\n')

























#### **** Não repete jogadores, mas não funciona para busca por prefixos - Pesquisa = Bra -> não encontra Brazil

# #Retorna true se a nacionalidade foi encontrada na lista de nacionalidades
# if arvoreTrie_nacionalidade.buscar(entrada_teclado) == True: 
#     #Cria arvore com base de dados na nacionalidade escolhida
#     prepara_aux_dados(arq_entrada=poucos_dados, coluna='nationality', entrada_teclado=entrada_teclado,arq_saida=arq_aux_dados)
#     arvore_b.criar_arvore_b(coluna=str(filtro), arq_entrada=arq_aux_dados, arq_saida=lista)
#     if ordem == 'crescente':
#         arvore_b.percorrer_e_imprimir_crescente()
#     if ordem == 'decrescente':
#         arvore_b.percorrer_e_imprimir_decrescente()
        
# elif arvoreTrie_nome_jogador.buscar(entrada_teclado) == True:
#     #Cria arvore com base de dados do prefixo de nome escolhido
#     prepara_aux_dados(arq_entrada=poucos_dados, coluna='short_name', entrada_teclado=entrada_teclado,arq_saida=arq_aux_dados)
#     arvore_b.criar_arvore_b(coluna=str(filtro), arq_entrada=arq_aux_dados, arq_saida=lista)
#     if ordem == 'crescente':
#         arvore_b.percorrer_e_imprimir_crescente()
#     if ordem == 'decrescente':
#         arvore_b.percorrer_e_imprimir_decrescente()

# elif arvoreTrie_clube.buscar(entrada_teclado) == True:
#     #Cria arvore com base de dados do prefixo do clube escolhido
#     prepara_aux_dados(arq_entrada=poucos_dados, coluna='club', entrada_teclado=entrada_teclado,arq_saida=arq_aux_dados)
#     arvore_b.criar_arvore_b(coluna=str(filtro), arq_entrada=arq_aux_dados, arq_saida=lista)
#     if ordem == 'crescente':
#         arvore_b.percorrer_e_imprimir_crescente()
#     if ordem == 'decrescente':
#         arvore_b.percorrer_e_imprimir_decrescente()
