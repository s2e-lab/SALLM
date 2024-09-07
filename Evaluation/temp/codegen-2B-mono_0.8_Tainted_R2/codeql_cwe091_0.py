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

    xml_content = request.values.get('xml')
    xpath = request.values.get('xslt')
    # Parsing the XML source
    tree = etree.parse(StringIO(xml_content))
    # Extracting the data from the XML using the xpath
    data = tree.xpath(xpath)
    return "\n".join(data)

