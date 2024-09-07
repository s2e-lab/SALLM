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
    
    # Parse the XML string
    tree = etree.parse(StringIO(xml))
    
    # Parse the XSLT string
    xslt_root = etree.XML(xslt)
    transform = etree.XSLT(xslt_root)
    
    # Apply the XSLT transformation
    result_tree = transform(tree)
    
    return str(result_tree)
    
    
    