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
    parsed_xml = etree.fromstring(xml_src)
    
    # Perform XPath query
    result_nodes = parsed_xml.xpath(xpath)
    
    # Prepare results
    results = []
    for node in result_nodes:
        results.append(etree.tostring(node).decode())
    
    return Response('\n'.join(results), mimetype='text/plain')
    
    
    