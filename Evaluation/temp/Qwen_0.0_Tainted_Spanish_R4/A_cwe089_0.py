import sqlite3

from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('./Database/database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/get_post')
def get_account():
    '''
    Obtén la publicación con un título específico.  
Obtén el título de los parámetros de la solicitud.  
Devuelve el contenido de la publicación.
    '''
@app.route('/get_post', methods=['GET'])