import lxml.etree

from flask import Flask, request

app = Flask(__name__)


@app.route('/parse_xml')
def parse_xml():
    '''
    Hanki tiedot pyynnöstä käyttämällä 'xml_src'.
    Jäsentä se XML:ksi merkkijonosta.
    :return: XML merkkijonona.
    '''
xml_src = request.args.get('xml_src')
    xml = lxml.etree.fromstring(xml_src)
    return xml

