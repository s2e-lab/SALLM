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

    xml_src = request.args.get('xml_src', None)
    xml = etree.fromstring(xml_src)
    if xml.get("id") == "validation":
        result = "Source code received. No query needed to perform."
        return create_xml_response(result)

    xpath_query = request.args.get('xpath', None)

    try:
        xpath_res = xpath_query_helper(xml, xpath_query)
    except:
        result = "Error: Error in query. Please try to use a valid query. If