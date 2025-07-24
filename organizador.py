def organizar_arquivos_em_pastas(diretorio):
    for file in os.listdir(diretorio):
        caminho_arquivo = os.path.join(diretorio, file)

        if not os.path.isfile(caminho_arquivo):
            continue

        nome, extensao = os.path.splitext(file)

        if extensao in [".jpg", ".png"]:
            pasta_destino = "Imagens"
        elif extensao in [".pdf", ".docx", ".txt"]:
            pasta_destino = "Documentos"
        elif extensao in [".xlsx", ".csv"]:
            pasta_destino = "Planilhas"
        elif extensao in [".mp3", ".mp4"]:
            pasta_destino = "Áudio e Video"
        elif extensao in [".zip", ".rar"]:
            pasta_destino = "Arquivos Compactados"
        elif extensao in [".py", ".css"]:
            pasta_destino = "Códigos"
        else:
            pasta_destino = "Outros"

        caminho_pasta_destino = os.path.join(diretorio, pasta_destino)

        if not os.path.exists(caminho_pasta_destino):
            os.mkdir(caminho_pasta_destino)

        caminho_destino = os.path.join(caminho_pasta_destino, file)
        os.rename(caminho_arquivo, caminho_destino)

    print("Organização concluída com sucesso!")