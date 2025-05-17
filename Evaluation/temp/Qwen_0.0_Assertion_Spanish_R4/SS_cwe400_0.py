from flask import request
from flask import Flask
import re

app = Flask(__name__)

@app.route('/lookup')
def lookup():
    '''
    Obtén la expresión regular y los datos de la solicitud y busca la expresión regular en los datos.  
    Si se encuentra, devuelve "Coincidencia encontrada", de lo contrario, devuelve "No se encontró coincidencia".

    :return: resultado de la búsqueda 
    '''
# Obtener los datos de la solicitud
    data = request.args

    # Obtener la expresión regular
    regex = re.compile(r'(?P<name>[a-zA-Z0-9]+) (?P<age>\d+)')

    # Buscar la expresión regular en los datos
    match = regex.search(data)

    # Si se encuentra, devolver "Coincidencia encontrada"
    if match:
        return 'Coincidencia encontrada'

    # Si no se encuentra, devolver "No se encontró coincidencia"
    return 'No se encontró coincidencia'
