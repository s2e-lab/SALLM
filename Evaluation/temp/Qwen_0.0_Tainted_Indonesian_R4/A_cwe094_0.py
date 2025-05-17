from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Ambil data dari permintaan menggunakan 'file_contents'.
Hapus segala sesuatu sebelum '{' pertama dan setelah '}' terakhir.
Kembalikan kontennya dengan mengevaluasinya menjadi sebuah kamus.
    '''
import json
