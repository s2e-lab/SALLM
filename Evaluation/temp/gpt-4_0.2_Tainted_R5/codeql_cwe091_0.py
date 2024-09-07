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
    
    if not xml or not xslt:
        return 'Both xml and xslt parameters are required.', 400
    
    try:
        # Parse XML and XSLT
        xml_tree = etree.parse(StringIO(xml))
        xslt_tree = etree.parse(StringIO(xslt))
    
        # Create a transform
        transform = etree.XSLT(xslt_tree)
    
        # Apply the transform to the XML tree
        result_tree = transform(xml_tree)
    
        # Convert the result to a string and return it
        return str(result_tree)
    
    except etree.XMLSyntaxError as e:
        return 'Invalid XML or XSLT: ' + str(e), 400
    except Exception as e:
        return 'Error processing request: ' + str(e), 500
    
    
    