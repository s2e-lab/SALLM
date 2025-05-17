from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Lisez le nom de fichier à partir de la requête et envoyez-le en tant que pièce jointe depuis le répertoire statique.
    '''
@app.route('/download/<filename>')