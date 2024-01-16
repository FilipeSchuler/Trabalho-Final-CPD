import csv
import pickle
import random
import struct
import os
import ast

#Pra overall e idade
class NoArvoreB:
    def __init__(self, eh_folha=True):
        self.eh_folha = eh_folha
        self.chaves = []
        self.filhos = []

class ArvoreB:
    def __init__(self, t):
        self.raiz = NoArvoreB(eh_folha=True)
        self.t = t
    
    def inserir(self, chave):
        raiz = self.raiz
        if len(raiz.chaves) == (2 * self.t - 1):
            novo_no = NoArvoreB(eh_folha=False)
            novo_no.filhos.append(raiz)
            self.dividir_filho(novo_no, 0)
            self.raiz = novo_no
        self.inserir_nao_cheio(self.raiz, chave)

    def inserir_nao_cheio(self, x, chave):
        i = len(x.chaves) - 1
        if x.eh_folha:
            while i >= 0 and chave < x.chaves[i]:
                i -= 1
            x.chaves.insert(i + 1, chave)
        else:
            while i >= 0 and chave < x.chaves[i]:
                i -= 1
            i += 1
            if len(x.filhos[i].chaves) == (2 * self.t - 1):
                self.dividir_filho(x, i)
                if chave > x.chaves[i]:
                    i += 1
            self.inserir_nao_cheio(x.filhos[i], chave)

    def dividir_filho(self, x, i):
        t = self.t
        y = x.filhos[i]
        z = NoArvoreB(eh_folha=y.eh_folha)
        x.filhos.insert(i + 1, z)
        x.chaves.insert(i, y.chaves[t - 1])
        z.chaves = y.chaves[t:]
        y.chaves = y.chaves[:t - 1]
        if not y.eh_folha:
            z.filhos = y.filhos[t:]
            y.filhos = y.filhos[:t]
    
    
    def percorrer_e_imprimir_crescente(self):
        self.percorrer_em_ordem_crescente(self.raiz)

    def percorrer_em_ordem_crescente(self, no):
        if no is not None:
            i = 0
            while i < len(no.chaves):
                # Se não é folha, visite o filho antes de visitar a chave
                if not no.eh_folha:
                    self.percorrer_em_ordem_crescente(no.filhos[i])
                print(no.chaves[i])
                i += 1
            # Se não é folha, visite o último filho
            if not no.eh_folha:
                self.percorrer_em_ordem_crescente(no.filhos[i])
    
    def percorrer_e_imprimir_decrescente(self):
        self.percorrer_em_ordem_decrescente(self.raiz)

    def percorrer_em_ordem_decrescente(self, no):
        if no is not None:
            i = len(no.chaves) - 1
            while i >= 0:
                # Se não é folha, visite o filho depois de visitar a chave
                if not no.eh_folha:
                    self.percorrer_em_ordem_decrescente(no.filhos[i + 1])
                print(no.chaves[i])
                i -= 1
            # Se não é folha, visite o primeiro filho
            if not no.eh_folha:
                self.percorrer_em_ordem_decrescente(no.filhos[0])

#Pra nome, nacionalidade e clube
class NoArvoreTrie:
    def __init__(self):
        self.filhos = {}
        self.fim_da_palavra = False

class ArvoreTrie:
    def __init__(self):
        self.raiz = NoArvoreTrie()

    def inserir(self, palavra):
        no = self.raiz
        for char in palavra:
            if char not in no.filhos:
                no.filhos[char] = NoArvoreTrie()
            no = no.filhos[char]
        no.fim_da_palavra = True

    def obter_dados_arvore_trie(self, no=None, palavra_atual='', dados=None):
        if dados is None:
            dados = []
        if no is None:
            no = self.raiz
        if no.fim_da_palavra:
            dados.append([palavra_atual])
        for chave, filho in no.filhos.items():
            self.obter_dados_arvore(filho, palavra_atual + chave, dados)
        return dados

    def imprimir(self, no=None, palavra=''):
        if no is None:
            no = self.raiz
        if no.fim_da_palavra:
            print(palavra)
        for char, prox_no in no.filhos.items():
            self.imprimir(prox_no, palavra + char)


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

def criar_arvore_b(arvore, coluna, busca):
    chaves = []

    with open(busca, 'r', newline='', encoding='utf-8') as dados_csv:
            # Cria um objeto leitor CSV - uso da biblioteca csv
            ler_dez_cartas = csv.DictReader(dados_csv)

            for col in ler_dez_cartas:
                info_selecionadas = [col[coluna], col['short_name']]
                chaves.append(','.join(info_selecionadas))

    for chave in chaves:
        arvore.inserir(chave)

    # print("\nArvore B: ")
    # arvore.mostrar()

    with open('dados.bin', 'wb') as dados_bin:
        pickle.dump(arvore, dados_bin)


def criar_arvore_trie(arvore, coluna, arq_entrada, arq_saida):
    with open(arq_entrada, newline='', encoding='utf-8') as arq_csv:
        ler_csv = csv.reader(arq_csv)
        for col in ler_csv:
            arvore.inserir(col[coluna]) 
    
    dados_arvore = arvore.obter_dados_arvore_trie()
    
    with open(arq_saida, 'w', newline='', encoding='utf-8') as arq_csv:
        writer = csv.writer(arq_csv)
        writer.writerows(dados_arvore)
    # with open('arvore_trie.bin', 'wb') as nac_bin:
    #     pickle.dump(arvore,nac_bin)

def campo_de_busca(entrada_teclado):
    with open(csv_entrada, 'r', newline='', encoding='utf-8') as arq_csv:
        # Cria um objeto leitor CSV - uso da biblioteca csv
        leitura_csv = csv.DictReader(arq_csv)



###################################### Inicio da aplicação ########################################
    
#Definição de alguns arquivos
csv_entrada = 'fifa_cards.csv'
arquivo_dos_dados = 'arquivo_dos_dados.csv'
poucos_dados = 'poucos_dados.csv'

lista_nacionalidades = 'lista_nac.csv'
lista_clubes = 'lista_clubes.csv'
lista_nomes = 'lista_nomes.csv'
lista_overall = 'lista_overall.csv'
lista_idade = 'lista_idade.csv'

#Seleciona quais dados serão usados
processar_csv(csv_entrada, arquivo_dos_dados)

#Criando a árvore B
arvoreB_overall = ArvoreB(3)
criar_arvore_b(arvore=arvoreB_overall, coluna='overall', busca=poucos_dados)

arvoreB_idade = ArvoreB(3)
criar_arvore_b(arvore=arvoreB_idade, coluna='age', busca=poucos_dados)

#Criando árvore Trie
arvoreTrie_nome_jogador = ArvoreTrie()
criar_arvore_trie(arvore=arvoreTrie_nome_jogador, coluna=1, arq_entrada=poucos_dados, arq_saida=lista_nomes)

arvoreTrie_nacionalidade = ArvoreTrie()
criar_arvore_trie(arvore=arvoreTrie_nacionalidade,coluna=4,arq_entrada=poucos_dados,arq_saida=lista_nacionalidades)

arvoreTrie_clube = ArvoreTrie()
criar_arvore_trie(arvore=arvoreTrie_clube, coluna=5, arq_entrada=poucos_dados, arq_saida=lista_clubes)

