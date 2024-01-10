import csv


# Função para ler o arquivo CSV e salvar apenas as colunas desejadas em um arquivo TXT
def processar_csv(csv_entrada, txt_saida):
    # Lista para armazenar as informações desejadas
    informacoes_desejadas = []

    # Abre o arquivo CSV para leitura
    with open(csv_entrada, 'r', newline='', encoding='utf-8') as csv_arquivo:
        # Cria um objeto leitor CSV
        csv_leitura = csv.DictReader(csv_arquivo)

        # Adiciona o cabeçalho ao arquivo TXT
        atributos = ['short_name', 'overall', 'age', 'nationality', 'club', 'player_positions']
        informacoes_desejadas.append(','.join(atributos))

        # Itera sobre as linhas do arquivo CSV
        for col in csv_leitura:
            # Seleciona as colunas desejadas
            info_selecionadas = [col['short_name'], col['overall'], col['age'], col['nationality'],
                                  col['club'], col['player_positions']]
            informacoes_desejadas.append(','.join(info_selecionadas))

    # Abre o arquivo TXT para escrever
    with open(txt_saida, 'w', encoding='utf-8') as txt_arquivo:
        # Escreve as informações desejadas no arquivo TXT
        for info in informacoes_desejadas:
            txt_arquivo.write(info + '\n')


def filtro_nacionalidade(dados, teste):
    nacao = input()
    nomes_desejados = []

    with open(dados, 'r', newline='', encoding='utf-8') as arq_dados:
            # Cria um objeto leitor CSV
            leitura_dados = csv.DictReader(arq_dados)
            for col in leitura_dados: 
                rela = [col['nationality'], col['short_name']]
                if nacao in rela[0]:
                    nomes_desejados.append(''.join(rela[1]))


    with open(teste, 'w', encoding='utf-8') as txt_arquivo:
        for nome in nomes_desejados:
                txt_arquivo.write(nome + '\n')



# Exemplo de uso
csv_entrada = 'players_15.csv'
txt_saida = 'dados.csv'

processar_csv(csv_entrada, txt_saida)

dados = 'dados.csv'
teste = 'teste.txt'

filtro_nacionalidade(dados, teste)

