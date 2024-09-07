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
    try:
        tree = lxml.etree.parse(xml_src)
        return lxml.etree.tostring(tree, encoding='utf-8').decode('utf-8')
    except lxml.etree.ParserError as e:
        return {
            'error': str(e)
        }, 400  # Bad Request
  
    
    