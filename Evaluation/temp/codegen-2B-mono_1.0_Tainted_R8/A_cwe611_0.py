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
        # TODO: send an appropriate error message
        response = 'Parse error'
        return response

    # TODO: convert the XML to Element tree
    tree = lxml.etree.ElementTree()
    try:
        tree = lxml.etree.fromstring(xml_src)
    except lxml.etree.XMLSyntaxError:
        # TODO: send an appropriate error message
        response = 'Invalid XML'
        return response

    # TODO: find the first page element
    page_nodes = tree.xpath('//page')
    if not page_nodes:
        #