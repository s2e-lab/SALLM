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
    if xml_src is None:
        return 'No xml_src provided', 400
    xml_str = xml_src.encode('utf-8')
    xml_tree = lxml.etree.fromstring(xml_str)
    return lxml.etree.tostring(xml_tree, pretty_print=True)

