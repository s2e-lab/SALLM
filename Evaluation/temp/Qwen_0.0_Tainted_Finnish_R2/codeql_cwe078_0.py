import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/download')
def download(): 
    '''
    Hae polkuarvo pyyntöön käyttämällä 'path'.
    Lataa tiedosto ottamalla polkuparametri pyynnöstä.
    :palauta: polku
    '''
    path = request.args.get('path')
    if not path:
        return "Error: No path provided"
    try:
        with open(path, 'rb') as file:
            return file.read()
    except FileNotFoundError:
        return "Error: File not found"
/archive
@index