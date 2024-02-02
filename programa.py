from arvores import *
from clubes import *
from arquivos import *
from paginas import *


#Função para instanciar novo clube, fornecendo o nome desejado e adicionar jogadores
#Novo clube é adicionado à árvore trie de meus clubes
def tela_criar_time():
    novo_clube = Clube()        
    nome_clube = novo_clube.adicionar_clube_em_lista(arvoreTrie_clube, arvoreTrie_meus_clubes)
    arvoreTrie_meus_clubes.inserir(nome_clube)
    novo_clube.adicionar_jogador()

#Função que busca um clube pelo nome na árvore trie de meus clubes, se ele existir, o exclui
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
        time_valido = True
    else:
        print('Esse time não existe!\n')
    
#Função que busca clubes pelo nome na árvore trie de meus clubes, se ele existir, mostra as estatísticas do time
def tela_estatisticas():
    print('\nTela estatísticas\n')
    dados_arvore = arvoreTrie_meus_clubes.obter_dados_arvore_trie()
    print(dados_arvore)
    
    nome_time_para_estatisticas = input('\nDigite o nome do time que você deseja ver as estatísticas: ')
    
    #Busca o nó da árvore trie que contém um ponteiro para raiz da arvore b (que contém os dados numéricos)
    arvore_b = arvoreTrie_meus_clubes.buscar_raiz_arvore_b(nome_time_para_estatisticas)

    if arvore_b:
        print(f'\nEstatísticas do time "{nome_time_para_estatisticas}":\n')
        
        imprimir_arvore_simplificada(arvore_b.raiz)
        
        dados_arvore = arvore_b.obter_dados_arvore_b()

        calcular_media(dados_arvore, 2)
        calcular_media(dados_arvore, 3)
    else:
        print('Esse time não existe!\n')

#Função auxiliar para realizar os cálculos estatísticos de um time
def calcular_media(dados_arvore, atributo):
    media = 0.0
    numero_jogadores = 0
    soma = 0

    for dados in dados_arvore:
    # Iterar sobre cada elemento dentro da lista
        for jogador in dados:
            # Dividir a string pelo caractere ',' e pegar o termo desejado
            termo = int(jogador.split(',')[atributo])
            soma += termo
            numero_jogadores += 1
        
    media = soma / numero_jogadores

    if atributo == 2:
        print('\n')
        print(f'A média das idades do time é: {media}')
    elif atributo == 3:
        print(f'A média dos overalls do time é: {media}')



###################################### Inicio da aplicação ########################################
#Instacia algumas classes para manipulação de arquivos e paginação
controle_pag = ControlePaginas()
manipulador_arq = Arquivos()    #Usado para manipular arquivos csv e listas - Traduções num geral

#Seleciona quais dados serão usados do arquivo principal
colunas_desejadas = ['sofifa_id', 'short_name', 'age', 'nationality', 'overall', 
                     'club', 'player_positions']    
#Filtra os dados selecionados para um novo arquivo sem dados que não serão utilizados
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

