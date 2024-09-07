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
    if not xml_src:
        return "No xml_src provided", 400
    
    try:
        root = lxml.etree.fromstring(xml_src)
        return lxml.etree.tostring(root, pretty_print=True).decode()
    except lxml.etree.XMLSyntaxError as e:
        return f"Invalid XML: {e}", 400
    
    
    