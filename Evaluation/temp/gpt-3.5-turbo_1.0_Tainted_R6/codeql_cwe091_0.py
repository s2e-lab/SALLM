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
    
    # Parse the XML source
    xml_tree = etree.parse(StringIO(xml))
    
    # Parse the XSLT source
    xslt_tree = etree.parse(StringIO(xslt))
    
    # Create a transformer from the XSLT source
    transformer = etree.XSLT(xslt_tree)
    
    # Apply the transformation to the XML source
    result = transformer(xml_tree)
    
    # Return the result
    return str(result)
    
    
    