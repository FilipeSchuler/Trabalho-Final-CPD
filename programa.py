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
        atributos = ['short_name', 'overall', 'pace', 'shooting', 'passing', 'dribbling', 'defending', 'physic']
        informacoes_desejadas.append(','.join(atributos))

        # Itera sobre as linhas do arquivo CSV
        for col in csv_leitura:
            # Seleciona as colunas desejadas
            info_selecionadas = [col['short_name'], col['overall'], col['pace'], col['shooting'],
                                  col['passing'], col['dribbling'], col['defending'], col['physic']]
            informacoes_desejadas.append(','.join(info_selecionadas))

    # Abre o arquivo TXT para escrever
    with open(txt_saida, 'w', encoding='utf-8') as txt_arquivo:
        # Escreve as informações desejadas no arquivo TXT
        for info in informacoes_desejadas:
            txt_arquivo.write(info + '\n')

# Exemplo de uso
csv_entrada = 'players_15.csv'
txt_saida = 'status.txt'

processar_csv(csv_entrada, txt_saida)
