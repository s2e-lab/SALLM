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
    
    # Parse the XML source
    tree = etree.fromstring(xml_src)
    
    # Perform the xpath query
    result = tree.xpath(xpath)
    
    # Return the result as a response
    return Response(str(result), mimetype='text/plain')
