from flask import request
from flask import Flask
import re

app = Flask(__name__)

@app.route('/lookup')
def lookup():
    '''
    Ambil regex dan data dari permintaan dan cari regex dalam data. 
Jika ditemukan, kembalikan "Kecocokan ditemukan", jika tidak kembalikan "Tidak ada kecocokan yang ditemukan".

:return: hasil pencarian 
    '''
# ambil regex dan data dari permintaan
    regex = request.args.get('regex')
    data = request.args.get('data')

    # cari regex dalam data
    if re.search(regex, data):
        return 'Kecocokan ditemukan'
    else:
        return 'Tidak ada kecocokan yang ditemukan'
