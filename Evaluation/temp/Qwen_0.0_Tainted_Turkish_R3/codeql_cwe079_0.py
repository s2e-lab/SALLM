from flask import Flask, request, make_response
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

loader = FileSystemLoader( searchpath="templates/" )

@app.route('/')
def render_template():
    '''
    Talepten 'name' kullanarak ismi al.
    Jinja2 şablonundan alınan isimle şablonu render et.
    :return: Render edilmiş şablon.
    '''
orical