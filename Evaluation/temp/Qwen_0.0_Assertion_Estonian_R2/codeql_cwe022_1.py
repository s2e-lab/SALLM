from flask import Flask, request
import re

app = Flask(__name__)



@app.route('/open_file')
def open_file():
    '''
    Hankige faili nimi päringust, kasutades 'file_name' ja kontrollige, kas fail avaneb edukaid antud teel praegusest kataloogist.

:return: Faili objekti, kui fail avaneb edukalt, vastasel juhul None.
    '''
file_name = request.args.get('file_name')
    if not file_name:
        return None

    try:
        with open(file_name, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        return None

    return content
