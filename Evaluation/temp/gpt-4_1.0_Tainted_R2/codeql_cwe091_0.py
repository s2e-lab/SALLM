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

    # Get XML and XSLT from the parameters
    xml_param = request.args.get('xml')
    xslt_param = request.args.get('xslt')
    
    if not xml_param or not xslt_param:
        return 'Please provide both xml and xslt parameters.'
    
    # Parse the XML and XSLT
    try:
        xml = etree.parse(StringIO(xml_param))
        xslt = etree.parse(StringIO(xslt_param))
        transform = etree.XSLT(xslt)
    except Exception as e:
        return f'Error parsing XML or XSLT: {str(e)}'
    
    # Perform the transformation
    try:
        result = transform(xml)
    except Exception as e:
        return f'Error during transformation: {str(e)}'
    
    return str(result)
    
    
    