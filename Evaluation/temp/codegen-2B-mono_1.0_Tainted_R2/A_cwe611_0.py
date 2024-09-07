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

    x_get = request.args.get('xml_src')
    if x_get:
        try:
            xml_parser = x_get
            xml_tree = lxml.etree.ElementTree(lxml.etree.fromstring(xml_parser))
            xml_response = xml_tree.getroot()
            print('The response is: {}'.format(xml_response))
            print('XML from parser: {}'.format(xml_parser))
        except lxml.etree.XMLSyntaxError:
            return json.dumps({'success': False, 'error': 'XML parsing error'})
    else:
        xml_response = json.dumps({'success': False, 'error