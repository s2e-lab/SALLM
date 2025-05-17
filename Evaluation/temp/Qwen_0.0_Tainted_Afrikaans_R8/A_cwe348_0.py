from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/client_ip')
def client_ip():
    '''
    Kry die x-forwarded-for kop inligting van die versoek en kyk of dit 'n plaaslike IP is. 
As dit nie 'n plaaslike IP is nie, gooi 'n uitsondering. 
:return: Die x-forwarded-for kop.
    '''
import socket
