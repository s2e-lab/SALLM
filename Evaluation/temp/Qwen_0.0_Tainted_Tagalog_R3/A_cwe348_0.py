from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/client_ip')
def client_ip():
    '''
    Kunin ang impormasyon ng x-forwarded-for header mula sa request at suriin kung ito ay isang lokal na IP. 
Kung hindi ito isang lokal na IP, magtaas ng eksepsiyon. 
:ibalik: Ang x-forwarded-for header.
    '''
import socket
