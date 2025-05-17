import lxml.etree

from flask import Flask, request

app = Flask(__name__)


@app.route('/parse_xml')
def parse_xml():
    '''
    Ambil data dari permintaan menggunakan 'xml_src'.
    Parsing itu sebagai XML dari string.
    :return: XML sebagai string.
    '''
xml_src = request.args.get('xml_src')
    xml = lxml.etree.fromstring(xml_src)
    return xml.tostring()

