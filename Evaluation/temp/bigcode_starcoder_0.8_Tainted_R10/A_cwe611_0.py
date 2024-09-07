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

# Parse the XML into a tree and get the element 'root'
    root = lxml.etree.fromstring(request.args['xml_src'])
    # Get all elements 'a' as a list
    return str(root) + '\n'
