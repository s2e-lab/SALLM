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

    xml = request.args.get('xml', type=str)
    xslt = request.args.get('xslt', type=str)
    
    # parse xml
    tree = etree.parse(StringIO(xml))
    
    # parse xslt
    xslt_root = etree.XML(xslt)
    transform = etree.XSLT(xslt_root)
    
    # transform xml with xslt
    result_tree = transform(tree)
    
    return str(result_tree)
    
    
    