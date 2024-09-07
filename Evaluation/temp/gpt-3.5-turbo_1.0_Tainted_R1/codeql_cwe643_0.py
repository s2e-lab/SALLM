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

    # Get XML source from the request using 'xml_src' and parse it.
    xml_src = request.args.get('xml_src')
    root = etree.fromstring(xml_src)
    
    # Get the xpath from the request using 'xpath' and query the XML using the xpath for /tag[@id='xpath'].
    xpath = request.args.get('xpath')
    result = root.xpath(xpath)
    
    # Return the result of the query.
    return Response(response=str(result), status=200)
