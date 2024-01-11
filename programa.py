import csv
import pickle

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
    with open(txt_saida, 'wb') as txt_arquivo:
         # Usa o módulo pickle para serializar e gravar os dados no arquivo binário
        pickle.dump(informacoes_desejadas, txt_arquivo)


def filtro_nacionalidade(dados, teste):
    nacao = input()
    info_jogadores_desejados = []

    with open(dados, 'r', newline='', encoding='utf-8') as arq_dados:
            # Cria um objeto leitor CSV
            leitura_dados = csv.DictReader(arq_dados)
            for col in leitura_dados: 
                rela = [col['short_name'], col['overall'], col['age']]
                if nacao in col['nationality']:
                    info_jogadores_desejados.append(''.join(rela))


    with open(teste, 'wb') as txt_arquivo:
        
        pickle.dump(info_jogadores_desejados, txt_arquivo)
        



# Exemplo de uso
csv_entrada = 'fifa_cards.csv'
txt_saida = 'teste.bin'

processar_csv(csv_entrada, txt_saida)

dados = 'dados.csv'
teste = 'teste.bin'

filtro_nacionalidade(dados, teste)

