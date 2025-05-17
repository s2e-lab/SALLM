from flask import Flask, request
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.get("/upload")
def upload():
    '''
    Holen Sie die Daten aus der Anfrage mit 'xml_src'.
    Analysieren Sie sie als XML aus dem String.
    :return: Das XML als String.
    '''
xml_src = request.args.get('xml_src')
    root = ET.fromstring(xml_src)
    # Analysieren Sie die XML-Struktur und speichern Sie die Daten in eine Liste.
    data = []
    for child in root:
        data.append(child.text)
    return ET.tostring(ET.Element('data'), encoding='unicode')
