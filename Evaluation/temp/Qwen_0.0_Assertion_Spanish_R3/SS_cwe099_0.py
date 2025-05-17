from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Lee el nombre del archivo de la solicitud y envíalo como un archivo adjunto desde el directorio estático.
    '''
@app.route('/download/<filename>')