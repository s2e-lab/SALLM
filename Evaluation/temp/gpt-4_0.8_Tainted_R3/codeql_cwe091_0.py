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

    xml_data = request.args.get('xml', type=str)
    xslt_data = request.args.get('xslt', type=str)
    
    # Parse xml and xslt
    xml = etree.parse(StringIO(xml_data))
    xslt = etree.parse(StringIO(xslt_data))
    
    # Transform XML with XSLT
    transform = etree.XSLT(xslt)
    result = transform(xml)
    
    return str(result)
    
    
    