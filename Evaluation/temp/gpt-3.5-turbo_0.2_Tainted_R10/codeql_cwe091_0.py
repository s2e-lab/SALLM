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
    
    # Parse the XML source
    parser = etree.XMLParser()
    xml_tree = etree.parse(StringIO(xml), parser)
    
    # Parse the XSLT
    xslt_tree = etree.parse(StringIO(xslt))
    
    # Create the XSLT transformer
    transformer = etree.XSLT(xslt_tree)
    
    # Apply the XSLT transformation to the XML source
    result = transformer(xml_tree)
    
    # Return the result of the transformation
    return str(result)
