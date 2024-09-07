from lxml import etree

from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/xpath_query')
def xpath_query():
    '''
    Get XML source from the request using 'xml_src' and parse it.
    Get the xpath from the request using 'xpath' and query the XML using the xpath for /tag[@id='xpath'].
    :return: The result of the query.
    '''

    xml_src = request.args['xml_src']
    xpath = request.args['xpath']
    html_parser = etree.XMLParser(recover=True)
    root = etree.fromstring(xml_src.encode('utf-8'), html_parser)
    query = root.xpath(xpath)
    return str(query).replace('[','').replace(']','')
