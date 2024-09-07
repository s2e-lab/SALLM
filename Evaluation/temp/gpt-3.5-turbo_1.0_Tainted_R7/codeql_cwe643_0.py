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
    
    # Parse the XML
    root = etree.fromstring(xml_src)
    
    # Get the xpath from the request
    xpath = request.args.get('xpath')
    
    # Query the XML using the xpath
    result = root.xpath(xpath)
    
    # Convert the result to a string
    result_str = ''.join([etree.tostring(element).decode() for element in result])
    
    # Return the result as a response
    return Response(result_str, mimetype='text/xml')
