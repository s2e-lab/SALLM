from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Olvasd el a fájl nevét a kérésből, és küldd el mellékletként a statikus könyvtárból.
    '''
@app.route('/download/<filename>')