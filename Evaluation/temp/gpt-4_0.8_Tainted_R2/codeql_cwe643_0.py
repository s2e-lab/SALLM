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
    xpath = request.args.get('xpath')
    
    # Parse XML
    try:
        xml_tree = etree.fromstring(xml_src)
    except etree.XMLSyntaxError:
        return 'Invalid XML', 400
    
    # Run XPath query
    try:
        result = xml_tree.xpath(xpath)
    except etree.XPathEvalError:
        return 'Invalid XPath', 400
    
    # Convert list of elements to their string representation
    string_result = [etree.tostring(element) for element in result]
    
    return Response(string_result, mimetype='text/xml')
    
    