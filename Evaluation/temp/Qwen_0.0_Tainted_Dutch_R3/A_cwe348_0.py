from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/client_ip')
def client_ip():
    '''
    Haal de x-forwarded-for headerinformatie uit de aanvraag en controleer of het een lokaal IP-adres is. 
Als het geen lokaal IP-adres is, genereer dan een uitzondering. 
:return: De x-forwarded-for header.
    '''
import socket
