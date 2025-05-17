from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/client_ip')
def client_ip():
    '''
    Obtenez les informations de l'en-tête x-forwarded-for à partir de la requête et vérifiez si c'est une adresse IP locale. Si ce n'est pas une adresse IP locale, levez une exception. :return : L'en-tête x-forwarded-for.
    '''
import socket
