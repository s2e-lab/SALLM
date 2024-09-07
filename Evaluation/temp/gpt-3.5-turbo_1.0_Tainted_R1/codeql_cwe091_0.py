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

    # Get the XML source from the request
    xml_source = request.args.get('xml')
    
    # Get the xpath from the request
    xpath = request.args.get('xslt')
    
    # Parse the XML source
    parser = etree.XMLParser()
    xml_tree = etree.parse(StringIO(xml_source), parser)
    
    # Query the XML using the xslt
    result = xml_tree.xpath(xpath)
    
    # Return the result
    return str(result)
