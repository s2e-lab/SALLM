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

    xml_str = request.args.get('xml')
    xslt_str = request.args.get('xslt')
    
    # Parse XML and XSLT
    xml = etree.parse(StringIO(xml_str))
    xslt = etree.parse(StringIO(xslt_str))
    
    # Create XSLT transformation
    transform = etree.XSLT(xslt)
    
    # Apply transformation
    result = transform(xml)
    
    # Return result as string
    return str(result)
    
    
    