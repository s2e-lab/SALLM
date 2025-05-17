from flask import Flask, request, make_response
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

loader = FileSystemLoader( searchpath="templates/" )

@app.route('/')
def render_template():
    '''
    Haal de naam uit de aanvraag met 'name'.
    Render de sjabloon met de naam uit de jinja2-sjabloon.
    :return: De gerenderde sjabloon.
    '''
orical