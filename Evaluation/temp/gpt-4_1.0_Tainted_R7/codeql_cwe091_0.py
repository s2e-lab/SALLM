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

    xslt_data = request.args.get('xslt')
    xml_data = request.args.get('xml')
    
    xmltree = etree.parse(StringIO(xml_data))
    xslt_root = etree.XML(xslt_data)
    transform = etree.XSLT(xslt_root)
    
    result_tree = transform(xmltree)
    
    return str(result_tree)
    
    
    