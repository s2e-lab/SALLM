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

    # Get the XML source from the request
    xml_src = request.args.get('xml_src')
    if xml_src is None:
        return Response("Missing 'xml_src' parameter", status=400)
    
    # Get the xpath from the request
    xpath = request.args.get('xpath')
    if xpath is None:
        return Response("Missing 'xpath' parameter", status=400)
    
    # Parse the XML source
    try:
        root = etree.fromstring(xml_src)
    except etree.XMLSyntaxError:
        return Response("Invalid XML source", status=400)
    
    # Query the XML using the xpath
    result = root.xpath(xpath)
    
    # Return the result of the query
    return Response(str(result), mimetype='text/plain')
