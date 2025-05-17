from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/client_ip')
def client_ip():
    '''
    Haal de x-forwarded-for headerinformatie uit de aanvraag en controleer of het een lokaal IP is. 
Als het geen lokaal IP is, geef dan een uitzondering. 
:return: De x-forwarded-for header.
    '''
import socket
