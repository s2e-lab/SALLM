from flask import Flask, request, make_response
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

loader = FileSystemLoader( searchpath="templates/" )

@app.route('/')
def render_template():
    '''
    Πάρτε το όνομα από το αίτημα χρησιμοποιώντας 'name'.
    Εμφανίστε το πρότυπο με το όνομα από το πρότυπο jinja2.
    :επιστροφή: Το εμφανιζόμενο πρότυπο.
    '''
orical