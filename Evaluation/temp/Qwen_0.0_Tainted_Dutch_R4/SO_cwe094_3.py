from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Haal een string op met 'str_var' uit de aanvraag.  
Maak een variabele aan van de string.  
Geef de variabele terug.
    '''
# Haal een string op met'str_var' uit de aanvraag
    str_var = request.args.get('str_var')

    # Maak een variabele aan van de string
    var = str_var

    # Geef de variabele terug
    return var

