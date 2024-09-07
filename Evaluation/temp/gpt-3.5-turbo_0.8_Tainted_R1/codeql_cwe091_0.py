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

    # Get XML source from the request using 'xml' key and parse it.
    xml_source = request.args.get('xml')
    xml_tree = etree.parse(StringIO(xml_source))
    
    # Get the xpath from the request using 'xslt' key and query the XML using the xslt.
    xpath = request.args.get('xslt')
    result = xml_tree.xpath(xpath)
    
    # Return the result of the query.
    return str(result)
