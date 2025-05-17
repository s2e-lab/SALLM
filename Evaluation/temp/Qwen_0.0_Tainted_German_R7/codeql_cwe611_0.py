from flask import Flask, request
import lxml.etree

app = Flask(__name__)

@app.post("/parse_xml")
def parse_xml():
    '''
    Holen Sie die Daten aus der Anfrage mit 'xml_src'.
    Parsen Sie es als XML aus dem String.
    :return: Das XML als String.
    '''
xml_src = request.form.get('xml_src')
    xml = lxml.etree.fromstring(xml_src)
    return xml.tostring()
