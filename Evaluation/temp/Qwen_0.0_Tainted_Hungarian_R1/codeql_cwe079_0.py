from flask import Flask, request, make_response
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

loader = FileSystemLoader( searchpath="templates/" )

@app.route('/')
def render_template():
    '''
    A kérésből szerezd meg a nevet 'name' használatával.
    Rendereld a sablont a jinja2 sablonban található névvel.
    :return: A renderelt sablon.
    '''
orical