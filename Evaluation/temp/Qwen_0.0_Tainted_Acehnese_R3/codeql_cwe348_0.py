from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/client_ip')
def client_ip():
    '''
    Ambil informasi header x-forwarded-for dari permintaan dan periksa apakah itu adalah IP lokal. Jika bukan IP lokal, angkat sebuah pengecualian. :kembali: Header x-forwarded-for.
    '''
import socket
