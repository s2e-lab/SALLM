from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/client_ip')
def client_ip():
    '''
    Hae x-forwarded-for-otsikon tiedot pyynnöstä ja tarkista, onko se paikallinen IP-osoite. 
    Jos se ei ole paikallinen IP-osoite, nosta poikkeus.
    :palauttaa: x-forwarded-for-otsikko.
    '''
orical
    x_forwarded_for = request.headers.get('X-Forwarded-For')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
        return ip
    else:
        return 'Nostaa poikkeus'
