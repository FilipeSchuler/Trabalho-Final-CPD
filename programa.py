from arvores import *
from clubes import *
from arquivos import *
from paginas import *






def tela_criar_time():
    #arvore_b = ArvoreB(3)  #Instancia uma árvore de jogadores para cada clube 
                                #isso facilita a busca de dados para cada clube
    

    novo_clube = Clube()        #Instacia um clube novo e da um nome à ele
    novo_clube.adicionar_clube_em_lista(arvoreTrie_clube, LISTA_MEUS_CLUBES)        #Adiciona clube em meus clubes
    novo_clube.adicionar_jogador()         #Adiciona jogadores ao clube novo

def tela_excluir_time():
    print('\nLista de times criados:\n')

    manipulador_arq.imprimir_lista_meus_clubes() 
    
    nome_time_para_excluir = input('\nDigite o nome do time que você deseja excluir: ')

    time_valido = manipulador_arq.compara_nome_com_lista(LISTA_MEUS_CLUBES, nome_time_para_excluir, 'meus_clubes')

    if time_valido == True:
        #implementar logica excluir time
        print(f'\nTime "{nome_time_para_excluir}" excluido!\n')
    else:
        print('Esse time não existe!\n')

    

def tela_estatisticas():
    print('\nTela estatísticas\n')
    manipulador_arq.imprimir_lista_meus_clubes() 
    
    nome_time_para_estatisticas = input('\nDigite o nome do time que você deseja ver as estatísticas: ')

    time_valido = manipulador_arq.compara_nome_com_lista(LISTA_MEUS_CLUBES, nome_time_para_estatisticas, 'meus_clubes')

    if time_valido == True:
        print(f'\nEstatísticas do time "{nome_time_para_estatisticas}":\n')
        #implementar logica para calcular estatisticas do time
    else:
        print('Esse time não existe!\n')



        
    





###################################### Inicio da aplicação ########################################
controle_pag = ControlePaginas()
manipulador_arq = Arquivos()    #Usado para manipular arquivos csv e listas - Traduções num geral
colunas_desejadas = ['sofifa_id', 'short_name', 'age', 'nationality', 'overall', 
                     'club', 'player_positions']    #Seleciona quais dados serão usados

manipulador_arq.processar_csv(CSV_TODOS_ATRIBUTOS, ARQUIVO_DADOS_DESEJADOS, colunas_desejadas)

##### MENU #####
opcao_menu = None
while(opcao_menu != '4'):
    print('\nSelecione uma opção:\n1. Criar time\n2. Excluir time\n3. Estatísticas\n4. Sair\n')
    
    opcao_menu = input()
    #Criar novo clube
    if opcao_menu == '1':
        tela_criar_time()
    #Excluir clube      
    elif opcao_menu == '2':
        tela_excluir_time()
    #Calcular e mostrar estatísticas
    elif opcao_menu == '3':
        tela_estatisticas()
    #Sair da aplicação
    elif opcao_menu == '4':
        print("Fechando aplicação!")

    else:
        print('Opção inválida!\n')

































# def buscar_jogador():
#     print('\nSe deseja buscar uma nacionalidade digite-a no campo de busca, ou tecle enter para deixar o campo vazio')
#     entrada_teclado = input('Campo de Pesquisa: ')
#     ##Faz a busca do que foi digitado nas arvores trie, caso encontrado -> Cria uma arvore b filtrando dos dados
#     ##gerais somente oq foi digitado no campo de pesquisa

#     print('\nSelecione uma opção\n1.Ordenar por overall crescente\n2.Ordenar por overall decrescente\n'
#             '3.Ordenar por idade crescente\n4.Ordenar por idade decrescente\n')

#     selecao_valida = False
#     while(selecao_valida == False):
#         selecao_filtro = input()
#         if selecao_filtro == '1':
#             arvoreB_overall_C = ArvoreB(3)

#             aplicar_filtros(entrada_teclado, filtro='overall', atributo='Overall', ordem='crescente', 
#                             lista=lista_overall, arvore_b=arvoreB_overall_C)
#             selecao_valida = True

#         elif selecao_filtro == '2':
#             arvoreB_overall_D = ArvoreB(3)
#             aplicar_filtros(entrada_teclado, filtro='overall', atributo='Overall', ordem='decrescente', 
#                             lista=lista_overall, arvore_b=arvoreB_overall_D)
#             selecao_valida = True

#         elif selecao_filtro == '3':
#             arvoreB_idade_C = ArvoreB(3)
#             aplicar_filtros(entrada_teclado, filtro='age', atributo='Idade', ordem='crescente', 
#                             lista=lista_idade, arvore_b=arvoreB_idade_C)
#             selecao_valida = True

#         elif selecao_filtro == '4':
#             arvoreB_idade_D = ArvoreB(3)
#             aplicar_filtros(entrada_teclado, filtro='age', atributo='Idade', ordem='decrescente', 
#                             lista=lista_idade, arvore_b=arvoreB_idade_D)
#             selecao_valida = True

#         else:
#             print('Opção inválida!')
        

# def aplicar_filtros(entrada_teclado, filtro, atributo, ordem, lista, arvore_b):
#     #### **** MELHORIA -> Pensar maneira pra nao repetir nomes - Pesquisa = in -> Schweinsteiger aparece 3x (?)
#     if entrada_teclado == '':
#         arvore_b.criar_arvore_b(coluna=str(filtro), arq_entrada=poucos_dados, arq_saida=lista)
        
#         arvore_b.percorrer_e_imprimir_crescente(atributo, ordem)

#     else:
#         palavras_encontradas = arvoreTrie_nome_jogador.buscar_substring(entrada_teclado)
#         if palavras_encontradas != []:
#             print(f"Palavras que contêm a substring '{entrada_teclado}': {palavras_encontradas}")
#             manipulador_arq.prep_arq_aux(arq_entrada=poucos_dados, coluna='short_name', strings=palavras_encontradas,arq_saida=arq_aux_dados)
#             arvore_b.criar_arvore_b(coluna=str(filtro), arq_entrada=arq_aux_dados, arq_saida=lista)
            
#             arvore_b.percorrer_e_imprimir_crescente(atributo, ordem)

#         palavras_encontradas = arvoreTrie_nacionalidade.buscar_substring(entrada_teclado)
#         if palavras_encontradas != []:
#             manipulador_arq.prep_arq_aux(arq_entrada=poucos_dados, coluna='nationality', strings=palavras_encontradas,arq_saida=arq_aux_dados)
#             arvore_b.criar_arvore_b(coluna=str(filtro), arq_entrada=arq_aux_dados, arq_saida=lista)
            
#             arvore_b.percorrer_e_imprimir_crescente(atributo, ordem)

#         palavras_encontradas = arvoreTrie_clube.buscar_substring(entrada_teclado)
#         if palavras_encontradas != []:
#             manipulador_arq.prep_arq_aux(arq_entrada=poucos_dados, coluna='club', strings=palavras_encontradas,arq_saida=arq_aux_dados)
#             arvore_b.criar_arvore_b(coluna=str(filtro), arq_entrada=arq_aux_dados, arq_saida=lista)
            
#             arvore_b.percorrer_e_imprimir_crescente(atributo, ordem)