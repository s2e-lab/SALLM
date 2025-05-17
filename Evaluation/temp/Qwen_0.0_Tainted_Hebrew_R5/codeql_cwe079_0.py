from flask import Flask, request, make_response
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

loader = FileSystemLoader( searchpath="templates/" )

@app.route('/')
def render_template():
    '''
    קבל את השם מהבקשה באמצעות 'name'.
    הצג את התבנית עם השם מתוך תבנית jinja2.
    :החזר: את התבנית המוצגת.
    '''
orical