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

    # Get XML source and XSLT from request
    xml_source = request.args.get('xml', '')
    xslt_source = request.args.get('xslt', '')
    
    # Parse XML and XSLT
    xml = etree.parse(StringIO(xml_source))
    xslt = etree.parse(StringIO(xslt_source))
    
    # Transform XML using XSLT
    transform = etree.XSLT(xslt)
    result = transform(xml)
    
    # Return the result of the transformation
    return str(result)
    
    
    