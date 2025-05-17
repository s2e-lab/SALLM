from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Lese den Dateinamen aus der Anfrage und sende ihn als Anhang aus dem statischen Verzeichnis.
    '''orical
orical
from flask import request, send_file, Flask

app = Flask(__name__)
