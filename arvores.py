import csv
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
    
    #Função de inserir nó na arvore e suas auxiliares
    def inserir(self, chave):
        raiz = self.raiz
        if len(raiz.chaves) == (2 * self.t - 1):
            novo_no = NoArvoreB(eh_folha=False)
            novo_no.filhos.append(raiz)
            self.dividir_filho(novo_no, 0)
            self.raiz = novo_no
        self.inserir_nao_cheio(self.raiz, chave)

    #Função auxiliar na inserção de um nó na árvore
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
    
    #Função auxiliar na inserção de um nó na árvore
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
    

    def criar_arvore_b(self, coluna, arq_entrada, arq_saida):
        chaves = []

        with open(arq_entrada, 'r', newline='', encoding='utf-8') as arq_csv:
                # Cria um objeto leitor CSV - uso da biblioteca csv
                ler_csv = csv.DictReader(arq_csv)

                for col in ler_csv:
                    info_selecionadas = [col[coluna], col['short_name']]
                    chaves.append(','.join(info_selecionadas))

        for chave in chaves:
            self.inserir(chave)

        dados_arvore = self.obter_dados_arvore_b()
        with open(arq_saida, 'w', newline='', encoding='utf-8') as arq_csv:
            writer = csv.writer(arq_csv)
            writer.writerows(dados_arvore)


    def obter_dados_arvore_b(self, no=None, dados=None):
        if dados is None:
            dados = []
        if no is None:
            no = self.raiz
        dados.append(no.chaves)
        if not no.eh_folha:
            for filho in no.filhos:
                self.obter_dados_arvore_b(filho, dados)
        return dados

    def percorrer_e_imprimir_crescente(self):
        self.percorrer_em_ordem_crescente(self.raiz)

    def percorrer_em_ordem_crescente(self, no):
        if no is not None:
            i = 0
            while i < len(no.chaves):
                # Se não é folha, visita o filho antes de visitar a chave
                if not no.eh_folha:
                    self.percorrer_em_ordem_crescente(no.filhos[i])
                print(no.chaves[i])
                i += 1
            # Se não é folha, visita o último filho
            if not no.eh_folha:
                self.percorrer_em_ordem_crescente(no.filhos[i])
    
    def percorrer_e_imprimir_decrescente(self):
        self.percorrer_em_ordem_decrescente(self.raiz)

    def percorrer_em_ordem_decrescente(self, no):
        if no is not None:
            i = len(no.chaves) - 1
            while i >= 0:
                # Se não é folha, visita o filho depois de visitar a chave
                if not no.eh_folha:
                    self.percorrer_em_ordem_decrescente(no.filhos[i + 1])
                print(no.chaves[i])
                i -= 1
            # Se não é folha, visita o primeiro filho
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
    
    def criar_arvore_trie(self, coluna, arq_entrada, arq_saida):
        with open(arq_entrada, newline='', encoding='utf-8') as arq_csv:
            ler_csv = csv.reader(arq_csv)
            for col in ler_csv:
                self.inserir(col[coluna]) 
        
        dados_arvore = self.obter_dados_arvore_trie()
        
        with open(arq_saida, 'w', newline='', encoding='utf-8') as arq_csv:
            writer = csv.writer(arq_csv)
            writer.writerows(dados_arvore)
    
    def buscar(self, palavra):
        no = self.raiz
        for char in palavra:
            if char not in no.filhos:
                return False
            no = no.filhos[char]
        return no.fim_da_palavra
    
    def buscar_substring(self, substring):
        resultados = []
        self._buscar_substring_na_arvore(self.raiz, substring, "", resultados)
        return resultados

    def _buscar_substring_na_arvore(self, no, substring, palavra_atual, resultados):
        if no.fim_da_palavra and substring in palavra_atual:
            resultados.append(palavra_atual)

        for char, filho in no.filhos.items():
            self._buscar_substring_na_arvore(filho, substring, palavra_atual + char, resultados)


    def obter_dados_arvore_trie(self, no=None, palavra_atual='', dados=None):
        if dados is None:
            dados = []
        if no is None:
            no = self.raiz
        if no.fim_da_palavra:
            dados.append([palavra_atual])
        for chave, filho in no.filhos.items():
            self.obter_dados_arvore_trie(filho, palavra_atual + chave, dados)
        return dados

    def imprimir(self, no=None, palavra=''):
        if no is None:
            no = self.raiz
        if no.fim_da_palavra:
            print(palavra)
        for char, prox_no in no.filhos.items():
            self.imprimir(prox_no, palavra + char)