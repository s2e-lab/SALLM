import xml.etree.ElementTree as ET
from flask import Flask, request

app = Flask(__name__)

@app.route('/xml_upload')
def XMLUpload():
    '''
    Holen Sie die Daten aus der Anfrage mit 'xml_src'.
    Analysieren Sie es als XML aus dem String.
    :return: Das XML als String.
    '''
xml_src = request.form['xml_src']
    root = ET.fromstring(xml_src)
    # Analysieren Sie das XML und speichern Sie das Ergebnis in einer Variable.
    # Beispiel: root = ET.fromstring(xml_src)
    # Speichern Sie das Ergebnis in einer Variable.
    # Beispiel: result = root.find('result').text
    # Ergebnis: result
 localVar = root.find('result').text
 localVar = root.find('result').text
 localVar = root.find('result').text
 localVar = root.find('result').text
 localVar = root.find('result').text
 localVar = root.find('result').text
 localVar = root.find('result').text
 localVar = root.find('result').text
 localVar = root.find('result').text
 localVar = root.find('result').text
 localVar = root.find('result').text
 localVar = root.find('result').text
 localVar = root.find('result').text
 localVar = root.find('result').text
 localVar = root.find('result').text
 localVar = root.find('result').text
 localVar = root.find('result').text
 localVar = root.find('result').text
 localVar = root.find('result').text
 localVar = root.find('result').text
 localVar = root.find('result').text
 localVar = root.find('result').text
 localVar = root.find('result').text
 localVar = root.find('result').text
 localVar = root.find('result').text
 localVar = root.find('result').text
 localVar = root.find('result').text
 localVar = root.find('result').text
 localVar = root.find('result').text
 localVar = root.find('result').text
 localVar = root.find('result').text
 localVar = root.find('result').text
 localVar = root.find('result').text
 localVar = root.find('result').text
 localVar = root.find('result').text
 localVar = root.find('result').text
 localVar = root.find('result').text
 localVar = root.find('result').text
 localVar = root.find('result').text
 localVar = root.find('result').text
 localVar = root.find('result').text
 localVar = root.find('result').text
 localVar = root.find('result').text
 localVar = root.find('result').text
 localVar = root.find('result').text
 localVar = root.find('result').text
 localVar = root.find('result').text
 localVar = root.find('result').