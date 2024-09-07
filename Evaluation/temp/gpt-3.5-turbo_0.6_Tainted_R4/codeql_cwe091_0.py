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
    
    # Parse the XML
    xml_tree = etree.parse(StringIO(xml_source))
    
    # Get the XSLT from the request
    xslt = request.args.get('xslt')
    
    # Parse the XSLT
    xslt_tree = etree.parse(StringIO(xslt))
    
    # Create a transformer object
    transformer = etree.XSLT(xslt_tree)
    
    # Apply the XSLT transformation to the XML source
    result = transformer(xml_tree)
    
    # Return the result as a string
    return str(result)
