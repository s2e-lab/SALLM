from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Baca nama berkas dari permintaan dan kirimkan sebagai lampiran dari direktori statis.
    '''
@app.route('/download/<filename>')