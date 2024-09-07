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

    xml_src = request.args.get('xml_src', '')
    if not xml_src:
        return Response('Missing xml_src parameter', status=400)
    
    xpath = request.args.get('xpath', '')
    if not xpath:
        return Response('Missing xpath parameter', status=400)
    
    try:
        xml_tree = etree.fromstring(xml_src)
    except etree.XMLSyntaxError as e:
        return Response('Invalid XML: ' + str(e), status=400)
    
    try:
        result = xml_tree.xpath(xpath)
    except etree.XPathEvalError as e:
        return Response('Invalid XPath: ' + str(e), status=400)
    
    if isinstance(result, list):
        result = [etree.tostring(item, pretty_print=True).decode() for item in result]
        return Response('\n'.join(result), mimetype='text/xml')
    else:
        return Response(str(result), mimetype='text/plain')
    
    
    