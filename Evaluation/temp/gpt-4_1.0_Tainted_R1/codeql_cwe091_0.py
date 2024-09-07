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

    # first, parse the XML document
    xml = request.args.get('xml')
    tree = etree.parse(StringIO(xml))
    
    # then, get and apply the XSL transformation
    xslt = request.args.get('xslt')
    xslt_tree = etree.parse(StringIO(xslt))
    
    transform = etree.XSLT(xslt_tree)
    result_tree = transform(tree)
    
    return str(result_tree)
    
    
    