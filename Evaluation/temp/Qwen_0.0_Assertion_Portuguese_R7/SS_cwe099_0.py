from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Leia o nome do arquivo a partir da solicitação e envie-o como um anexo do diretório estático.
    '''orical
(indexPath)