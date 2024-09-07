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

    xml_string = request.args.get('xml')
    xslt_string = request.args.get('xslt')
    xml_root = etree.parse(StringIO(xml_string))
    
    xslt_root = etree.fromstring(xslt_string)
    transform = etree.XSLT(xslt_root)
    
    result = transform(xml_root)
    
    return str(result)
