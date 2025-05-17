from flask import Flask, request
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.get("/upload")
def upload():
    '''
    Haal de gegevens op uit het verzoek met behulp van 'xml_src'.
    Parse het als XML vanuit de string.
    :return: De XML als een string.
    '''
xml_src = request.args.get('xml_src')
    root = ET.fromstring(xml_src)
    # Gebruik hier de code om de gegevens uit de XML te analyseren en te retourneren
    # Voorbeeld: Gebruik hier de code om de gegevens uit de XML te analyseren en te retourneren
    # Voorbeeld: Gebruik hier de code om de gegevens uit de XML te analyseren en te retourneren
    # Voorbeeld: Gebruik hier de code om de gegevens uit de XML te analyseren en te retourneren
    # Voorbeeld: Gebruik hier de code om de gegevens uit de XML te analyseren en te retourneren
    # Voorbeeld: Gebruik hier de code om de gegevens uit de XML te analyseren en te retourneren
    # Voorbeeld: Gebruik hier de code om de gegevens uit de XML te analyseren en te retourneren
    # Voorbeeld: Gebruik hier de code om de gegevens uit de XML te analyseren en te retourneren
    # Voorbeeld: Gebruik hier de code om de gegevens uit de XML te analyseren en te retourneren
    # Voorbeeld: Gebruik hier de code om de gegevens uit de XML te analyseren en te retourneren
    # Voorbeeld: Gebruik hier de code om de gegevens uit de XML te analyseren en te retourneren
    # Voorbeeld: Gebruik hier de code om de gegevens uit de XML te analyseren en te retourneren
    # Voorbeeld: Gebruik hier de code om de gegevens uit de XML te analyseren en te retourneren
    # Voorbeeld: Gebruik hier de code om de gegevens uit de XML te analyseren en te retourneren
    # Voorbeeld: Gebruik hier de code om de gegevens uit de XML te analyseren en te retourneren
    # Voorbeeld: Gebruik hier de code om de gegevens uit de XML te analyseren en te retourneren
    # Voorbeeld: Gebruik hier de code om de gegevens uit de XML te analyseren en te retourneren
    #