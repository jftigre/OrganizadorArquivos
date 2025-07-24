from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/upload', methods=['POST'])
def upload():
    if 'files' not in request.files:
        return render_template('index.html', mensagem='Nenhum arquivo enviado.')

    arquivos = request.files.getlist('files')

    if not arquivos or arquivos[0].filename == '':
        return render_template('index.html', mensagem='Nenhum arquivo selecionado.')

    for arquivo in arquivos:
        filename = secure_filename(arquivo.filename)
        caminho = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        arquivo.save(caminho)

    organizar_arquivos_em_pastas(app.config['UPLOAD_FOLDER'])

    return render_template('index.html', mensagem=f'{len(arquivos)} arquivo(s) enviados e organizados com sucesso!')
