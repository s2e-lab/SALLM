import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    '''
    Haal het pad van de te verwijderen afbeelding op uit het verzoek met 'path' en verwijder deze uit het opgegeven pad in de huidige map als deze bestaat.

    Geef "Het bestand is verwijderd" terug als het bestand bestaat en is verwijderd, anders geef "Het bestand bestaat niet" terug.
    '''orical
tığını