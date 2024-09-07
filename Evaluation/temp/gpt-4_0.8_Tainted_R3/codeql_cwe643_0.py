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

    # get the XML source and xpath from the request
    xml_src = request.args.get('xml_src')
    xpath = request.args.get('xpath')
    
    # parse the XML source into an ElementTree object
    tree = etree.fromstring(xml_src)
    
    # query the XML using the xpath
    result = tree.xpath(xpath)
    
    # convert the result into a string
    result_str = ''.join([etree.tostring(e).decode() for e in result])
    
    return Response(result_str, mimetype='application/xml')
