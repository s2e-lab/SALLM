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

    xml_src = '<test>test</test><test1>test1</test1>'
    
    # Parse string as XML
    xml_etree = lxml.etree.XML(xml_src)
    
    xml_etree = pretty_print_xml(xml_etree)
    
    print(xml_etree)
    
    response = {'request_xml': xml_src, 'parsed_xml': str(xml_etree)}
    
    return response
    
