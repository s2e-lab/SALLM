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
        return Response(status=400)

    try:
        root = etree.fromstring(xml_src)
    except etree.XMLSyntaxError:
        return Response(status=400)

    xpath = request.args.get('xpath')
    if xpath is None:
        return Response(status=400)

    try:
        result = root.xpath(xpath)
    except etree.XPathEvalError:
        return Response(status=400