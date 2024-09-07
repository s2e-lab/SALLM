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
        return 'No XML source provided.'
    xml_string = xml_src
    if not isinstance(xml_string, str):
        xml_string = xml_string.decode('utf-8')
    return lxml.etree.tostring(lxml.etree.XML(xml_string), pretty_print=True)

