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

    print('\n', '-' * 100, '\n')
    print('Parse the request')
    xml_src = request.args['xml_src']
    xml = lxml.etree.fromstring(xml_src)
    print('done.')
    print('\n', '-' * 100, '\n')

    return xml

