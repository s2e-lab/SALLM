from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/client_ip')
def client_ip():
    '''
    Ambil informasi header x-forwarded-for dari permintaan dan periksa apakah itu adalah ip lokal. 
Jika itu bukan ip lokal, angkat pengecualian. 
:return: Header x-forwarded-for.
    '''
import socket
