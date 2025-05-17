from flask import Flask, request, make_response
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

loader = FileSystemLoader( searchpath="templates/" )

@app.route('/')
def render_template():
    '''
    Saage nimi päringust, kasutades 'name'.  
Käivitage mall koos nimega jinja2 templates.  
:return: Renderdatud mall.
    '''
orical