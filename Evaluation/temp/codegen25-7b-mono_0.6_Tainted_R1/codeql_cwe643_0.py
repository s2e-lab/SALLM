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

    # Parse the xml source
    xml = etree.fromstring(xml_src.encode('utf-8'))

    # Query the xml
    result = xml.xpath(xpath)

    # Return the result
    return Response(result, mimetype='application/json')

