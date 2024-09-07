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

    xml_src = request.args.get('xml_src')
    if xml_src is None:
        return 'XML source not found in request', 400

    try:
        xml_tree = etree.XML(xml_src)
    except etree.XMLSyntaxError:
        return 'XML source is not valid', 400

    xpath = request.args.get('xpath')
    if xpath is None:
        return 'XPath not found in request', 400

    try:
        result = xml_tree.xpath(xpath)
    except etree.