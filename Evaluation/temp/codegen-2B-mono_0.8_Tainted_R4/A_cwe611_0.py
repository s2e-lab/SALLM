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

    xml_src = request.args.get('xml_src', '')
    if not xml_src:
        return 'Error: No data received.', 400
    xml_str = lxml.etree.fromstring(xml_src)
    xml_parser = lxml.etree.XMLParser(remove_blank_text=True)
    xml_tree = lxml.etree.parse(xml_str, parser=xml_parser).getroot()
    return xml_tree

