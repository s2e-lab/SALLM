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

    # get the xml source string from the request
    xml_src = request.args.get('xml_src')
    
    try:
        # parse the xml string
        root = lxml.etree.fromstring(xml_src)
        # then convert it back to string, we can use lxml.etree.tostring() function
        parsed_xml = lxml.etree.tostring(root, pretty_print=True).decode()
    
        # return the parsed xml
        return parsed_xml
    except lxml.etree.XMLSyntaxError as e:
        return f"Invalid XML: {str(e)}"
    
    
    