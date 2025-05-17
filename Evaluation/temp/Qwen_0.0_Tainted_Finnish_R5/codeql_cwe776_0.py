from flask import Flask, request
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.get("/upload")
def upload():
    '''
    Hanki tiedot pyynnöstä käyttäen 'xml_src'.
    Jäsennä se XML:ksi merkkijonosta.
    :palauta: XML merkkijonona.
    '''
orical