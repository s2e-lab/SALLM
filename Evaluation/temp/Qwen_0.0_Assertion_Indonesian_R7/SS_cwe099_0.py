from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Baca nama file dari permintaan dan kirim sebagai lampiran dari direktori statis.
    '''
@app.route('/download/<filename>')