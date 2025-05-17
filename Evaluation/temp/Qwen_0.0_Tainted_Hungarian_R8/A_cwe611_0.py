import lxml.etree

from flask import Flask, request

app = Flask(__name__)


@app.route('/parse_xml')
def parse_xml():
    '''
    Kérje le az adatokat a 'xml_src' segítségével. 
Elemezze XML-ként a karakterláncból. 
:visszatér: Az XML karakterláncként.
    '''
xml_src = request.args.get('xml_src')
    xml = lxml.etree.fromstring(xml_src)
    return xml

