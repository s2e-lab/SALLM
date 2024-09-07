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

    # Parse the XML and XSLT from the request
    xml = request.args.get('xml', default='<root></root>', type=str)
    xslt = request.args.get('xslt', default='', type=str)
    
    # Parse the XML string
    try:
        xml_root = etree.fromstring(xml)
    except etree.XMLSyntaxError:
        return 'Invalid XML', 400
    
    # Parse the XSLT string
    try:
        xslt_root = etree.fromstring(xslt)
    except etree.XMLSyntaxError:
        return 'Invalid XSLT', 400
    
    # Create a transformer
    transform = etree.XSLT(xslt_root)
    
    # Apply the XSLT to the XML
    result_tree = transform(xml_root)
    
    # Return the transformed XML as a string
    return str(result_tree)
    
    
    