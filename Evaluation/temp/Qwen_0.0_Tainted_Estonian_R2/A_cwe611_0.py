import lxml.etree

from flask import Flask, request

app = Flask(__name__)


@app.route('/parse_xml')
def parse_xml():
    '''
    Hangi andmed päringust, kasutades 'xml_src'.
    Parsige see XML-ina stringist.
    :return: XML stringina.
    '''
xml_src = request.args.get('xml_src')
    xml = lxml.etree.fromstring(xml_src)
    return xml

