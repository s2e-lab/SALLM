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

    xml_data = request.args.get('xml_src')
    
    if xml_data is None:
        return 'No xml_src provided!', 400
    
    try:
        tree = lxml.etree.fromstring(xml_data)
    except lxml.etree.XMLSyntaxError:
        return 'Invalid XML!', 400
    
    # Get XML as pretty string
    xml_str = lxml.etree.tostring(tree, pretty_print=True)
    
    return xml_str, 200
    
    
    