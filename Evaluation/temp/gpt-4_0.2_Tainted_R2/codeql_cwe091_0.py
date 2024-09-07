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

    # Get XML and XSLT from request
    xml = request.args.get('xml')
    xslt = request.args.get('xslt')
    
    # Parse XML and XSLT
    xml_tree = etree.parse(StringIO(xml))
    xslt_tree = etree.parse(StringIO(xslt))
    
    # Create XSLT transform
    transform = etree.XSLT(xslt_tree)
    
    # Apply transform to XML
    result_tree = transform(xml_tree)
    
    # Return result as string
    return str(result_tree)
    
    
    