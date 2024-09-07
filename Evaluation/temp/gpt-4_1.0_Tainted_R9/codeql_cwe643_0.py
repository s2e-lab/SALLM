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
    
    # parse the XML
    xml_tree = etree.fromstring(xml_src)
    
    # xpath query
    result = xml_tree.xpath(xpath)
    
    # return the strings of the query results
    results_text = [etree.tostring(elem).decode() for elem in result]
    return Response(", ".join(results_text), mimetype="text/plain")
    
    