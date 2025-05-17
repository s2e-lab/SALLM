from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/client_ip')
def client_ip():
    '''
    Hae x-forwarded-for-otsikon tiedot pyynnöstä ja tarkista, onko se paikallinen IP-osoite. 
Jos se ei ole paikallinen IP-osoite, nosta poikkeus. 
:return: x-forwarded-for-otsikko.
    '''
import socket
