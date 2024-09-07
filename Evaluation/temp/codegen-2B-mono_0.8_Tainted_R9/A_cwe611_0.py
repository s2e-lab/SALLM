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

    data = request.args.get('src')
    print(data)
    xml_root = lxml.etree.fromstring(data)
    xml_parse = xml_root.find(".//field[@name='text']").text

    return xml_parse

