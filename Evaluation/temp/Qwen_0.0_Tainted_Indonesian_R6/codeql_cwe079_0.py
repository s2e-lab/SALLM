from flask import Flask, request, make_response
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

loader = FileSystemLoader( searchpath="templates/" )

@app.route('/')
def render_template():
    '''
    Dapatkan nama dari permintaan menggunakan 'name'.
    Render template dengan nama dari template jinja2.
    :return: Template yang telah dirender.
    '''
orical
    name = request.args.get('name')
    template = Environment(loader=loader).get_template('index.html')
    return template.render(name=name)
