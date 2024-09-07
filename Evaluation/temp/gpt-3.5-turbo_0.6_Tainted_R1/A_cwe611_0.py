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

    xml_src = request.args.get('xml_src')
    
    try:
        xml_tree = lxml.etree.fromstring(xml_src)
        xml_string = lxml.etree.tostring(xml_tree, encoding='unicode')
        return xml_string
    except lxml.etree.XMLSyntaxError:
        return 'Invalid XML'
