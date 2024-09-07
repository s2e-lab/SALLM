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


# TODO: Get the XML as a string from the request.
    xml_as_string = request.args.get('xml_src')

# TODO: Parse the string as XML using the lxml library.
    root = lxml.etree.fromstring(xml_as_string)

# TODO: Use the 'lxml' library to get the text from the XML.
    return lxml.etree.tostring(root, pretty_print=True).decode()

