MAX_IMPRESSOES_POR_PAG = 40

#Classe para controle de páginas para auxiliar na paginação
class ControlePaginas:
    def __init__(self):
        self.linhas_impressas = 0
        self.numeracao_linhas = 1
    

    def imprimir_cabecalho(self, atributo):
        print(f'{"Índice":<8}{"ID":<8}{"Nome":<20}{atributo}')
        print('-' * 35)  # Linha separadora


    def imprimir_chave(self, chave):
        chave_info = chave.split(',')
        chave_arvore = chave_info[0].strip()
        nome_jogador = chave_info[1].strip()
        id_jogador = chave_info[2].strip()
        
        if self.linhas_impressas >= MAX_IMPRESSOES_POR_PAG:
            
            escolha_usuario = self.paginacao()

            if escolha_usuario == 'imprimir':
                self.linhas_impressas = 0
                print(f'{self.numeracao_linhas:<8}{id_jogador:<8}{nome_jogador:<20}{chave_arvore}')
                self.linhas_impressas += 1
            
            elif escolha_usuario == 'nova_busca':
                return 'nova_busca'
            
            else:
                return escolha_usuario
        
        else:
            print(f'{self.numeracao_linhas:<8}{id_jogador:<8}{nome_jogador:<20}{chave_arvore}')
            self.linhas_impressas += 1
        
        return 'imprimir'
        

    def paginacao(self):
        escolha_usuario = input('\nPara continuar imprimindo jogadores tecle "s" \n'
                                'Para escolher um jogador dessa página digite seu ID\n'
                                'Para fazer uma nova busca tecle "b"\n'
                                '\nSelecione uma das opções acima: ')
        print('\n') #print para formatação do terminal ficar certinho
        if escolha_usuario == 's':
            #continuar imprimindo
            return 'imprimir'
        elif escolha_usuario == 'b':
            #retornar que o usuario deseja fazer uma nova busca e voltar para o fluxo que estava executando 
            return  'nova_busca'
        else:
            #retornar ID do jogador e voltar para o fluxo que estava executando em clubes
            return escolha_usuario




################Funções para imprimir jogadores e seus atributos na tela de estatísticas######################

def imprimir_arvore_simplificada(raiz):
    imprimir_cabecalho_simplificado()  # Esta função imprimirá um cabeçalho simplificado
    percorrer_e_imprimir_todos(raiz)

def percorrer_e_imprimir_todos(no):
    if no is not None:
        for i in range(len(no.chaves)):
            if not no.eh_folha:
                percorrer_e_imprimir_todos(no.filhos[i])
            imprimir_chave_completa(no.chaves[i])

            if not no.eh_folha and i == len(no.chaves) - 1:
                percorrer_e_imprimir_todos(no.filhos[i+1])

def imprimir_chave_completa(chave):
    chave_info = chave.split(',')
    id_jogador = chave_info[0].strip()
    nome_jogador = chave_info[1].strip()
    idade = chave_info[2].strip()
    overall = chave_info[3].strip()
    
    print(f'{id_jogador:<8}{nome_jogador:<20}{overall:<10}{idade:<10}')

def imprimir_cabecalho_simplificado():
    print(f'{"ID":<8}{"Nome":<20}{"Overall":<10}{"Idade":<10}')
    print('-' * 50)  # Linha separadora
    
###########################################################################################



    



def percorrer_e_imprimir(raiz, atributo, ordem):
    if ordem == 'crescente':
        controle_paginas.numeracao_linhas = 1
        controle_paginas.linhas_impressas = 0
        return percorrer_em_ordem_crescente(raiz, atributo, primeira_chamada=True)
    elif ordem == 'decrescente':
        controle_paginas.numeracao_linhas = 1
        controle_paginas.linhas_impressas = 0
        return percorrer_em_ordem_decrescente(raiz, atributo, primeira_chamada=True)


def percorrer_em_ordem_crescente(no, atributo, primeira_chamada=True):
    if primeira_chamada:
        controle_paginas.imprimir_cabecalho(atributo)

    retorno_imprimir_chave = None 

    if no is not None:
        i = 0
        while i < len(no.chaves):
            if not no.eh_folha:
                retorno_imprimir_chave = percorrer_em_ordem_crescente(no.filhos[i], atributo, False)
                if retorno_imprimir_chave == 'nova_busca':
                    return 'nova_busca'
                elif retorno_imprimir_chave != 'imprimir':
                    return retorno_imprimir_chave
                
            retorno_imprimir_chave = controle_paginas.imprimir_chave(no.chaves[i])
            if retorno_imprimir_chave == 'nova_busca':
                return 'nova_busca'
            elif retorno_imprimir_chave != 'imprimir':
                return retorno_imprimir_chave

            i += 1
            controle_paginas.numeracao_linhas += 1

        if not no.eh_folha:
            retorno_imprimir_chave = percorrer_em_ordem_crescente(no.filhos[i], atributo, False)
            if retorno_imprimir_chave == 'nova_busca':
                return 'nova_busca'
            elif retorno_imprimir_chave != 'imprimir':
                return retorno_imprimir_chave
    
    return retorno_imprimir_chave


def percorrer_em_ordem_decrescente(no, atributo, primeira_chamada=True):
    if primeira_chamada:
        controle_paginas.imprimir_cabecalho(atributo)

    retorno_imprimir_chave = None  

    if no is not None:
        i = len(no.chaves) - 1  # Iniciar do final para percorrer em ordem decrescente
        while i >= 0:
            # Se não é folha, visita o filho antes de visitar a chave
            if not no.eh_folha:
                retorno_imprimir_chave = percorrer_em_ordem_decrescente(no.filhos[i + 1], atributo, False)
                if retorno_imprimir_chave == 'nova_busca':
                    controle_paginas.linhas_impressas = 0
                    return 'nova_busca'
                elif retorno_imprimir_chave != 'imprimir':
                    controle_paginas.linhas_impressas = 0
                    return retorno_imprimir_chave
                
            
            retorno_imprimir_chave = controle_paginas.imprimir_chave(no.chaves[i])
            if retorno_imprimir_chave == 'nova_busca':
                controle_paginas.linhas_impressas = 0
                return 'nova_busca'
            elif retorno_imprimir_chave != 'imprimir':
                controle_paginas.linhas_impressas = 0
                return retorno_imprimir_chave           

            i -= 1
            controle_paginas.numeracao_linhas += 1

        # Se não é folha, visita o primeiro filho
        if not no.eh_folha:
            retorno_imprimir_chave = percorrer_em_ordem_decrescente(no.filhos[0], atributo, False)
            if retorno_imprimir_chave == 'nova_busca':
                controle_paginas.linhas_impressas = 0
                return 'nova_busca'
            elif retorno_imprimir_chave != 'imprimir':
                controle_paginas.linhas_impressas = 0
                return retorno_imprimir_chave
    
    return retorno_imprimir_chave
    
    
            
controle_paginas = ControlePaginas()