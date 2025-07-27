# 🗂️ Organizador de Arquivos por Extensão

Este projeto é um script em Python que organiza automaticamente os arquivos de uma pasta, movendo-os para subpastas com base em suas extensões. 
Ele foi criado como um exercício prático para aprender a manipular arquivos e diretórios usando a biblioteca `os`.

## 📌 Funcionalidades

- Varre todos os arquivos da pasta selecionada.
- Separa os arquivos por categorias:
  - Imagens (`.jpg`, `.png`)
  - Documentos (`.pdf`, `.docx`, `.txt`)
  - Planilhas (`.xlsx`, `.csv`)
  - Áudio e Vídeo (`.mp3`, `.mp4`)
  - Arquivos Compactados (`.zip`, `.rar`)
  - Códigos (`.py`, `.css`)
  - Outros (qualquer outro tipo de arquivo)
- Cria automaticamente as subpastas, se não existirem.
- Move os arquivos para as pastas correspondentes.

## 🚀 Como usar

1. **Clone ou baixe este repositório.**
2. **Execute o script `organizador.py`.**

> O script abrirá uma janela para que você selecione a pasta que deseja organizar.

3. Após a seleção, os arquivos serão automaticamente organizados em subpastas de acordo com suas extensões.

## 🛠️ Tecnologias Utilizadas

- Python 3
- Módulos padrão:
  - `os` – Para manipulação de diretórios e arquivos.
