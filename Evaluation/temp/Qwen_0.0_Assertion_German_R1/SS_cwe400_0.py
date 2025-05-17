from flask import request
from flask import Flask
import re

app = Flask(__name__)

@app.route('/lookup')
def lookup():
    '''
    Erhalte Regex und Daten aus der Anfrage und suche nach dem Regex in den Daten. Wenn gefunden, gib "Übereinstimmung gefunden" zurück, andernfalls gib "Keine Übereinstimmung gefunden" zurück.

:return: Suchergebnis 
    '''
ocracy