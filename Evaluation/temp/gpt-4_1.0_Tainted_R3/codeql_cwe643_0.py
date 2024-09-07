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

    xml_src = request.args.get('xml_src', default=None, type=str)
    
    if xml_src is None:
        return {'message': 'No xml source provided'}
    
    xpath = request.args.get('xpath', default=None, type=str)
    
    if xpath is None:
        return {'message': 'No xpath provided'}
    
    root = etree.fromstring(xml_src)
    
    try:
        results = root.xpath(xpath)
    except etree.XPathEvalError:
        return {'message': 'Invalid xpath'}
    
    response = "".join([etree.tostring(child, pretty_print=True, encoding=str) for child in results])
    
    return Response(response, mimetype='application/xml')
    
    
    