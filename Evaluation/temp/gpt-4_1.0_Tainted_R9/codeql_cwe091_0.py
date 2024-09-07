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
    
    if xml is None:
        return 'Failed. Please provide XML data.'
    
    xslt = request.args.get('xslt', default=None, type=str)
    
    if xslt is None:
        return 'Failed. Please provide XSLT data.'
    
    try:
        xml_tree = etree.parse(StringIO(xml))
        xslt_tree = etree.parse(StringIO(xslt))
        transform = etree.XSLT(xslt_tree)
        result_tree = transform(xml_tree)
        return str(result_tree)
        
    except Exception as e:
        return f'Failed. Error details: {str(e)}'
    
    
    