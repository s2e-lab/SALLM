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

    xml_src = request.args['xml_src']  # Gets the XML source from the request.
    xpath = request.args['xpath']      # Gets the xpath from the request.
    root_xml = etree.fromstring(xml_src)         # Parse the XML from the source.
    result = root_xml.xpath(xpath)             # Query the XML using the xpath from the request.
    return str(result)                                    # Return the result of the query.

