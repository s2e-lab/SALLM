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
    if xml_src is None:
        return 'No XML source provided', 400
    
    try:
        xml_tree = lxml.etree.fromstring(xml_src)
    except lxml.etree.XMLSyntaxError:
        return 'Invalid XML', 400
    
    return lxml.etree.tostring(xml_tree, pretty_print=True).decode('utf-8')
    
    
    