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
        if xml_src == 'None':
            raise ValueError('No request parameter in the query')
        # If the request parameter isn't a string it'll throw a value error so we need to catch it.
        xml_src = xml_src.encode().decode('UTF-8')
        root = lxml.etree.fromstring(xml_src)
        return root
    except ValueError:
        return 'Error in the request parameter', 400

