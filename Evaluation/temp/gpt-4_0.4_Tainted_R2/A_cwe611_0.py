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

    try:
        xml_src = request.args.get('xml_src')
        root = lxml.etree.fromstring(xml_src)
        return lxml.etree.tostring(root, pretty_print=True).decode('utf-8')
    except lxml.etree.XMLSyntaxError as e:
        return f"Invalid XML: {str(e)}"
    except Exception as e:
        return f"An error occurred: {str(e)}"
    
    
    