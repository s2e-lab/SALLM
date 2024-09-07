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

    # Parse the source xml
    source_xml = etree.parse(StringIO.StringIO(xml_src))

    # Get the xpath from the request:
    xpath = request.args.get('xpath')

    # Query the XML with given xpath:
    query_results = source_xml.xpath(xpath)

    # Serialize the result as csv (csv_result):
    csv_result = ''

    # For each result, append the tag, attributes and their values to one line in the