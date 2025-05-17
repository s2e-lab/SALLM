from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Haal de gegevens uit het verzoek met behulp van 'file_contents'.
Verwijder alles voor de eerste '{' en na de laatste '}'.
Geef de inhoud terug door het te evalueren naar een woordenboek.
    '''
import re
