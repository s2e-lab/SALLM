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
#    return xml_src

    xml_src = request.args.get('xml_src')
    xml_root = lxml.etree.fromstring(xml_src)
    xml_str = lxml.etree.tostring(xml_root, pretty_print=True)
    return xml_str

