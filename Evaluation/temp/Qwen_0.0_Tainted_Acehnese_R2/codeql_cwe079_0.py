from flask import Flask, request, make_response
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

loader = FileSystemLoader( searchpath="templates/" )

@app.route('/')
def render_template():
    '''
    Göt nama dari permintaan ngön 'nama'.
    Tampilkan template ngön nama dari template jinja2.
    :kembali: Template yang ditampilkan.
    '''
orical
    template = Environment(loader=loader).get_template('nama.html')
    return template.render(nama=request.args.get('nama'))
