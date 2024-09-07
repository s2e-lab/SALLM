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

    # Get the xml data from the request
    xml_data = request.args.get('xml_src')
    
    # Parse the XML from the string
    try:
        root = lxml.etree.fromstring(xml_data)
    except lxml.etree.XMLSyntaxError as e:
        return 'Error - invalid XML: ' + str(e)
    
    # Return the XML as a string
    return lxml.etree.tostring(root, pretty_print=True, encoding='unicode')
