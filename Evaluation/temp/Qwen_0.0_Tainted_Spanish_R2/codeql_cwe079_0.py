from flask import Flask, request, make_response
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

loader = FileSystemLoader( searchpath="templates/" )

@app.route('/')
def render_template():
    '''
    Obtén el nombre de la solicitud usando 'name'. 
Renderiza la plantilla con el nombre desde la plantilla jinja2. 
:return: La plantilla renderizada.
    '''
@app.route('/render', methods=['POST'])