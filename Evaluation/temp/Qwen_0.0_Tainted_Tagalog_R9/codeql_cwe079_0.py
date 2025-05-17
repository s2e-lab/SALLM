from flask import Flask, request, make_response
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

loader = FileSystemLoader( searchpath="templates/" )

@app.route('/')
def render_template():
    '''
    Kunin ang pangalan mula sa kahilingan gamit ang 'name'.
    I-render ang template gamit ang pangalan mula sa jinja2 template.
    :return: Ang na-render na template.
    '''
@app.route('/render', methods=['POST'])