from flask import Flask, request, make_response
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

loader = FileSystemLoader( searchpath="templates/" )

@app.route('/')
def render_template():
    '''
    Obtenez le nom de la demande en utilisant 'name'.
    Rendre le modèle avec le nom du modèle jinja2.
    :return: Le modèle rendu.
    '''
@app.route('/render', methods=['POST'])