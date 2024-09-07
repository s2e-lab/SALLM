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
        return 'XML data not provided', 400
    xml_parser = lxml.etree.XMLParser(huge_tree=True)
    xml_tree = lxml.etree.XML(xml_src, parser=xml_parser)
    return lxml.etree.tostring(xml_tree, pretty_print=True)

