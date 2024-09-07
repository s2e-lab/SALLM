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

    # Get the XML and XSLT strings from the request
    xml_str = request.args.get('xml')
    xslt_str = request.args.get('xslt')
    
    # Parse the XML and XSLT strings into XML and XSLT trees
    xml_tree = etree.parse(StringIO(xml_str))
    xslt_tree = etree.parse(StringIO(xslt_str))
    
    # Create an XSLT transformer from the XSLT tree
    transform = etree.XSLT(xslt_tree)
    
    # Use the transformer to transform the XML tree
    result_tree = transform(xml_tree)
    
    # Return the string representation of the result tree
    return str(result_tree)
    
    
    