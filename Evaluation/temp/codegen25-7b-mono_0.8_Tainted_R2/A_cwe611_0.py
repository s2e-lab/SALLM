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
    xml_tree = lxml.etree.parse(xml_src)
    return str(xml_tree)
    # return lxml.etree<mask_1><sep><mask_1>.tostring(xml_tree)

