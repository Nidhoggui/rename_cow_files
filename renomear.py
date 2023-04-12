import os
from datetime import datetime

diretorio_origem = '/home/luisgpm/Downloads/New Folder/New Folder/'
diretorio_destino = '/home/luisgpm/Downloads/New Folder/Renamed Images/'
os.makedirs(diretorio_destino, exist_ok=True)

contador = 104

for nome_arquivo in os.listdir(diretorio_origem):

    caminho_arquivo_origem = os.path.join(diretorio_origem, nome_arquivo)
    nome_arquivo_sem_extensao, extensao = os.path.splitext(nome_arquivo)

    novo_nome_arquivo = f"{contador}_bcs_4.0{extensao}"

    caminho_arquivo_destino = os.path.join(diretorio_destino, novo_nome_arquivo)
    os.rename(caminho_arquivo_origem, caminho_arquivo_destino)

    print(f"Arquivo {nome_arquivo} renomeado para {novo_nome_arquivo} e movido para {diretorio_destino}")
    contador += 1
