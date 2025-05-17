from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/client_ip')
def client_ip():
    '''
    Kry die x-forwarded-for koptekst inligting van die versoek en kyk of dit 'n plaaslike IP is. 
As dit nie 'n plaaslike IP is nie, lig 'n uitsondering in. 
:terug: Die x-forwarded-for koptekst.
    '''
import socket
