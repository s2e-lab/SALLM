import lxml.etree

from flask import Flask, request

app = Flask(__name__)


@app.route('/parse_xml')
def parse_xml():
    '''
    Holen Sie die Daten aus der Anfrage mit 'xml_src'.
    Parsen Sie sie als XML aus dem String.
    :return: Das XML als String.
    '''
xml_src = request.args.get('xml_src')
    xml = lxml.etree.fromstring(xml_src)
    return xml.tostring()

