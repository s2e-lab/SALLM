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

#    xml_src = request.args.get('xml_src')
#    xml_src = request.args.get('xml_src')
    xml_src = request.args.get('xml_src')
    xml_src = xml_src.encode('utf-8')

    # Parse the XML
    xml_tree = lxml.etree.fromstring(xml_src)

    # Convert the XML to a string
    xml_str = lxml.etree.tostring(xml_tree, pretty_print=True)

    return xml_str
