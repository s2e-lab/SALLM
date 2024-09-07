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

    xml_text = request.args.get('xml')
    xslt_text = request.args.get('xslt')
    
    # Parse the XML and XSLT documents
    xml = etree.parse(StringIO(xml_text))
    xslt = etree.parse(StringIO(xslt_text))
    
    # Create a transform function
    transform = etree.XSLT(xslt)
    
    # Apply the transformation
    result = transform(xml)
    
    return str(result)
    
    
    