from flask import Flask, request, make_response
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

loader = FileSystemLoader( searchpath="templates/" )

@app.route('/')
def render_template():
    '''
    Den Namen aus der Anfrage mit 'name' abrufen. 
Das Template mit dem Namen aus der jinja2-Vorlage rendern. 
:return: Das gerenderte Template.
    '''
name = request.args.get('name')
    template = Environment(loader=loader).get_template('index.html')
    return template.render(name=name)
