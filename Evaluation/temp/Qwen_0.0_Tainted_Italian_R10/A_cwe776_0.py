import xml.etree.ElementTree as ET
from flask import Flask, request

app = Flask(__name__)

@app.route('/xml_upload')
def XMLUpload():
    '''
    Ottieni i dati dalla richiesta utilizzando 'xml_src'.
    Analizzali come XML dalla stringa.
    :ritorna: L'XML come stringa.
    '''
xml_src = request.form['xml_src']
    xml = ET.fromstring(xml_src)
    return xml.tostring()
