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

    try:
        # Get XML and XSLT from request
        xml = request.args.get('xml')
        xslt = request.args.get('xslt')
    
        # Parse XML and XSLT
        xml_parsed = etree.parse(StringIO(xml))
        xslt_parsed = etree.parse(StringIO(xslt))
    
        # Create XSLT Transformation
        transform = etree.XSLT(xslt_parsed)
    
        # Transform XML using XSLT
        result = transform(xml_parsed)
    
        return str(result)
    
    except Exception as e:
        return f"Error: {str(e)}"
    
    
    