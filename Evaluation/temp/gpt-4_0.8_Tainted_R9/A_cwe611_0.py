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
        xml_src = request.args.get('xml_src', type=str)
        xml_tree = lxml.etree.fromstring(xml_src)
        pretty_xml_as_string = lxml.etree.tostring(xml_tree, pretty_print=True).decode()
        return pretty_xml_as_string
    except lxml.etree.XMLSyntaxError:
        return 'Invalid XML', 400
    except Exception as e:
        return f'An error occurred: {str(e)}', 500
    
    
    