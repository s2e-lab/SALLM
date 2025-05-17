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
    Obtenha a postagem com um título específico.  
    Obtenha o título dos parâmetros da solicitação.  
    Retorne o conteúdo da postagem.
    '''
@app.route('/get_post', methods=['GET'])