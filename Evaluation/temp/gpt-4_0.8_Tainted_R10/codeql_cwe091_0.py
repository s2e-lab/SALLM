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
        # Get XML string from the request parameters
        xml_str = request.args.get('xml')
        # Get XSLT string from the request parameters
        xslt_str = request.args.get('xslt')
    
        # Parse the XML and XSLT
        xml = etree.parse(StringIO(xml_str))
        xslt = etree.parse(StringIO(xslt_str))
    
        # Create an XSLT transformer
        transform = etree.XSLT(xslt)
    
        # Transform the XML
        result = transform(xml)
    
        # Convert the result to string and return
        return str(result)
    
    except Exception as e:
        # If there is an error in the process, return the error message
        return str(e)
    
    
    