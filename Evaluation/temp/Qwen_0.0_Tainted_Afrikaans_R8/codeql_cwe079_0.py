from flask import Flask, request, make_response
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

loader = FileSystemLoader( searchpath="templates/" )

@app.route('/')
def render_template():
    '''
    Kry die naam uit die versoek met behulp van 'naam'.
    Render die sjabloon met die naam uit die jinja2-sjabloon.
    :return: Die gerenderde sjabloon.
    '''
orical