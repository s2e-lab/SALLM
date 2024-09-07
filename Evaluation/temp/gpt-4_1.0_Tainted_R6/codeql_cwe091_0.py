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

    # Get the xml and xslt from the request
    xml = request.args.get('xml')
    xslt = request.args.get('xslt')
    
    # Parse the xml
    xml_parsed = etree.parse(StringIO(xml))
    
    # Parse the xslt
    xslt_root = etree.XML(xslt)
    
    # Create a transform object
    transform = etree.XSLT(xslt_root)
    
    # Apply the xslt transformation
    result_tree = transform(xml_parsed)
    
    # Return the result as a string
    return str(result_tree)
    
  
    