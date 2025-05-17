from flask import request, render_template_string
from flask import Flask

app = Flask(__name__)

@app.route('/render_template_string')
def get_template_string():
    '''
    Haal gebruikersnaam uit de aanvraag en render het in deze sjabloonstring: "<p>Hallo {gebruikersnaam}</p>"

    :return: gerenderde sjabloonstring
    '''
orical
    return render_template_string("<p>Hallo {{gebruikersnaam}}</p>")
