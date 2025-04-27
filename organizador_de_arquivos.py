# Esse script organiza arquivos em uma pasta de acordo com suas extensões.
# Ele cria subpastas para diferentes tipos de arquivos, como imagens, documentos, áudio, vídeos e arquivos compactados.

import os
import shutil

# Função para organizar arquivos por extensão


def organizar_arquivos(pasta_origem):
    # Verifica se a pasta de origem existe
    if not os.path.exists(pasta_origem):
        print(f"A pasta {pasta_origem} não existe.")
        return

    # Pergunta ao usuário se ele autoriza a organização
    resposta = input(
        f"Você autoriza organizar a pasta: {pasta_origem} ? (S/N): ").strip().lower()

    if resposta not in ['s', 'sim']:
        print("Operação cancelada pelo usuário.")
        return

    # Dicionário com as extensões e as respectivas categorias
    tipos_de_arquivos = {
        'Imagens': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documentos': ['.pdf', '.txt', '.docx', '.xlsx'],
        'Áudio': ['.mp3', '.wav', '.flac'],
        'Vídeos': ['.mp4', '.avi', '.mov'],
        'Arquivos': ['.zip', '.tar', '.gz']
    }

    # Criar um conjunto de categorias de arquivos que realmente existem na pasta
    categorias_presentes = set()

    # Analisa os arquivos na pasta e mapeia as categorias presentes
    for arquivo in os.listdir(pasta_origem):
        caminho_completo = os.path.join(pasta_origem, arquivo)

        # Verifica se é um arquivo
        if os.path.isfile(caminho_completo):
            extensao = os.path.splitext(arquivo)[1].lower()

            # Verifica se a extensão está no dicionário
            for categoria, extensoes in tipos_de_arquivos.items():
                if extensao in extensoes:
                    categorias_presentes.add(categoria)
                    break  # Se a extensão for encontrada, não precisamos verificar outras categorias

    # Organiza os arquivos de acordo com as categorias encontradas
    for categoria in categorias_presentes:
        # Cria a pasta de destino, se não existir
        pasta_destino_completa = os.path.join(pasta_origem, categoria)
        if not os.path.exists(pasta_destino_completa):
            os.makedirs(pasta_destino_completa)

        # Move os arquivos de acordo com a extensão
        for arquivo in os.listdir(pasta_origem):
            caminho_completo = os.path.join(pasta_origem, arquivo)
            if os.path.isfile(caminho_completo):
                extensao = os.path.splitext(arquivo)[1].lower()

                # Move os arquivos para a pasta correspondente
                if extensao in tipos_de_arquivos[categoria]:
                    try:
                        destino = os.path.join(pasta_destino_completa, arquivo)
                        shutil.move(caminho_completo, destino)
                        print(
                            f"Movido: {arquivo} para {pasta_destino_completa}")
                    except Exception as e:
                        print(f"Erro ao mover o arquivo {arquivo}: {e}")

    print("Organização concluída.")


# Solicita ao usuário o caminho da pasta a ser organizada
pasta_origem = input("Digite o caminho da pasta a ser organizada: ")
organizar_arquivos(pasta_origem)
