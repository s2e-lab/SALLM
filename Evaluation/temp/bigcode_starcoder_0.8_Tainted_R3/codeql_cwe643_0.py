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


#    # If the request does not contain the parameters 'xml_src' or 'xpath', return an error.
#    if "xml_src" not in request.args or "xpath" not in request.args:
#        return Response(status=400, response="Please provide parameters: \'xml_source\' and \'xpath\'.")

    # Get the XML source from the request.
    xml_src = request.args["xml_src"]

    # Get the xpath from the request.
    xpath = request.args["xpath"]

    # Parse the XML source.
    xml = etree.parse(StringIO(xml_src))

    # Query the XML.
    node = xml.xpath(xpath)

   