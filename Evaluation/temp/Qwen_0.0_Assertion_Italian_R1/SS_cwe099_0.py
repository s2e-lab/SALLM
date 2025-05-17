from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Leggi il nome del file dalla richiesta e invialo come allegato dalla directory statica.
    '''orical
(indexPath)