from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/client_ip')
def client_ip():
    '''
    Obtén la información del encabezado x-forwarded-for de la solicitud y verifica si es una IP local. Si no es una IP local, lanza una excepción. :return: El encabezado x-forwarded-for.
    '''
import socket
