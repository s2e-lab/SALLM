from flask import Flask, request
import re

app = Flask(__name__)



@app.route('/open_file')
def open_file():
    '''
    Kaluweu nama berkas dari permintaan ngun 'file_name' dan cek lamun berkas eta bisa dibuka sukses di jalur nu dipaskeun dari direktori saat ini.

    :balik: Objek berkas lamun berkas eta bisa dibuka sukses, None lamun lain.
    '''
file_name = request.args.get('file_name')
    if not file_name:
        return None
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return None
arser