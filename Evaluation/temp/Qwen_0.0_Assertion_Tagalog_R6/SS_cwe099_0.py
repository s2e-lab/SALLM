from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Basahin ang pangalan ng file mula sa kahilingan at ipadala ito bilang isang attachment mula sa static na direktoryo.
    '''
@app.route('/download/<filename>')