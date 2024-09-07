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

    # Get the XML source and XSLT from the request query parameters
    xml_source = request.args.get('xml', None)
    xslt_source = request.args.get('xslt', None)
    
    # If any of the parameters are missing, return an error message
    if xml_source is None or xslt_source is None:
        return 'Both XML and XSLT are required parameters.', 400
    
    try:
        # Parse the XML and XSLT
        xml = etree.parse(StringIO(xml_source))
        xslt = etree.parse(StringIO(xslt_source))
    
        # Transform the XML using the XSLT
        transform = etree.XSLT(xslt)
        result = transform(xml)
    
        # Return the result as a string
        return str(result)
    
    except etree.XMLSyntaxError as e:
        # If there is a parsing error, return an error message
        return f'Error parsing XML or XSLT: {str(e)}', 400
    
    except Exception as e:
        # If there is any other error, return an error message
        return f'Error processing XSLT transformation: {str(e)}', 500
    
    
    