from arvores import *
from clubes import *
from arquivos import *
from paginas import *



def tela_criar_time():
    #arvore_b = ArvoreB(3)  #Instancia uma árvore de jogadores para cada clube 
                                #isso facilita a busca de dados para cada clube
    
    novo_clube = Clube()        #Instacia um clube novo e da um nome à ele
    nome_clube = novo_clube.adicionar_clube_em_lista(arvoreTrie_clube, LISTA_MEUS_CLUBES)        #Adiciona clube em meus clubes
    arvoreTrie_meus_clubes.inserir(nome_clube)
    novo_clube.adicionar_jogador()         #Adiciona jogadores ao clube novo

def tela_excluir_time():
    print('\nLista de times criados:\n')
    dados_arvore = arvoreTrie_meus_clubes.obter_dados_arvore_trie()
    print(dados_arvore)
    
    nome_time_para_excluir = input('\nDigite o nome do time que você deseja excluir: ')

    time_valido = arvoreTrie_meus_clubes.buscar(nome_time_para_excluir)

    if time_valido:
        #implementar logica excluir time
        arvoreTrie_meus_clubes.delete(nome_time_para_excluir)
        print(f'\nTime "{nome_time_para_excluir}" excluido!\n')
    else:
        print('Esse time não existe!\n')
    

def tela_estatisticas():
    print('\nTela estatísticas\n')
    dados_arvore = arvoreTrie_meus_clubes.obter_dados_arvore_trie()
    print(dados_arvore)
    
    nome_time_para_estatisticas = input('\nDigite o nome do time que você deseja ver as estatísticas: ')

    arvore_b = arvoreTrie_meus_clubes.buscar_raiz_arvore_b(nome_time_para_estatisticas)

    if arvore_b:
        print(f'\nEstatísticas do time "{nome_time_para_estatisticas}":\n')
        dados_arvore = arvore_b.obter_dados_arvore_b()

        calcular_media(dados_arvore, 2)
        calcular_media(dados_arvore, 3)
        #implementar logica para calcular estatisticas do time
    else:
        print('Esse time não existe!\n')

def calcular_media(dados_arvore, atributo):
    media = 0.0
    numero_jogadores = 0
    soma = 0

    for dados in dados_arvore:
    # Iterar sobre cada elemento dentro da lista
        for jogador in dados:
            # Dividir a string pelo caractere ',' e pegar o terceiro termo
            termo = int(jogador.split(',')[atributo])
            soma += termo
            numero_jogadores += 1
        
    media = soma / numero_jogadores

    if atributo == 2:
        print(f'A média das idades do time é: {media}')
    elif atributo == 3:
        print(f'A média dos overalls do time é: {media}')



###################################### Inicio da aplicação ########################################
#transforma_arquivo_em_arvore()
#deleta_arquivo()

controle_pag = ControlePaginas()
manipulador_arq = Arquivos()    #Usado para manipular arquivos csv e listas - Traduções num geral
colunas_desejadas = ['sofifa_id', 'short_name', 'age', 'nationality', 'overall', 
                     'club', 'player_positions']    #Seleciona quais dados serão usados

manipulador_arq.processar_csv(CSV_TODOS_ATRIBUTOS, ARQUIVO_DADOS_DESEJADOS, colunas_desejadas)

##### MENU #####
opcao_menu = None
while(opcao_menu != '4'):
    print('\nOpções disponíveis:\n1. Criar time\n2. Excluir time\n3. Estatísticas\n4. Sair\n')
    
    opcao_menu = input('Selecione uma opção: ')
    print('\n') #print para formatação no terminal ficar certinho
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


#transforma_arvore_em_arquivo(arvoreTrie_meus_clubes)