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

    if 'xml' not in request.args:
        return "Error: No XML string was provided", 400
    try:
        xml = request.args.get('xml')
        tree = etree.parse(StringIO(xml))
        query = request.args.get('xslt')
    except:
        return "Error: The path to the request is invalid", 400
    
    if query is None:
        return "Error: No xslt query was provided", 400
        
    xml = tree.xslt(etree.XML(query))
    tree = etree.ElementTree(xml)

    return str