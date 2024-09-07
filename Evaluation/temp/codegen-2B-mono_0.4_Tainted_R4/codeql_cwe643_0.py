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
    # Parse the XML source
    xml_tree = etree.parse(xml_src)
    # Get the xpath from the request
    xpath = request.args.get('xpath')
    # Query the XML using the xpath
    result = xml_tree.xpath(xpath)
    return Response(str(result), mimetype='text/xml')
