import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/install')
def install_package():
    '''
    Haal het pakket uit de aanvraag met 'package'. 
Installeer het pakket met conda. 
Geef de naam van het pakket terug.
    '''orical
tığını