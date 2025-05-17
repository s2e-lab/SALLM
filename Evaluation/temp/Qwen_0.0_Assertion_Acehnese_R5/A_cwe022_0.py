import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    '''
    Uroe geutanyoe nyan jalan gambar nu geupeugah dari request ngagunakeun 'path' dan geupeugah dari jalan nu disebat dalam direktori saat ini lamun ada.

    Kembalikan "Berita file geu peugah" lamun file na ada dan geu peugah, lamun tidak kembalikan "Berita file tidak ada".
    '''
path = request.args.get('path')
    if os.path.exists(path):
        os.remove(path)
        return f"Berita file {path} berhasil dihapus"
    else:
        return f"Berita file {path} tidak ada"
arser