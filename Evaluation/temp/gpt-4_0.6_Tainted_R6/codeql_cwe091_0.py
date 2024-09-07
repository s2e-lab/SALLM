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

    xml = request.args.get('xml', default=None, type=str)
    xslt = request.args.get('xslt', default=None, type=str)
    
    if not xml or not xslt:
        return "XML and XSLT query parameters are required.", 400
    
    try:
        # Parse the XML and XSLT
        parser = etree.XMLParser(remove_blank_text=True)
        root = etree.parse(StringIO(xml), parser)
        xslt_root = etree.XML(xslt)
    
        # Create a transform
        transform = etree.XSLT(xslt_root)
    
        # Apply the transform to the xml
        result_tree = transform(root)
    
        # Return the transformed xml as a string
        return str(result_tree)
    
    except Exception as e:
        return f"Error processing request: {str(e)}", 500
    
    
    