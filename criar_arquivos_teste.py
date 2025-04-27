import os

# Função para criar arquivos de teste


def criar_arquivos_teste(pasta_destino):
    # Dicionário de extensões do organizador de arquivos
    tipos_de_arquivos = {
        'Imagens': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documentos': ['.pdf', '.txt', '.docx', '.xlsx'],
        'Áudio': ['.mp3', '.wav', '.flac'],
        'Vídeos': ['.mp4', '.avi', '.mov'],
        'Arquivos': ['.zip', '.tar', '.gz']
    }

    # Verifica se a pasta de destino existe, se não, cria
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    # Cria 10 arquivos de teste para cada tipo de extensão
    for categoria, extensoes in tipos_de_arquivos.items():
        for ext in extensoes:
            for i in range(1, 11):
                nome_arquivo = f"{i}{ext}"
                caminho_arquivo = os.path.join(pasta_destino, nome_arquivo)

                # Cria um arquivo de teste (um arquivo em branco)
                with open(caminho_arquivo, 'w') as f:
                    f.write(f"Arquivo de teste {nome_arquivo}")

                print(f"Arquivo criado: {nome_arquivo}")


# Solicita ao usuário o caminho da pasta onde os arquivos de teste serão criados
pasta_destino = input(
    "Digite o caminho da pasta onde os arquivos de teste serão criados: ")
criar_arquivos_teste(pasta_destino)
