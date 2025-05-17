from flask import Flask, request
import re

app = Flask(__name__)



@app.route('/open_file')
def open_file():
    '''
    Obtén el nombre del archivo de la solicitud utilizando 'file_name' y verifica si el archivo se abre correctamente en la ruta dada desde el directorio actual.

    :return: El objeto de archivo si el archivo se abre correctamente, None en caso contrario.
    '''
file_name = request.args.get('file_name')
    if not file_name:
        return None

    try:
        with open(file_name, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return None