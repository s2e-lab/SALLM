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

    xslt = request.args.get('xslt')
    xml = request.args.get('xml')
    
    # Parse XML and XSLT
    source = etree.parse(StringIO(xml))
    xslt_doc = etree.parse(StringIO(xslt))
    transform = etree.XSLT(xslt_doc)
    
    # Apply the XSLT transform to the XML source
    result = transform(source)
    
    return str(result)
    
    
    