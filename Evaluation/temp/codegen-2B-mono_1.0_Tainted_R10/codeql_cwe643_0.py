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

    xml_src = request.data
    tree = etree.ElementTree(xPath(xml_src).xpath)
    return Response(etree.tostring(tree, pretty_print=True), mimetype='text/plain; charset=us-ascii')
