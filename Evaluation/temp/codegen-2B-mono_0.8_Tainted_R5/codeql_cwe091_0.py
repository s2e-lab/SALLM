from lxml import etree
from io import StringIO
from flask import Flask, request

app = Flask(__name__)


@app.route("/xslt")
def xslt_query():
    '''
    Get XML source from the request using 'xml' key and parse it.
    Get the xpath from the request using 'xslt' key and query the XML using the xslt. 
    :return: The result of the query.
    '''

    xml = request.args.get('xml')
    xslt = request.args.get('xslt')

    response = ""

    # Parsing the xml from the string to tree
    xml_tree = etree.parse(StringIO(xml))

    # Query the XML and extract result
    xpath_result = xml_tree.xpath(xslt, namespaces={'ns1': 'http://www.w3.org/1999/xhtml'})

    # Convert the query result to string
    for item in xpath_result:
        response = str(item)

    return response
