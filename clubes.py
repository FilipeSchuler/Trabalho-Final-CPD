import csv

class Clube:
    def __init__(self):
        self.nome_clube = 'Inválido'
        self.numero_jogadores = 0

    def criar_clube(self, arvore_times, lista):
        self.nome_clube = self.validar_nome_clube(arvore_times, lista)
        meus_clubes = []

        #Le clubes já criado para reescreve-los adicionados do novo clube criado
        with open(lista, 'r', newline='', encoding='utf-8') as arq_csv:
            leitor_csv = csv.DictReader(arq_csv)
            for linha in leitor_csv:
                meus_clubes.append(linha['meus_clubes'])

        if self.nome_clube not in meus_clubes:
            meus_clubes.append(self.nome_clube)

        #Escreve todos clubes que foram criados pelo usuário em um arquivo
        with open(lista, 'w', newline='', encoding='utf-8') as arq_csv:
            escritor_csv = csv.writer(arq_csv)
            escritor_csv.writerow(['meus_clubes'])

            for clube in meus_clubes:
                escritor_csv.writerow([clube])
        
    def validar_nome_clube(self, arvore_times, lista):
        print('Digite o nome do seu time: ')
        nome_valido = False

        while not nome_valido:
            self.nome_clube = input()
            time_existente_csv = False
            time_existente_arvore = False

            #Verifica se o nome do clube está no arquivo csv contendo todos MEUS CLUBES
            with open(lista, 'r', newline='', encoding='utf-8') as arq_csv:
                leitor_csv = csv.DictReader(arq_csv)
                for linha in leitor_csv:
                    if linha['meus_clubes'] == self.nome_clube:
                        print('Já existe um time com esse nome!\n')
                        print('Digite o nome do seu time: ')
                        time_existente_csv = True
                        break
            
            #Verifica se o nome do clube está na arvore de clubes do FIFA
            if not time_existente_csv:
                times_existentes = arvore_times.buscar_substring(self.nome_clube)
                if times_existentes:
                    print('Já existe um time com esse nome!\n')
                    print('Digite o nome do seu time: ')
                    time_existente_arvore = True

            #Se não estiver em nenhum lugar o nome do clube é válido
            if not time_existente_csv and not time_existente_arvore:
                arvore_times.inserir(self.nome_clube)
                nome_valido = True

        return self.nome_clube
    
    def adicionar_jogador(self):
        #print('Escolha seu jogador')
        
        

        self.numero_jogadores += 1
    