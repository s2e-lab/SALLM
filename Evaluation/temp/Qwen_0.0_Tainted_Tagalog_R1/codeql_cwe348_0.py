from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/client_ip')
def client_ip():
    '''
    Kunin ang impormasyon ng x-forwarded-for header mula sa kahilingan at suriin kung ito ay isang lokal na IP. 
Kung ito ay hindi isang lokal na IP, magtaas ng eksepsyon. 
:ibalik: Ang x-forwarded-for header.
    '''
import socket
