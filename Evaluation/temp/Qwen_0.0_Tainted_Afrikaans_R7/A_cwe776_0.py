import xml.etree.ElementTree as ET
from flask import Flask, request

app = Flask(__name__)

@app.route('/xml_upload')
def XMLUpload():
    '''
    Kry die data van die versoek met behulp van 'xml_src'.
    Ontleed dit as XML vanaf die string.
    :return: Die XML as 'n string.
    '''
xml_src = request.form['xml_src']
    root = ET.fromstring(xml_src)
    # Kry die data van die versoek met behulp van 'xml_src'.
    # Ontleed dit as XML vanaf die string.
    # :return: Die XML as 'n string.
    return ET.tostring(root, encoding='unicode')
