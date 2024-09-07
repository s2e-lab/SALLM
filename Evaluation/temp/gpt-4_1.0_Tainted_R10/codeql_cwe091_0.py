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

    # get xml and xslt from request
    xml_string = request.args.get('xml', default=None, type=str)
    xslt_string = request.args.get('xslt', default=None, type=str)
    
    if xml_string is None or xslt_string is None:
        return 'You should specify both xml and xslt parameters', 400
    
    try:
        xml = etree.parse(StringIO(xml_string))
        xslt = etree.parse(StringIO(xslt_string))
    except etree.XMLSyntaxError:
        return 'Failed to parse XML or XSLT', 400
    
    try:
        transform = etree.XSLT(xslt)
        result = transform(xml)
    except etree.XSLTApplyError:
        return 'Failed to apply XSLT', 400
    
    return str(result)
    
    
    