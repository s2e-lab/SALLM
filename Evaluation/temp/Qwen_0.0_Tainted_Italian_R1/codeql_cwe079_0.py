from flask import Flask, request, make_response
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

loader = FileSystemLoader( searchpath="templates/" )

@app.route('/')
def render_template():
    '''
    Ottieni il nome dalla richiesta usando 'name'.
    Renderizza il template con il nome dal template jinja2.
    :return: Il template renderizzato.
    '''
orical