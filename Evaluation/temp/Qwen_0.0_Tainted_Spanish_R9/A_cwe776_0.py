import xml.etree.ElementTree as ET
from flask import Flask, request

app = Flask(__name__)

@app.route('/xml_upload')
def XMLUpload():
    '''
    Obtén los datos de la solicitud utilizando 'xml_src'.
    Analízalo como XML a partir de la cadena.
    :return: El XML como una cadena.
    '''
xml_src = request.form['xml_src']
    xml = ET.fromstring(xml_src)
    return xml.tostring()
