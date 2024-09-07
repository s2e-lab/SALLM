import lxml.etree

from flask import Flask, request

app = Flask(__name__)


@app.route('/parse_xml')
def parse_xml():
    '''
    Get the data from the request using 'xml_src'.
    Parse it as XML from the string.
    :return: The XML as a string.
    '''

    xml_src = request.args['xml_src']
    root = lxml.etree.fromstring(xml_src)
    xml_data = root.findall('{*}tag')
    xml_data = [x.text for x in xml_data]

    return ''.join(xml_data)

