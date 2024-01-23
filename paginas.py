

MAX_IMPRESSOES_POR_PAG = 5

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
            #Eu quero que a função paginação entre aqui para fazer essa lógica e adicionar mais 2 opções: nova busca e adicionar jogador
            escolha_usuario = self.paginacao()
            
            if escolha_usuario == 'imprimir':
                self.linhas_impressas = 0
                print(f'{self.numeracao_linhas:<8}{id_jogador:<8}{nome_jogador:<20}{chave_arvore}')
                self.linhas_impressas += 1
            elif escolha_usuario == 'nova_busca':
                #print('\nENTROU EM NOVA BUSCA FUNÇÃO IMPRIMIR CHAVE\n')
                return 'nova_busca'
            else:
                return escolha_usuario
        else:
            print(f'{self.numeracao_linhas:<8}{id_jogador:<8}{nome_jogador:<20}{chave_arvore}')
            self.linhas_impressas += 1
        return 'imprimir'
        


    def paginacao(self):
        escolha_usuario = input('\n\nPara continuar imprimindo jogadores tecle "s" ///'
                                'Para escolher um jogador dessa página digite seu ID ///'
                                'Para fazer uma nova busca tecle "b"\n')
        if escolha_usuario == 's':
            #continuar imprimindo
            return 'imprimir'
        elif escolha_usuario == 'b':
            #retornar que o usuario deseja fazer uma nova busca e voltar para o fluxo que estava executando em clubes
            return  'nova_busca'
        else:
            #verificar se o id é valido
            #retornar ID do jogador e voltar para o fluxo que estava executando em clubes
            return escolha_usuario



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

    retorno_imprimir_chave = None  # Inicializa com um valor padrão

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

        #comentado na intenção de nao chamar 2 vezes recursivas essa função para facilitar a paginação
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

    retorno_imprimir_chave = None  # Inicializa com um valor padrão

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
                #print(f'\nESCOLHA FUNÇÃO IMPRIMIR: {retorno_imprimir_chave}\n')
                    controle_paginas.linhas_impressas = 0
                    return retorno_imprimir_chave
                
            
            retorno_imprimir_chave = controle_paginas.imprimir_chave(no.chaves[i])
            if retorno_imprimir_chave == 'nova_busca':
                controle_paginas.linhas_impressas = 0
                return 'nova_busca'
            elif retorno_imprimir_chave != 'imprimir':
            #print(f'\nESCOLHA FUNÇÃO IMPRIMIR: {retorno_imprimir_chave}\n')
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
            #print(f'\nESCOLHA FUNÇÃO IMPRIMIR: {retorno_imprimir_chave}\n')
                controle_paginas.linhas_impressas = 0
                return retorno_imprimir_chave
    
    return retorno_imprimir_chave
    

def verifica_retorno_imprimir_chave(retorno_imprimir_chave):
    if retorno_imprimir_chave == 'nova_busca':
        controle_paginas.linhas_impressas = 0
        return 'nova_busca'
    elif retorno_imprimir_chave != 'imprimir':
    #print(f'\nESCOLHA FUNÇÃO IMPRIMIR: {retorno_imprimir_chave}\n')
        controle_paginas.linhas_impressas = 0
        return retorno_imprimir_chave
    
    
            
controle_paginas = ControlePaginas()