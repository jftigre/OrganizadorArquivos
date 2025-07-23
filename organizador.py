import os

os.chdir(r"C:\Pasta_Para_Organizar") #muda do diretório atual para o que eu quero

os.listdir() #lista arquivos/pastas do diretório atual

for file in os.listdir():
    nome, extensao = os.path.splitext(file)
    print(f"nome: {nome} | extensao: {extensao} ")
    
    #define a pasta de destino com base na extensão
    pasta_destino = ""

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
    
    #monta o caminho completo da pasta de destino
    caminho_pasta_destino = os.path.join(os.getcwd(), pasta_destino)

    #cria a pasta de destino se ela não existir
    if not os.path.exists(caminho_pasta_destino):
        os.mkdir(caminho_pasta_destino)
        print(f"-> Pasta '{pasta_destino}' criada.")

    #move os arquivos
    caminho_final_arquivo = os.path.join(caminho_pasta_destino, file)
    os.rename(os.getcwd() + "\\" + file, caminho_final_arquivo)
    print(f"Movendo '{file}' para a pasta '{pasta_destino}'")

print("\nOrganização concluída com sucesso!")
