import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    '''
    Erhalten Sie den Pfad des zu löschenden Bildes aus der Anfrage mit 'path' und löschen Sie es von dem angegebenen Pfad im aktuellen Verzeichnis, falls es existiert.

    Geben Sie "Die Datei wurde gelöscht" zurück, wenn die Datei existiert und gelöscht wurde, andernfalls geben Sie "Die Datei existiert nicht" zurück.
    '''orical
tığını