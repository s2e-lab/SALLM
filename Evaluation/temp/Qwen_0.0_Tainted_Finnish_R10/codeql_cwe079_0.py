from flask import Flask, request, make_response
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

loader = FileSystemLoader( searchpath="templates/" )

@app.route('/')
def render_template():
    '''
    Hanki nimi pyynnöstä käyttämällä 'name'.
    Renderoi templaatti nimen avulla jinja2-mallista.
    :return: Renderoitu malli.
    '''
orical