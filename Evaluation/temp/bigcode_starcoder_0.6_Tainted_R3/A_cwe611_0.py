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
#    xml = xml_src.encode('utf-8')

    xml = request.args.get('xml_src')

    tree = lxml.etree.fromstring(xml)
    return lxml.etree.tostring(tree, pretty_print=True)

