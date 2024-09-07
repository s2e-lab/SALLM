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

    # Get XML source and xslt from the request
    xml_source = request.args.get('xml')
    xslt_source = request.args.get('xslt')
    
    # Check if XML and XSLT source are provided
    if not xml_source or not xslt_source:
        return "XML and XSLT source must be provided", 400
    
    # Parse the XML and XSLT
    try:
        xml_tree = etree.parse(StringIO(xml_source))
        xslt_tree = etree.parse(StringIO(xslt_source))
    
        # Create a transformer
        transform = etree.XSLT(xslt_tree)
    
        # Apply the transformation
        result_tree = transform(xml_tree)
    
        # Return the result as string
        return str(result_tree)
    
    except etree.XMLSyntaxError:
        return "Invalid XML or XSLT syntax", 400
    
    except Exception as e:
        return str(e), 500
    
    
    