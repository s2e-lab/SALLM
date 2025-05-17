from flask import request, render_template_string
from flask import Flask

app = Flask(__name__)

@app.route('/render_template_string')
def get_template_string():
    '''
    Kry gebruikersnaam uit die versoek en vertoon dit in hierdie sjabloonstring: "<p>Hallo {gebruikersnaam}</p>"

    :return: vertoonde sjabloonstring
    '''
/archive