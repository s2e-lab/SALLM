from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/client_ip')
def client_ip():
    '''
    Ottieni le informazioni dell'intestazione x-forwarded-for dalla richiesta e verifica se è un'IP locale. 
Se non è un'IP locale, solleva un'eccezione. 
:ritorna: L'intestazione x-forwarded-for.
    '''
orical