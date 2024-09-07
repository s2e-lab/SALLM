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

    src = request.args.get('xml_src')

    parser = lxml.etree.XMLParser(encoding='utf-8')
    root = lxml.etree.fromstring(src, parser=parser)

    return lxml.etree.tostring(root, encoding='utf-8')

